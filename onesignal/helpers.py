"""Helpers for common OneSignal API usage patterns."""

import collections
import time
import uuid

import urllib3

from onesignal.exceptions import ApiException


CreateNotificationWithRetryResult = collections.namedtuple(
    'CreateNotificationWithRetryResult', ['response', 'was_replayed']
)

_RETRYABLE_STATUSES = (429, 503)
_MIN_BASE_DELAY = 1.0
_MAX_BASE_DELAY = 60.0


def _header_value(headers, name):
    if not headers:
        return None
    name = name.lower()
    try:
        items = headers.items()
    except AttributeError:
        return None
    for key, value in items:
        if str(key).lower() == name:
            return value
    return None


def _was_replayed(headers):
    value = _header_value(headers, 'idempotent-replayed')
    return value is not None and str(value).strip().lower() == 'true'


def _retry_delay(headers, attempt, base_delay):
    retry_after = _header_value(headers, 'retry-after')
    if retry_after is not None:
        try:
            return max(float(retry_after), 0.0)
        except (TypeError, ValueError):
            pass
    return base_delay * (2 ** attempt)


def create_notification_with_retry(api, notification, max_retries=3, base_delay=1.0):
    """Create a notification with safe, idempotent retries.

    Ensures ``notification.idempotency_key`` is set (generating a UUIDv4 when
    absent) so the server can deduplicate, then calls ``create_notification``.
    Transient failures (HTTP 429, HTTP 503, or connection-level errors) are
    retried up to ``max_retries`` times with the SAME idempotency key,
    honoring the ``Retry-After`` response header when present and falling back
    to exponential backoff (``base_delay * 2**attempt`` seconds) otherwise.
    Other errors are raised immediately.

    :param api: a ``DefaultApi`` instance
    :param notification: the ``Notification`` to send; an existing
        ``idempotency_key`` is respected, never overwritten
    :param max_retries: retries after the initial attempt (default 3)
    :param base_delay: backoff base in seconds when ``Retry-After`` is absent;
        clamped to [1.0, 60.0]
    :return: ``CreateNotificationWithRetryResult`` with ``response`` (the
        ``CreateNotificationSuccessResponse``) and ``was_replayed`` (True when
        the server answered from a previously completed request, as signaled
        by the ``Idempotent-Replayed`` response header)
    """
    if not getattr(notification, 'idempotency_key', None):
        notification.idempotency_key = str(uuid.uuid4())

    # Clamp the backoff base so a stray value can neither hammer the API
    # (too small) nor stall the caller for an unbounded stretch (too large).
    base_delay = min(_MAX_BASE_DELAY, max(_MIN_BASE_DELAY, base_delay))

    attempt = 0
    while True:
        try:
            data, _status, headers = api.create_notification(
                notification, _return_http_data_only=False
            )
            return CreateNotificationWithRetryResult(
                response=data, was_replayed=_was_replayed(headers)
            )
        except ApiException as e:
            if e.status not in _RETRYABLE_STATUSES or attempt >= max_retries:
                raise
            delay = _retry_delay(e.headers, attempt, base_delay)
        except urllib3.exceptions.HTTPError:
            if attempt >= max_retries:
                raise
            delay = base_delay * (2 ** attempt)
        if delay > 0:
            time.sleep(delay)
        attempt += 1

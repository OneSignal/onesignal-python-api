# AGENTS.md — OneSignal Python SDK

Integration guide for AI agents and LLMs using the OneSignal server SDK for Python. Human-oriented docs are in the [README](./README.md).

## What this SDK does

Server-side access to the OneSignal REST API: send push / email / SMS, manage users, subscriptions, segments, templates and live activities, and administer apps & API keys.

- PyPI package: `onesignal-python-api` (import as `onesignal`)
- Repository: https://github.com/OneSignal/onesignal-python-api

## Install

```sh
pip install onesignal-python-api
```

## Authentication — two key types

OneSignal uses two bearer credentials; each endpoint requires a specific one:

- **REST API key** — used by almost every endpoint (notifications, users, subscriptions, segments, templates, live activities, custom events). Found in **App Settings → Keys & IDs**.
- **Organization API key** — required *only* for organization-level endpoints: app management (list / create / get / update apps), API-key management (view / create / update / rotate / delete API keys), and copying a template to another app. Found in **Organization Settings**.

Set both on one `Configuration`; the SDK sends the correct credential per endpoint. Never hard-code keys — read them from environment variables or a secrets manager.

```python
import os
import onesignal
from onesignal.api import default_api

configuration = onesignal.Configuration(
    rest_api_key=os.environ['ONESIGNAL_REST_API_KEY'],
    organization_api_key=os.environ['ONESIGNAL_ORGANIZATION_API_KEY'],
)

with onesignal.ApiClient(configuration) as api_client:
    client = default_api.DefaultApi(api_client)
```

## Calling convention

Methods take **positional arguments**. Build the model object and pass it directly — do **not** wrap arguments in a request/options object.

```python
from onesignal.model.notification import Notification
from onesignal.model.language_string_map import LanguageStringMap

notification = Notification(
    app_id='YOUR_APP_ID',
    contents=LanguageStringMap(en='Hello from OneSignal!'),
    include_aliases={'external_id': ['YOUR_USER_EXTERNAL_ID']},
    target_channel='push',
)

response = client.create_notification(notification)
```

## Idempotent sends & retries

Set `idempotency_key` (a UUID) so a create-notification request can be safely retried — the server returns the original result instead of sending twice. The `create_notification_with_retry` helper handles this for you: it generates an `idempotency_key` when absent, retries `429` / `503` / transport errors with the **same** key (honoring `Retry-After`), and reports via `was_replayed` whether the server answered from a previously completed request.

```python
result = client.create_notification_with_retry(notification, max_retries=5, base_delay=1.0)
print('id:', result.response.id, 'replayed:', result.was_replayed)
```

> The notification-level `external_id` field is the **deprecated** idempotency mechanism — prefer `idempotency_key`. Don't confuse it with the `external_id` **alias label** (under `include_aliases`) used to target users.

## Full API reference

- [DefaultApi.md](https://github.com/OneSignal/onesignal-python-api/blob/main/docs/DefaultApi.md) — every endpoint, parameter, and model, with runnable examples.
- [OneSignal REST API reference](https://documentation.onesignal.com/reference)

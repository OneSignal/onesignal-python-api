<h1 align="center">Welcome to onesignal-python-api</h1>
<p>
  <a href="https://pypi.org/project/onesignal-python-api/" target="_blank">
    <img alt="Version" src="https://img.shields.io/pypi/v/onesignal-python-api">
  </a>
  <a href="https://github.com/OneSignal/onesignal-python-api#readme" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://github.com/OneSignal/onesignal-python-api/graphs/commit-activity" target="_blank">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" />
  </a>
</p>

A powerful way to send personalized messages at scale and build effective customer engagement strategies. Learn more at onesignal.com

- API version: 5.3.0
- Package version: 5.3.0

## Requirements

Python >=3.6

## Installation

```sh
pip install onesignal-python-api
```

## Configuration

Every SDK requires authentication via API keys. Two key types are available:

- **REST API Key** — required for most endpoints (sending notifications, managing users, etc.). Found in your app's **Settings > Keys & IDs**.
- **Organization API Key** — only required for organization-level endpoints like creating or listing apps. Found in **Organization Settings**.

> **Warning:** Store your API keys in environment variables or a secrets manager. Never commit them to source control.

```python
import onesignal
from onesignal.api import default_api

configuration = onesignal.Configuration(
    rest_api_key='YOUR_REST_API_KEY',
    organization_api_key='YOUR_ORGANIZATION_API_KEY',
)

with onesignal.ApiClient(configuration) as api_client:
    client = default_api.DefaultApi(api_client)
```

## Send a push notification

```python
notification = onesignal.Notification(
    app_id='YOUR_APP_ID',
    contents=onesignal.StringMap(en='Hello from OneSignal!'),
    headings=onesignal.StringMap(en='Push Notification'),
    included_segments=['Subscribed Users'],
)

response = client.create_notification(notification)
print('Notification ID:', response.id)
```

## Send an email

```python
notification = onesignal.Notification(
    app_id='YOUR_APP_ID',
    email_subject='Important Update',
    email_body='<h1>Hello!</h1><p>This is an HTML email.</p>',
    included_segments=['Subscribed Users'],
    channel_for_external_user_ids='email',
)

response = client.create_notification(notification)
```

## Send an SMS

```python
notification = onesignal.Notification(
    app_id='YOUR_APP_ID',
    contents=onesignal.StringMap(en='Your SMS message content here'),
    included_segments=['Subscribed Users'],
    channel_for_external_user_ids='sms',
    sms_from='+15551234567',
)

response = client.create_notification(notification)
```

## Full API reference

The complete list of API endpoints and their parameters is available in the [DefaultApi documentation](https://github.com/OneSignal/onesignal-python-api/blob/main/docs/DefaultApi.md).

For the underlying REST API, see the [OneSignal API reference](https://documentation.onesignal.com/reference).

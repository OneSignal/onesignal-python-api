<h1 align="center">Welcome to @onesignal/python-onesignal 👋</h1>
<p>
  <a href="https://pypi.org/project/onesignal-python-api/" target="_blank">
    <img alt="Version" src="https://img.shields.io/pypi/v/onesignal-python-api">
  </a>
  <a href="https://github.com/OneSignal/python-onesignal#readme" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://github.com/OneSignal/python-onesignal/graphs/commit-activity" target="_blank">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" />
  </a>
  <a href="https://twitter.com/onesignal" target="_blank">
    <img alt="Twitter: onesignal" src="https://img.shields.io/twitter/follow/onesignal.svg?style=social" />
  </a>
</p>

A powerful way to send personalized messages at scale and build effective customer engagement strategies. Learn more at onesignal.com

- API version: 1.0.1
- Package version: 1.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install
```sh
pip install onesignal-python-api
```

You can also install directly from GitHub using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```

You may need to run `pip` with root permission:
```sh
sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

To install the package for all users:
```sh
sudo python setup.py install
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import onesignal
from onesignal.api import default_api

# See configuration.py for a list of all supported configuration parameters.
# Some of the OneSignal endpoints require USER_KEY bearer token for authorization as long as others require APP_KEY
# (also knows as REST_API_KEY). We recommend adding both of them in the configuration page so that you will not need
# to figure it yourself.
configuration = onesignal.Configuration(
    app_key = "YOUR_APP_KEY",
    user_key = "YOUR_USER_KEY"
)


# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
```

## Documentation for API Endpoints

All URIs are relative to *https://onesignal.com/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**cancel_notification**](docs/DefaultApi.md#cancel_notification) | **DELETE** /notifications/{notification_id} | Stop a scheduled or currently outgoing notification
*DefaultApi* | [**create_app**](docs/DefaultApi.md#create_app) | **POST** /apps | Create an app
*DefaultApi* | [**create_notification**](docs/DefaultApi.md#create_notification) | **POST** /notifications | Create notification
*DefaultApi* | [**create_player**](docs/DefaultApi.md#create_player) | **POST** /players | Add a device
*DefaultApi* | [**create_segments**](docs/DefaultApi.md#create_segments) | **POST** /apps/{app_id}/segments | Create Segments
*DefaultApi* | [**delete_player**](docs/DefaultApi.md#delete_player) | **DELETE** /players/{player_id} | Delete a user record
*DefaultApi* | [**delete_segments**](docs/DefaultApi.md#delete_segments) | **DELETE** /apps/{app_id}/segments/{segment_id} | Delete Segments
*DefaultApi* | [**export_players**](docs/DefaultApi.md#export_players) | **POST** /players/csv_export?app_id&#x3D;{app_id} | CSV export
*DefaultApi* | [**get_app**](docs/DefaultApi.md#get_app) | **GET** /apps/{app_id} | View an app
*DefaultApi* | [**get_apps**](docs/DefaultApi.md#get_apps) | **GET** /apps | View apps
*DefaultApi* | [**get_notification**](docs/DefaultApi.md#get_notification) | **GET** /notifications/{notification_id} | View notification
*DefaultApi* | [**get_notification_history**](docs/DefaultApi.md#get_notification_history) | **POST** /notifications/{notification_id}/history | Notification History
*DefaultApi* | [**get_notifications**](docs/DefaultApi.md#get_notifications) | **GET** /notifications | View notifications
*DefaultApi* | [**get_outcomes**](docs/DefaultApi.md#get_outcomes) | **GET** /apps/{app_id}/outcomes | View Outcomes
*DefaultApi* | [**get_player**](docs/DefaultApi.md#get_player) | **GET** /players/{player_id} | View device
*DefaultApi* | [**get_players**](docs/DefaultApi.md#get_players) | **GET** /players | View devices
*DefaultApi* | [**update_app**](docs/DefaultApi.md#update_app) | **PUT** /apps/{app_id} | Update an app
*DefaultApi* | [**update_player**](docs/DefaultApi.md#update_player) | **PUT** /players/{player_id} | Edit device
*DefaultApi* | [**update_player_tags**](docs/DefaultApi.md#update_player_tags) | **PUT** /apps/{app_id}/users/{external_user_id} | Edit tags with external user id


## Documentation For Models

 - [App](docs/App.md)
 - [Apps](docs/Apps.md)
 - [BasicNotification](docs/BasicNotification.md)
 - [BasicNotificationAllOf](docs/BasicNotificationAllOf.md)
 - [BasicNotificationAllOfAndroidBackgroundLayout](docs/BasicNotificationAllOfAndroidBackgroundLayout.md)
 - [Button](docs/Button.md)
 - [Buttons](docs/Buttons.md)
 - [CancelNotificationSuccessResponse](docs/CancelNotificationSuccessResponse.md)
 - [CreateNotificationBadRequestResponse](docs/CreateNotificationBadRequestResponse.md)
 - [CreateNotificationSuccessResponse](docs/CreateNotificationSuccessResponse.md)
 - [CreatePlayerSuccessResponse](docs/CreatePlayerSuccessResponse.md)
 - [CreateSegmentBadRequestResponse](docs/CreateSegmentBadRequestResponse.md)
 - [CreateSegmentConflictResponse](docs/CreateSegmentConflictResponse.md)
 - [CreateSegmentSuccessResponse](docs/CreateSegmentSuccessResponse.md)
 - [DeletePlayerBadRequestResponse](docs/DeletePlayerBadRequestResponse.md)
 - [DeletePlayerNotFoundResponse](docs/DeletePlayerNotFoundResponse.md)
 - [DeletePlayerSuccessResponse](docs/DeletePlayerSuccessResponse.md)
 - [DeleteSegmentBadRequestResponse](docs/DeleteSegmentBadRequestResponse.md)
 - [DeleteSegmentNotFoundResponse](docs/DeleteSegmentNotFoundResponse.md)
 - [DeleteSegmentSuccessResponse](docs/DeleteSegmentSuccessResponse.md)
 - [DeliveryData](docs/DeliveryData.md)
 - [ExportPlayersRequestBody](docs/ExportPlayersRequestBody.md)
 - [ExportPlayersSuccessResponse](docs/ExportPlayersSuccessResponse.md)
 - [Filter](docs/Filter.md)
 - [FilterExpressions](docs/FilterExpressions.md)
 - [GetNotificationRequestBody](docs/GetNotificationRequestBody.md)
 - [InvalidIdentifierError](docs/InvalidIdentifierError.md)
 - [NoSubscribersError](docs/NoSubscribersError.md)
 - [Notification](docs/Notification.md)
 - [Notification200Errors](docs/Notification200Errors.md)
 - [NotificationAllOf](docs/NotificationAllOf.md)
 - [NotificationHistoryBadRequestResponse](docs/NotificationHistoryBadRequestResponse.md)
 - [NotificationHistorySuccessResponse](docs/NotificationHistorySuccessResponse.md)
 - [NotificationSlice](docs/NotificationSlice.md)
 - [NotificationTarget](docs/NotificationTarget.md)
 - [NotificationWithMeta](docs/NotificationWithMeta.md)
 - [NotificationWithMetaAllOf](docs/NotificationWithMetaAllOf.md)
 - [Operator](docs/Operator.md)
 - [OutcomeData](docs/OutcomeData.md)
 - [OutcomesData](docs/OutcomesData.md)
 - [PlatformDeliveryData](docs/PlatformDeliveryData.md)
 - [PlatformDeliveryDataEmailAllOf](docs/PlatformDeliveryDataEmailAllOf.md)
 - [PlatformDeliveryDataSmsAllOf](docs/PlatformDeliveryDataSmsAllOf.md)
 - [Player](docs/Player.md)
 - [PlayerNotificationTarget](docs/PlayerNotificationTarget.md)
 - [PlayerSlice](docs/PlayerSlice.md)
 - [Players](docs/Players.md)
 - [Purchase](docs/Purchase.md)
 - [Segment](docs/Segment.md)
 - [SegmentNotificationTarget](docs/SegmentNotificationTarget.md)
 - [StringMap](docs/StringMap.md)
 - [UpdatePlayerSuccessResponse](docs/UpdatePlayerSuccessResponse.md)
 - [UpdatePlayerTagsRequestBody](docs/UpdatePlayerTagsRequestBody.md)
 - [UpdatePlayerTagsSuccessResponse](docs/UpdatePlayerTagsSuccessResponse.md)


## Author

devrel@onesignal.com


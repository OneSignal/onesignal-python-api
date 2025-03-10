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

- API version: 1.4.0
- Package version: 2.2.0
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

All URIs are relative to *https://api.onesignal.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**begin_live_activity**](docs/DefaultApi.md#begin_live_activity) | **POST** /apps/{app_id}/live_activities/{activity_id}/token | Start Live Activity
*DefaultApi* | [**cancel_notification**](docs/DefaultApi.md#cancel_notification) | **DELETE** /notifications/{notification_id} | Stop a scheduled or currently outgoing notification
*DefaultApi* | [**create_app**](docs/DefaultApi.md#create_app) | **POST** /apps | Create an app
*DefaultApi* | [**create_notification**](docs/DefaultApi.md#create_notification) | **POST** /notifications | Create notification
*DefaultApi* | [**create_player**](docs/DefaultApi.md#create_player) | **POST** /players | Add a device
*DefaultApi* | [**create_segments**](docs/DefaultApi.md#create_segments) | **POST** /apps/{app_id}/segments | Create Segments
*DefaultApi* | [**create_subscription**](docs/DefaultApi.md#create_subscription) | **POST** /apps/{app_id}/users/by/{alias_label}/{alias_id}/subscriptions | 
*DefaultApi* | [**create_user**](docs/DefaultApi.md#create_user) | **POST** /apps/{app_id}/users | 
*DefaultApi* | [**delete_alias**](docs/DefaultApi.md#delete_alias) | **DELETE** /apps/{app_id}/users/by/{alias_label}/{alias_id}/identity/{alias_label_to_delete} | 
*DefaultApi* | [**delete_player**](docs/DefaultApi.md#delete_player) | **DELETE** /players/{player_id} | Delete a user record
*DefaultApi* | [**delete_segments**](docs/DefaultApi.md#delete_segments) | **DELETE** /apps/{app_id}/segments/{segment_id} | Delete Segments
*DefaultApi* | [**delete_subscription**](docs/DefaultApi.md#delete_subscription) | **DELETE** /apps/{app_id}/subscriptions/{subscription_id} | 
*DefaultApi* | [**delete_user**](docs/DefaultApi.md#delete_user) | **DELETE** /apps/{app_id}/users/by/{alias_label}/{alias_id} | 
*DefaultApi* | [**end_live_activity**](docs/DefaultApi.md#end_live_activity) | **DELETE** /apps/{app_id}/live_activities/{activity_id}/token/{subscription_id} | Stop Live Activity
*DefaultApi* | [**export_events**](docs/DefaultApi.md#export_events) | **POST** /notifications/{notification_id}/export_events?app_id&#x3D;{app_id} | Export CSV of Events
*DefaultApi* | [**export_players**](docs/DefaultApi.md#export_players) | **POST** /players/csv_export?app_id&#x3D;{app_id} | Export CSV of Players
*DefaultApi* | [**fetch_aliases**](docs/DefaultApi.md#fetch_aliases) | **GET** /apps/{app_id}/subscriptions/{subscription_id}/user/identity | 
*DefaultApi* | [**fetch_user**](docs/DefaultApi.md#fetch_user) | **GET** /apps/{app_id}/users/by/{alias_label}/{alias_id} | 
*DefaultApi* | [**fetch_user_identity**](docs/DefaultApi.md#fetch_user_identity) | **GET** /apps/{app_id}/users/by/{alias_label}/{alias_id}/identity | 
*DefaultApi* | [**get_app**](docs/DefaultApi.md#get_app) | **GET** /apps/{app_id} | View an app
*DefaultApi* | [**get_apps**](docs/DefaultApi.md#get_apps) | **GET** /apps | View apps
*DefaultApi* | [**get_eligible_iams**](docs/DefaultApi.md#get_eligible_iams) | **GET** /apps/{app_id}/subscriptions/{subscription_id}/iams | 
*DefaultApi* | [**get_notification**](docs/DefaultApi.md#get_notification) | **GET** /notifications/{notification_id} | View notification
*DefaultApi* | [**get_notification_history**](docs/DefaultApi.md#get_notification_history) | **POST** /notifications/{notification_id}/history | Notification History
*DefaultApi* | [**get_notifications**](docs/DefaultApi.md#get_notifications) | **GET** /notifications | View notifications
*DefaultApi* | [**get_outcomes**](docs/DefaultApi.md#get_outcomes) | **GET** /apps/{app_id}/outcomes | View Outcomes
*DefaultApi* | [**get_player**](docs/DefaultApi.md#get_player) | **GET** /players/{player_id} | View device
*DefaultApi* | [**get_players**](docs/DefaultApi.md#get_players) | **GET** /players | View devices
*DefaultApi* | [**identify_user_by_alias**](docs/DefaultApi.md#identify_user_by_alias) | **PATCH** /apps/{app_id}/users/by/{alias_label}/{alias_id}/identity | 
*DefaultApi* | [**identify_user_by_subscription_id**](docs/DefaultApi.md#identify_user_by_subscription_id) | **PATCH** /apps/{app_id}/subscriptions/{subscription_id}/user/identity | 
*DefaultApi* | [**transfer_subscription**](docs/DefaultApi.md#transfer_subscription) | **PATCH** /apps/{app_id}/subscriptions/{subscription_id}/owner | 
*DefaultApi* | [**update_app**](docs/DefaultApi.md#update_app) | **PUT** /apps/{app_id} | Update an app
*DefaultApi* | [**update_live_activity**](docs/DefaultApi.md#update_live_activity) | **POST** /apps/{app_id}/live_activities/{activity_id}/notifications | Update a Live Activity via Push
*DefaultApi* | [**update_player**](docs/DefaultApi.md#update_player) | **PUT** /players/{player_id} | Edit device
*DefaultApi* | [**update_player_tags**](docs/DefaultApi.md#update_player_tags) | **PUT** /apps/{app_id}/users/{external_user_id} | Edit tags with external user id
*DefaultApi* | [**update_subscription**](docs/DefaultApi.md#update_subscription) | **PATCH** /apps/{app_id}/subscriptions/{subscription_id} | 
*DefaultApi* | [**update_user**](docs/DefaultApi.md#update_user) | **PATCH** /apps/{app_id}/users/by/{alias_label}/{alias_id} | 


## Documentation For Models

 - [App](docs/App.md)
 - [Apps](docs/Apps.md)
 - [BasicNotification](docs/BasicNotification.md)
 - [BasicNotificationAllOf](docs/BasicNotificationAllOf.md)
 - [BasicNotificationAllOfAndroidBackgroundLayout](docs/BasicNotificationAllOfAndroidBackgroundLayout.md)
 - [BeginLiveActivityRequest](docs/BeginLiveActivityRequest.md)
 - [Button](docs/Button.md)
 - [Buttons](docs/Buttons.md)
 - [CancelNotificationSuccessResponse](docs/CancelNotificationSuccessResponse.md)
 - [CreateNotificationSuccessResponse](docs/CreateNotificationSuccessResponse.md)
 - [CreatePlayerSuccessResponse](docs/CreatePlayerSuccessResponse.md)
 - [CreateSegmentConflictResponse](docs/CreateSegmentConflictResponse.md)
 - [CreateSegmentSuccessResponse](docs/CreateSegmentSuccessResponse.md)
 - [CreateSubscriptionRequestBody](docs/CreateSubscriptionRequestBody.md)
 - [CreateUserConflictResponse](docs/CreateUserConflictResponse.md)
 - [CreateUserConflictResponseErrorsInner](docs/CreateUserConflictResponseErrorsInner.md)
 - [CreateUserConflictResponseErrorsItemsMeta](docs/CreateUserConflictResponseErrorsItemsMeta.md)
 - [DeletePlayerNotFoundResponse](docs/DeletePlayerNotFoundResponse.md)
 - [DeletePlayerSuccessResponse](docs/DeletePlayerSuccessResponse.md)
 - [DeleteSegmentNotFoundResponse](docs/DeleteSegmentNotFoundResponse.md)
 - [DeleteSegmentSuccessResponse](docs/DeleteSegmentSuccessResponse.md)
 - [DeliveryData](docs/DeliveryData.md)
 - [ExportEventsSuccessResponse](docs/ExportEventsSuccessResponse.md)
 - [ExportPlayersRequestBody](docs/ExportPlayersRequestBody.md)
 - [ExportPlayersSuccessResponse](docs/ExportPlayersSuccessResponse.md)
 - [Filter](docs/Filter.md)
 - [FilterExpressions](docs/FilterExpressions.md)
 - [GenericError](docs/GenericError.md)
 - [GenericErrorErrorsInner](docs/GenericErrorErrorsInner.md)
 - [GetNotificationRequestBody](docs/GetNotificationRequestBody.md)
 - [IdentityObject](docs/IdentityObject.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [InlineResponse202](docs/InlineResponse202.md)
 - [InvalidIdentifierError](docs/InvalidIdentifierError.md)
 - [NoSubscribersError](docs/NoSubscribersError.md)
 - [Notification](docs/Notification.md)
 - [Notification200Errors](docs/Notification200Errors.md)
 - [NotificationAllOf](docs/NotificationAllOf.md)
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
 - [PlayerNotificationTargetIncludeAliases](docs/PlayerNotificationTargetIncludeAliases.md)
 - [PlayerSlice](docs/PlayerSlice.md)
 - [Players](docs/Players.md)
 - [PropertiesDeltas](docs/PropertiesDeltas.md)
 - [PropertiesObject](docs/PropertiesObject.md)
 - [Purchase](docs/Purchase.md)
 - [RateLimiterError](docs/RateLimiterError.md)
 - [Segment](docs/Segment.md)
 - [SegmentNotificationTarget](docs/SegmentNotificationTarget.md)
 - [StringMap](docs/StringMap.md)
 - [SubscriptionObject](docs/SubscriptionObject.md)
 - [TransferSubscriptionRequestBody](docs/TransferSubscriptionRequestBody.md)
 - [UpdateLiveActivityRequest](docs/UpdateLiveActivityRequest.md)
 - [UpdateLiveActivitySuccessResponse](docs/UpdateLiveActivitySuccessResponse.md)
 - [UpdatePlayerSuccessResponse](docs/UpdatePlayerSuccessResponse.md)
 - [UpdatePlayerTagsRequestBody](docs/UpdatePlayerTagsRequestBody.md)
 - [UpdatePlayerTagsSuccessResponse](docs/UpdatePlayerTagsSuccessResponse.md)
 - [UpdateSubscriptionRequestBody](docs/UpdateSubscriptionRequestBody.md)
 - [UpdateUserRequest](docs/UpdateUserRequest.md)
 - [User](docs/User.md)
 - [UserIdentityRequestBody](docs/UserIdentityRequestBody.md)
 - [UserIdentityResponse](docs/UserIdentityResponse.md)
 - [UserSubscriptionOptions](docs/UserSubscriptionOptions.md)


## Author

devrel@onesignal.com


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

- API version: 5.2.0
- Package version: 5.2.0-beta1
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
# Some of the OneSignal endpoints require ORGANIZATION_API_KEY token for authorization, while others require REST_API_KEY.
# We recommend adding both of them in the configuration page so that you will not need to figure it out yourself.
configuration = onesignal.Configuration(
    rest_api_key = "YOUR_REST_API_KEY", # App REST API key required for most endpoints
    organization_api_key = "YOUR_ORGANIZATION_KEY" # Organization key is only required for creating new apps and other top-level endpoints
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
*DefaultApi* | [**cancel_notification**](docs/DefaultApi.md#cancel_notification) | **DELETE** /notifications/{notification_id} | Stop a scheduled or currently outgoing notification
*DefaultApi* | [**create_alias**](docs/DefaultApi.md#create_alias) | **PATCH** /apps/{app_id}/users/by/{alias_label}/{alias_id}/identity | 
*DefaultApi* | [**create_alias_by_subscription**](docs/DefaultApi.md#create_alias_by_subscription) | **PATCH** /apps/{app_id}/subscriptions/{subscription_id}/user/identity | 
*DefaultApi* | [**create_app**](docs/DefaultApi.md#create_app) | **POST** /apps | Create an app
*DefaultApi* | [**create_notification**](docs/DefaultApi.md#create_notification) | **POST** /notifications | Create notification
*DefaultApi* | [**create_segment**](docs/DefaultApi.md#create_segment) | **POST** /apps/{app_id}/segments | Create Segment
*DefaultApi* | [**create_subscription**](docs/DefaultApi.md#create_subscription) | **POST** /apps/{app_id}/users/by/{alias_label}/{alias_id}/subscriptions | 
*DefaultApi* | [**create_user**](docs/DefaultApi.md#create_user) | **POST** /apps/{app_id}/users | 
*DefaultApi* | [**delete_alias**](docs/DefaultApi.md#delete_alias) | **DELETE** /apps/{app_id}/users/by/{alias_label}/{alias_id}/identity/{alias_label_to_delete} | 
*DefaultApi* | [**delete_segment**](docs/DefaultApi.md#delete_segment) | **DELETE** /apps/{app_id}/segments/{segment_id} | Delete Segment
*DefaultApi* | [**delete_subscription**](docs/DefaultApi.md#delete_subscription) | **DELETE** /apps/{app_id}/subscriptions/{subscription_id} | 
*DefaultApi* | [**delete_user**](docs/DefaultApi.md#delete_user) | **DELETE** /apps/{app_id}/users/by/{alias_label}/{alias_id} | 
*DefaultApi* | [**export_events**](docs/DefaultApi.md#export_events) | **POST** /notifications/{notification_id}/export_events?app_id&#x3D;{app_id} | Export CSV of Events
*DefaultApi* | [**export_subscriptions**](docs/DefaultApi.md#export_subscriptions) | **POST** /players/csv_export?app_id&#x3D;{app_id} | Export CSV of Subscriptions
*DefaultApi* | [**get_aliases**](docs/DefaultApi.md#get_aliases) | **GET** /apps/{app_id}/users/by/{alias_label}/{alias_id}/identity | 
*DefaultApi* | [**get_aliases_by_subscription**](docs/DefaultApi.md#get_aliases_by_subscription) | **GET** /apps/{app_id}/subscriptions/{subscription_id}/user/identity | 
*DefaultApi* | [**get_app**](docs/DefaultApi.md#get_app) | **GET** /apps/{app_id} | View an app
*DefaultApi* | [**get_apps**](docs/DefaultApi.md#get_apps) | **GET** /apps | View apps
*DefaultApi* | [**get_notification**](docs/DefaultApi.md#get_notification) | **GET** /notifications/{notification_id} | View notification
*DefaultApi* | [**get_notification_history**](docs/DefaultApi.md#get_notification_history) | **POST** /notifications/{notification_id}/history | Notification History
*DefaultApi* | [**get_notifications**](docs/DefaultApi.md#get_notifications) | **GET** /notifications | View notifications
*DefaultApi* | [**get_outcomes**](docs/DefaultApi.md#get_outcomes) | **GET** /apps/{app_id}/outcomes | View Outcomes
*DefaultApi* | [**get_segments**](docs/DefaultApi.md#get_segments) | **GET** /apps/{app_id}/segments | Get Segments
*DefaultApi* | [**get_user**](docs/DefaultApi.md#get_user) | **GET** /apps/{app_id}/users/by/{alias_label}/{alias_id} | 
*DefaultApi* | [**transfer_subscription**](docs/DefaultApi.md#transfer_subscription) | **PATCH** /apps/{app_id}/subscriptions/{subscription_id}/owner | 
*DefaultApi* | [**unsubscribe_email_with_token**](docs/DefaultApi.md#unsubscribe_email_with_token) | **POST** /apps/{app_id}/notifications/{notification_id}/unsubscribe | Unsubscribe with token
*DefaultApi* | [**update_app**](docs/DefaultApi.md#update_app) | **PUT** /apps/{app_id} | Update an app
*DefaultApi* | [**update_live_activity**](docs/DefaultApi.md#update_live_activity) | **POST** /apps/{app_id}/live_activities/{activity_id}/notifications | Update a Live Activity via Push
*DefaultApi* | [**update_subscription**](docs/DefaultApi.md#update_subscription) | **PATCH** /apps/{app_id}/subscriptions/{subscription_id} | 
*DefaultApi* | [**update_user**](docs/DefaultApi.md#update_user) | **PATCH** /apps/{app_id}/users/by/{alias_label}/{alias_id} | 


## Documentation For Models

 - [App](docs/App.md)
 - [Apps](docs/Apps.md)
 - [BasicNotification](docs/BasicNotification.md)
 - [BasicNotificationAllOf](docs/BasicNotificationAllOf.md)
 - [BasicNotificationAllOfAndroidBackgroundLayout](docs/BasicNotificationAllOfAndroidBackgroundLayout.md)
 - [Button](docs/Button.md)
 - [CreateNotificationSuccessResponse](docs/CreateNotificationSuccessResponse.md)
 - [CreateSegmentConflictResponse](docs/CreateSegmentConflictResponse.md)
 - [CreateSegmentSuccessResponse](docs/CreateSegmentSuccessResponse.md)
 - [CreateUserConflictResponse](docs/CreateUserConflictResponse.md)
 - [CreateUserConflictResponseErrorsInner](docs/CreateUserConflictResponseErrorsInner.md)
 - [CreateUserConflictResponseErrorsItemsMeta](docs/CreateUserConflictResponseErrorsItemsMeta.md)
 - [DeliveryData](docs/DeliveryData.md)
 - [ExportEventsSuccessResponse](docs/ExportEventsSuccessResponse.md)
 - [ExportSubscriptionsRequestBody](docs/ExportSubscriptionsRequestBody.md)
 - [ExportSubscriptionsSuccessResponse](docs/ExportSubscriptionsSuccessResponse.md)
 - [Filter](docs/Filter.md)
 - [FilterExpression](docs/FilterExpression.md)
 - [GenericError](docs/GenericError.md)
 - [GenericSuccessBoolResponse](docs/GenericSuccessBoolResponse.md)
 - [GetNotificationHistoryRequestBody](docs/GetNotificationHistoryRequestBody.md)
 - [GetSegmentsSuccessResponse](docs/GetSegmentsSuccessResponse.md)
 - [IdentityObject](docs/IdentityObject.md)
 - [LanguageStringMap](docs/LanguageStringMap.md)
 - [Notification](docs/Notification.md)
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
 - [PropertiesBody](docs/PropertiesBody.md)
 - [PropertiesDeltas](docs/PropertiesDeltas.md)
 - [PropertiesObject](docs/PropertiesObject.md)
 - [Purchase](docs/Purchase.md)
 - [RateLimitError](docs/RateLimitError.md)
 - [Segment](docs/Segment.md)
 - [SegmentData](docs/SegmentData.md)
 - [SegmentNotificationTarget](docs/SegmentNotificationTarget.md)
 - [Subscription](docs/Subscription.md)
 - [SubscriptionBody](docs/SubscriptionBody.md)
 - [SubscriptionNotificationTarget](docs/SubscriptionNotificationTarget.md)
 - [TransferSubscriptionRequestBody](docs/TransferSubscriptionRequestBody.md)
 - [UpdateLiveActivityRequest](docs/UpdateLiveActivityRequest.md)
 - [UpdateLiveActivitySuccessResponse](docs/UpdateLiveActivitySuccessResponse.md)
 - [UpdateUserRequest](docs/UpdateUserRequest.md)
 - [User](docs/User.md)
 - [UserIdentityBody](docs/UserIdentityBody.md)
 - [WebButton](docs/WebButton.md)


## Author

devrel@onesignal.com


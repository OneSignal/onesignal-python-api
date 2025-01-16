# onesignal.DefaultApi

All URIs are relative to *https://api.onesignal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**begin_live_activity**](DefaultApi.md#begin_live_activity) | **POST** /apps/{app_id}/live_activities/{activity_id}/token | Start Live Activity
[**cancel_notification**](DefaultApi.md#cancel_notification) | **DELETE** /notifications/{notification_id} | Stop a scheduled or currently outgoing notification
[**create_app**](DefaultApi.md#create_app) | **POST** /apps | Create an app
[**create_notification**](DefaultApi.md#create_notification) | **POST** /notifications | Create notification
[**create_player**](DefaultApi.md#create_player) | **POST** /players | Add a device
[**create_segments**](DefaultApi.md#create_segments) | **POST** /apps/{app_id}/segments | Create Segments
[**create_subscription**](DefaultApi.md#create_subscription) | **POST** /apps/{app_id}/users/by/{alias_label}/{alias_id}/subscriptions | 
[**create_user**](DefaultApi.md#create_user) | **POST** /apps/{app_id}/users | 
[**delete_alias**](DefaultApi.md#delete_alias) | **DELETE** /apps/{app_id}/users/by/{alias_label}/{alias_id}/identity/{alias_label_to_delete} | 
[**delete_player**](DefaultApi.md#delete_player) | **DELETE** /players/{player_id} | Delete a user record
[**delete_segments**](DefaultApi.md#delete_segments) | **DELETE** /apps/{app_id}/segments/{segment_id} | Delete Segments
[**delete_subscription**](DefaultApi.md#delete_subscription) | **DELETE** /apps/{app_id}/subscriptions/{subscription_id} | 
[**delete_user**](DefaultApi.md#delete_user) | **DELETE** /apps/{app_id}/users/by/{alias_label}/{alias_id} | 
[**end_live_activity**](DefaultApi.md#end_live_activity) | **DELETE** /apps/{app_id}/live_activities/{activity_id}/token/{subscription_id} | Stop Live Activity
[**export_events**](DefaultApi.md#export_events) | **POST** /notifications/{notification_id}/export_events?app_id&#x3D;{app_id} | Export CSV of Events
[**export_players**](DefaultApi.md#export_players) | **POST** /players/csv_export?app_id&#x3D;{app_id} | Export CSV of Players
[**fetch_aliases**](DefaultApi.md#fetch_aliases) | **GET** /apps/{app_id}/subscriptions/{subscription_id}/user/identity | 
[**fetch_user**](DefaultApi.md#fetch_user) | **GET** /apps/{app_id}/users/by/{alias_label}/{alias_id} | 
[**fetch_user_identity**](DefaultApi.md#fetch_user_identity) | **GET** /apps/{app_id}/users/by/{alias_label}/{alias_id}/identity | 
[**get_app**](DefaultApi.md#get_app) | **GET** /apps/{app_id} | View an app
[**get_apps**](DefaultApi.md#get_apps) | **GET** /apps | View apps
[**get_eligible_iams**](DefaultApi.md#get_eligible_iams) | **GET** /apps/{app_id}/subscriptions/{subscription_id}/iams | 
[**get_notification**](DefaultApi.md#get_notification) | **GET** /notifications/{notification_id} | View notification
[**get_notification_history**](DefaultApi.md#get_notification_history) | **POST** /notifications/{notification_id}/history | Notification History
[**get_notifications**](DefaultApi.md#get_notifications) | **GET** /notifications | View notifications
[**get_outcomes**](DefaultApi.md#get_outcomes) | **GET** /apps/{app_id}/outcomes | View Outcomes
[**get_player**](DefaultApi.md#get_player) | **GET** /players/{player_id} | View device
[**get_players**](DefaultApi.md#get_players) | **GET** /players | View devices
[**identify_user_by_alias**](DefaultApi.md#identify_user_by_alias) | **PATCH** /apps/{app_id}/users/by/{alias_label}/{alias_id}/identity | 
[**identify_user_by_subscription_id**](DefaultApi.md#identify_user_by_subscription_id) | **PATCH** /apps/{app_id}/subscriptions/{subscription_id}/user/identity | 
[**transfer_subscription**](DefaultApi.md#transfer_subscription) | **PATCH** /apps/{app_id}/subscriptions/{subscription_id}/owner | 
[**update_app**](DefaultApi.md#update_app) | **PUT** /apps/{app_id} | Update an app
[**update_live_activity**](DefaultApi.md#update_live_activity) | **POST** /apps/{app_id}/live_activities/{activity_id}/notifications | Update a Live Activity via Push
[**update_player**](DefaultApi.md#update_player) | **PUT** /players/{player_id} | Edit device
[**update_player_tags**](DefaultApi.md#update_player_tags) | **PUT** /apps/{app_id}/users/{external_user_id} | Edit tags with external user id
[**update_subscription**](DefaultApi.md#update_subscription) | **PATCH** /apps/{app_id}/subscriptions/{subscription_id} | 
[**update_user**](DefaultApi.md#update_user) | **PATCH** /apps/{app_id}/users/by/{alias_label}/{alias_id} | 


# **begin_live_activity**
> begin_live_activity(app_id, activity_id, begin_live_activity_request)

Start Live Activity

Starts a Live Activity

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from onesignal.model.begin_live_activity_request import BeginLiveActivityRequest
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" # The OneSignal App ID for your app.  Available in Keys & IDs. 
    activity_id = "activity_id_example" # Live Activity record ID 
    begin_live_activity_request = BeginLiveActivityRequest(
        push_token="push_token_example",
        subscription_id="subscription_id_example",
    ) 

    # example passing only required values which don't have defaults set
    try:
        # Start Live Activity
        api_instance.begin_live_activity(app_id, activity_id, begin_live_activity_request)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->begin_live_activity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The OneSignal App ID for your app.  Available in Keys &amp; IDs. |
 **activity_id** | **str**| Live Activity record ID |
 **begin_live_activity_request** | [**BeginLiveActivityRequest**](BeginLiveActivityRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_notification**
> CancelNotificationSuccessResponse cancel_notification(app_id, notification_id)

Stop a scheduled or currently outgoing notification

Used to stop a scheduled or currently outgoing notification

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from onesignal.model.cancel_notification_success_response import CancelNotificationSuccessResponse
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    notification_id = "notification_id_example" 

    # example passing only required values which don't have defaults set
    try:
        # Stop a scheduled or currently outgoing notification
        api_response = api_instance.cancel_notification(app_id, notification_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->cancel_notification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **notification_id** | **str**|  |

### Return type

[**CancelNotificationSuccessResponse**](CancelNotificationSuccessResponse.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app**
> App create_app(app)

Create an app

Creates a new OneSignal app

### Example

* Bearer Authentication (user_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.app import App
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app = App(
        name="name_example",
        android_gcm_sender_id="android_gcm_sender_id_example",
        gcm_key="gcm_key_example",
        chrome_web_origin="chrome_web_origin_example",
        chrome_key="chrome_key_example",
        chrome_web_default_notification_icon="chrome_web_default_notification_icon_example",
        chrome_web_sub_domain="chrome_web_sub_domain_example",
        apns_env="sandbox",
        apns_p12="apns_p12_example",
        apns_p12_password="apns_p12_password_example",
        safari_apns_p12="safari_apns_p12_example",
        safari_apns_p12_password="safari_apns_p12_password_example",
        apns_key_id="apns_key_id_example",
        apns_team_id="apns_team_id_example",
        apns_bundle_id="apns_bundle_id_example",
        apns_p8="apns_p8_example",
        safari_site_origin="safari_site_origin_example",
        safari_icon_256_256="safari_icon_256_256_example",
        site_name="site_name_example",
        organization_id="organization_id_example",
        additional_data_is_root_payload=True,
    ) 

    # example passing only required values which don't have defaults set
    try:
        # Create an app
        api_response = api_instance.create_app(app)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->create_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | [**App**](App.md)|  |

### Return type

[**App**](App.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_notification**
> CreateNotificationSuccessResponse create_notification(notification)

Create notification

Sends notifications to your users 

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from onesignal.model.notification import Notification
from onesignal.model.create_notification_success_response import CreateNotificationSuccessResponse
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    notification = Notification(None) 

    # example passing only required values which don't have defaults set
    try:
        # Create notification
        api_response = api_instance.create_notification(notification)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->create_notification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification** | [**Notification**](Notification.md)|  |

### Return type

[**CreateNotificationSuccessResponse**](CreateNotificationSuccessResponse.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK, invalid_player_ids, invalid_external_user_ids or No Subscribed Players If a message was successfully created, you will get a 200 response and an id for the notification. If the 200 response contains \&quot;invalid_player_ids\&quot; or \&quot;invalid_external_user_ids\&quot; this will mark devices that exist in the provided app_id but are no longer subscribed. If no id is returned, then a message was not created and the targeted User IDs do not exist under the provided app_id. Any User IDs sent in the request that do not exist under the specified app_id will be ignored.  |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_player**
> CreatePlayerSuccessResponse create_player(player)

Add a device

Register a new device to one of your OneSignal apps &#x1F6A7; Don't use this This API endpoint is designed to be used from our open source Mobile and Web Push SDKs. It is not designed for developers to use it directly, unless instructed to do so by OneSignal support. If you use this method instead of our SDKs, many OneSignal features such as conversion tracking, timezone tracking, language detection, and rich-push won't work out of the box. It will also make it harder to identify possible setup issues. This method is used to register a new device with OneSignal. If a device is already registered with the specified identifier, then this will update the existing device record instead of creating a new one. The returned player is a player / user ID. Use the returned ID to send push notifications to this specific user later, or to include this player when sending to a set of users. &#x1F6A7; iOS Must set test_type to 1 when building your iOS app as development. Omit this field in your production app builds. 

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.player import Player
from onesignal.model.create_player_success_response import CreatePlayerSuccessResponse
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    player = Player(
        app_id="app_id_example",
        device_type=1,
        external_user_id="external_user_id_example",
        external_user_id_auth_hash="external_user_id_auth_hash_example",
        email_auth_hash="email_auth_hash_example",
        identifier="identifier_example",
        language="language_example",
        timezone=1,
        game_version="game_version_example",
        device_model="device_model_example",
        device_os="device_os_example",
        ad_id="ad_id_example",
        sdk="sdk_example",
        session_count=1,
        tags={},
        amount_spent=3.14,
        created_at=1,
        playtime=1,
        badge_count=1,
        last_active=1,
        notification_types=1,
        test_type=1,
        long=3.14,
        lat=3.14,
        country="country_example",
    ) 

    # example passing only required values which don't have defaults set
    try:
        # Add a device
        api_response = api_instance.create_player(player)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->create_player: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player** | [**Player**](Player.md)|  |

### Return type

[**CreatePlayerSuccessResponse**](CreatePlayerSuccessResponse.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_segments**
> CreateSegmentSuccessResponse create_segments(app_id)

Create Segments

Create segments visible and usable in the dashboard and API - Required: OneSignal Paid Plan The Create Segment method is used when you want your server to programmatically create a segment instead of using the OneSignal Dashboard UI. Just like creating Segments from the dashboard you can pass in filters with multiple \"AND\" or \"OR\" operator's. &#x1F6A7; Does Not Update Segments This endpoint will only create segments, it does not edit or update currently created Segments. You will need to use the Delete Segments endpoint and re-create it with this endpoint to edit. 

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.create_segment_success_response import CreateSegmentSuccessResponse
from onesignal.model.create_segment_conflict_response import CreateSegmentConflictResponse
from onesignal.model.segment import Segment
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" # The OneSignal App ID for your app.  Available in Keys & IDs. 
    segment = Segment(
        id="id_example",
        name="name_example",
        filters=[
            FilterExpressions(None),
        ],
    ) 

    # example passing only required values which don't have defaults set
    try:
        # Create Segments
        api_response = api_instance.create_segments(app_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->create_segments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Segments
        api_response = api_instance.create_segments(app_id, segment=segment)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->create_segments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The OneSignal App ID for your app.  Available in Keys &amp; IDs. |
 **segment** | [**Segment**](Segment.md)|  | [optional]

### Return type

[**CreateSegmentSuccessResponse**](CreateSegmentSuccessResponse.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription**
> InlineResponse201 create_subscription(app_id, alias_label, alias_id, create_subscription_request_body)



Creates a new Subscription under the User provided. Useful to add email addresses and SMS numbers to the User.

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.inline_response201 import InlineResponse201
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from onesignal.model.create_subscription_request_body import CreateSubscriptionRequestBody
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    alias_label = "alias_label_example" 
    alias_id = "alias_id_example" 
    create_subscription_request_body = CreateSubscriptionRequestBody(
        subscription=SubscriptionObject(
            id="id_example",
            type="iOSPush",
            token="token_example",
            enabled=True,
            notification_types=3.14,
            session_time=3.14,
            session_count=3.14,
            sdk="sdk_example",
            device_model="device_model_example",
            device_os="device_os_example",
            rooted=True,
            test_type=3.14,
            app_version="app_version_example",
            net_type=3.14,
            carrier="carrier_example",
            web_auth="web_auth_example",
            web_p256="web_p256_example",
        ),
        retain_previous_owner=True,
    ) 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_subscription(app_id, alias_label, alias_id, create_subscription_request_body)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->create_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **alias_label** | **str**|  |
 **alias_id** | **str**|  |
 **create_subscription_request_body** | [**CreateSubscriptionRequestBody**](CreateSubscriptionRequestBody.md)|  |

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**202** | ACCEPTED |  -  |
**400** | Bad Request |  -  |
**409** | Operation is not permitted due to user having the maximum number of subscriptions assigned |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> User create_user(app_id, user)



Creates a User, optionally Subscriptions owned by the User as well as Aliases. Aliases provided in the payload will be used to look up an existing User.

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.user import User
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from onesignal.model.create_user_conflict_response import CreateUserConflictResponse
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    user = User(
        properties=PropertiesObject(
            tags={},
            language="language_example",
            timezone_id="timezone_id_example",
            lat=3.14,
            long=3.14,
            country="country_example",
            first_active=3.14,
            last_active=3.14,
            amount_spent=3.14,
            purchases=[
                Purchase(
                    sku="sku_example",
                    amount="amount_example",
                    iso="iso_example",
                    count=3.14,
                ),
            ],
            ip="ip_example",
        ),
        identity=IdentityObject(),
        subscriptions=[
            SubscriptionObject(
                id="id_example",
                type="iOSPush",
                token="token_example",
                enabled=True,
                notification_types=3.14,
                session_time=3.14,
                session_count=3.14,
                sdk="sdk_example",
                device_model="device_model_example",
                device_os="device_os_example",
                rooted=True,
                test_type=3.14,
                app_version="app_version_example",
                net_type=3.14,
                carrier="carrier_example",
                web_auth="web_auth_example",
                web_p256="web_p256_example",
            ),
        ],
        subscription_options=UserSubscriptionOptions(
            retain_previous_owner=True,
        ),
    ) 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_user(app_id, user)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->create_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **user** | [**User**](User.md)|  |

### Return type

[**User**](User.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CREATED |  -  |
**201** | CREATED |  -  |
**202** | ACCEPTED |  -  |
**400** | Bad Request |  -  |
**409** | Multiple User Identity Conflict |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alias**
> InlineResponse200 delete_alias(app_id, alias_label, alias_id, alias_label_to_delete)



Deletes an alias by alias label

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from onesignal.model.inline_response200 import InlineResponse200
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    alias_label = "alias_label_example" 
    alias_id = "alias_id_example" 
    alias_label_to_delete = "alias_label_to_delete_example" 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_alias(app_id, alias_label, alias_id, alias_label_to_delete)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->delete_alias: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **alias_label** | **str**|  |
 **alias_id** | **str**|  |
 **alias_label_to_delete** | **str**|  |

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_player**
> DeletePlayerSuccessResponse delete_player(app_id, player_id)

Delete a user record

Delete player - Required: Used to delete a single, specific Player ID record from a specific OneSignal app. 

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from onesignal.model.delete_player_not_found_response import DeletePlayerNotFoundResponse
from onesignal.model.delete_player_success_response import DeletePlayerSuccessResponse
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" # The OneSignal App ID for your app.  Available in Keys & IDs. 
    player_id = "player_id_example" # The OneSignal player_id 

    # example passing only required values which don't have defaults set
    try:
        # Delete a user record
        api_response = api_instance.delete_player(app_id, player_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->delete_player: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The OneSignal App ID for your app.  Available in Keys &amp; IDs. |
 **player_id** | **str**| The OneSignal player_id |

### Return type

[**DeletePlayerSuccessResponse**](DeletePlayerSuccessResponse.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_segments**
> DeleteSegmentSuccessResponse delete_segments(app_id, segment_id)

Delete Segments

Delete segments (not user devices) - Required: OneSignal Paid Plan You can delete a segment under your app by calling this API. You must provide an API key in the Authorization header that has admin access on the app. The segment_id can be found in the URL of the segment when viewing it in the dashboard. 

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.delete_segment_success_response import DeleteSegmentSuccessResponse
from onesignal.model.generic_error import GenericError
from onesignal.model.delete_segment_not_found_response import DeleteSegmentNotFoundResponse
from onesignal.model.rate_limiter_error import RateLimiterError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" # The OneSignal App ID for your app.  Available in Keys & IDs. 
    segment_id = "segment_id_example" # The segment_id can be found in the URL of the segment when viewing it in the dashboard. 

    # example passing only required values which don't have defaults set
    try:
        # Delete Segments
        api_response = api_instance.delete_segments(app_id, segment_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->delete_segments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The OneSignal App ID for your app.  Available in Keys &amp; IDs. |
 **segment_id** | **str**| The segment_id can be found in the URL of the segment when viewing it in the dashboard. |

### Return type

[**DeleteSegmentSuccessResponse**](DeleteSegmentSuccessResponse.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> delete_subscription(app_id, subscription_id)



Deletes the Subscription.

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    subscription_id = "subscription_id_example" 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_subscription(app_id, subscription_id)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->delete_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **subscription_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | ACCEPTED |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(app_id, alias_label, alias_id)



Removes the User identified by (:alias_label, :alias_id), and all Subscriptions and Aliases

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    alias_label = "alias_label_example" 
    alias_id = "alias_id_example" 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_user(app_id, alias_label, alias_id)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **alias_label** | **str**|  |
 **alias_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **end_live_activity**
> end_live_activity(app_id, activity_id, subscription_id)

Stop Live Activity

Stops a Live Activity

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" # The OneSignal App ID for your app.  Available in Keys & IDs. 
    activity_id = "activity_id_example" # Live Activity record ID 
    subscription_id = "subscription_id_example" # Subscription ID 

    # example passing only required values which don't have defaults set
    try:
        # Stop Live Activity
        api_instance.end_live_activity(app_id, activity_id, subscription_id)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->end_live_activity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The OneSignal App ID for your app.  Available in Keys &amp; IDs. |
 **activity_id** | **str**| Live Activity record ID |
 **subscription_id** | **str**| Subscription ID |

### Return type

void (empty response body)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_events**
> ExportEventsSuccessResponse export_events(notification_id, app_id)

Export CSV of Events

Generate a compressed CSV report of all of the events data for a notification. This will return a URL immediately upon success but it may take several minutes for the CSV to become available at that URL depending on the volume of data. Only one export can be in-progress per OneSignal account at any given time.

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.export_events_success_response import ExportEventsSuccessResponse
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    notification_id = "notification_id_example" # The ID of the notification to export events from. 
    app_id = "app_id_example" # The ID of the app that the notification belongs to. 

    # example passing only required values which don't have defaults set
    try:
        # Export CSV of Events
        api_response = api_instance.export_events(notification_id, app_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->export_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| The ID of the notification to export events from. |
 **app_id** | **str**| The ID of the app that the notification belongs to. |

### Return type

[**ExportEventsSuccessResponse**](ExportEventsSuccessResponse.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_players**
> ExportPlayersSuccessResponse export_players(app_id)

Export CSV of Players

Generate a compressed CSV export of all of your current user data This method can be used to generate a compressed CSV export of all of your current user data. It is a much faster alternative than retrieving this data using the /players API endpoint. The file will be compressed using GZip. The file may take several minutes to generate depending on the number of users in your app. The URL generated will be available for 3 days and includes random v4 uuid as part of the resource name to be unguessable. &#x1F6A7; 403 Error Responses          You can test if it is complete by making a GET request to the csv_file_url value. This file may take time to generate depending on how many device records are being pulled. If the file is not ready, a 403 error will be returned. Otherwise the file itself will be returned. &#x1F6A7; Requires Authentication Key Requires your OneSignal App's REST API Key, available in Keys & IDs. &#x1F6A7; Concurrent Exports Only one concurrent export is allowed per OneSignal account. Please ensure you have successfully downloaded the .csv.gz file before exporting another app. CSV File Format: - Default Columns:   | Field | Details |   | --- | --- |   | id | OneSignal Player Id |   | identifier | Push Token |   | session_count | Number of times they visited the app or site   | language | Device language code |   | timezone | Number of seconds away from UTC. Example: -28800 |   | game_version | Version of your mobile app gathered from Android Studio versionCode in your App/build.gradle and iOS uses kCFBundleVersionKey in Xcode. |   | device_os | Device Operating System Version. Example: 80 = Chrome 80, 9 = Android 9 |   | device_type | Device Operating System Type |   | device_model | Device Hardware String Code. Example: Mobile Web Subscribers will have `Linux armv` |   | ad_id | Based on the Google Advertising Id for Android, identifierForVendor for iOS. OptedOut means user turned off Advertising tracking on the device. |   | tags | Current OneSignal Data Tags on the device. |   | last_active | Date and time the user last opened the mobile app or visited the site. |   | playtime | Total amount of time in seconds the user had the mobile app open. |   | amount_spent |  Mobile only - amount spent in USD on In-App Purchases. |    | created_at | Date and time the device record was created in OneSignal. Mobile - first time they opened the app with OneSignal SDK. Web - first time the user subscribed to the site. |   | invalid_identifier | t = unsubscribed, f = subscibed |   | badge_count | Current number of badges on the device | - Extra Columns:   | Field | Details |   | --- | --- |   | external_user_id | Your User Id set on the device |   | notification_types | Notification types |   | location | Location points (Latitude and Longitude) set on the device. |   | country | Country code |   | rooted | Android device rooted or not |   | ip | IP Address of the device if being tracked. See Handling Personal Data. |   | web_auth | Web Only authorization key. |   | web_p256 | Web Only p256 key. | 

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.export_players_success_response import ExportPlayersSuccessResponse
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from onesignal.model.export_players_request_body import ExportPlayersRequestBody
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" # The app ID that you want to export devices from 
    export_players_request_body = ExportPlayersRequestBody(
        extra_fields=[
            "extra_fields_example",
        ],
        last_active_since="last_active_since_example",
        segment_name="segment_name_example",
    ) 

    # example passing only required values which don't have defaults set
    try:
        # Export CSV of Players
        api_response = api_instance.export_players(app_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->export_players: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export CSV of Players
        api_response = api_instance.export_players(app_id, export_players_request_body=export_players_request_body)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->export_players: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID that you want to export devices from |
 **export_players_request_body** | [**ExportPlayersRequestBody**](ExportPlayersRequestBody.md)|  | [optional]

### Return type

[**ExportPlayersSuccessResponse**](ExportPlayersSuccessResponse.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_aliases**
> UserIdentityResponse fetch_aliases(app_id, subscription_id)



Lists all Aliases for the User identified by :subscription_id.

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.generic_error import GenericError
from onesignal.model.user_identity_response import UserIdentityResponse
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    subscription_id = "subscription_id_example" 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_aliases(app_id, subscription_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->fetch_aliases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **subscription_id** | **str**|  |

### Return type

[**UserIdentityResponse**](UserIdentityResponse.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user**
> User fetch_user(app_id, alias_label, alias_id)



Returns the User’s properties, Aliases, and Subscriptions.

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.user import User
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    alias_label = "alias_label_example" 
    alias_id = "alias_id_example" 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_user(app_id, alias_label, alias_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->fetch_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **alias_label** | **str**|  |
 **alias_id** | **str**|  |

### Return type

[**User**](User.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_user_identity**
> InlineResponse200 fetch_user_identity(app_id, alias_label, alias_id)



Lists all Aliases for the User identified by (:alias_label, :alias_id).

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from onesignal.model.inline_response200 import InlineResponse200
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    alias_label = "alias_label_example" 
    alias_id = "alias_id_example" 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_user_identity(app_id, alias_label, alias_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->fetch_user_identity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **alias_label** | **str**|  |
 **alias_id** | **str**|  |

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app**
> App get_app(app_id)

View an app

View the details of a single OneSignal app

### Example

* Bearer Authentication (user_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.app import App
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" # An app id 

    # example passing only required values which don't have defaults set
    try:
        # View an app
        api_response = api_instance.get_app(app_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->get_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| An app id |

### Return type

[**App**](App.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apps**
> Apps get_apps()

View apps

View the details of all of your current OneSignal apps

### Example

* Bearer Authentication (user_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.apps import Apps
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # View apps
        api_response = api_instance.get_apps()
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->get_apps: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Apps**](Apps.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_eligible_iams**
> InlineResponse2003 get_eligible_iams(app_id, subscription_id)



Manifest of In-App Messages the Subscription is eligible to display by the SDK.

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.inline_response2003 import InlineResponse2003
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    subscription_id = "subscription_id_example" 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_eligible_iams(app_id, subscription_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->get_eligible_iams: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **subscription_id** | **str**|  |

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification**
> NotificationWithMeta get_notification(app_id, notification_id)

View notification

View the details of a single notification and outcomes associated with it

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from onesignal.model.notification_with_meta import NotificationWithMeta
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    notification_id = "notification_id_example" 

    # example passing only required values which don't have defaults set
    try:
        # View notification
        api_response = api_instance.get_notification(app_id, notification_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->get_notification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **notification_id** | **str**|  |

### Return type

[**NotificationWithMeta**](NotificationWithMeta.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_history**
> NotificationHistorySuccessResponse get_notification_history(notification_id, get_notification_request_body)

Notification History

-> View the devices sent a message - OneSignal Paid Plan Required This method will return all devices that were sent the given notification_id of an Email or Push Notification if used within 7 days of the date sent. After 7 days of the sending date, the message history data will be unavailable. After a successful response is received, the destination url may be polled until the file becomes available. Most exports are done in ~1-3 minutes, so setting a poll interval of 10 seconds should be adequate. For use cases that are not meant to be consumed by a script, an email will be sent to the supplied email address. &#x1F6A7; Requirements A OneSignal Paid Plan. Turn on Send History via OneSignal API in Settings -> Analytics. Cannot get data before this was turned on. Must be called within 7 days after sending the message. Messages targeting under 1000 recipients will not have \"sent\" events recorded, but will show \"clicked\" events. Requires your OneSignal App's REST API Key, available in Keys & IDs.

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.notification_history_success_response import NotificationHistorySuccessResponse
from onesignal.model.get_notification_request_body import GetNotificationRequestBody
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    notification_id = "notification_id_example" # The \"id\" of the message found in the Notification object 
    get_notification_request_body = GetNotificationRequestBody(
        events="sent",
        email="email_example",
        app_id="app_id_example",
    ) 

    # example passing only required values which don't have defaults set
    try:
        # Notification History
        api_response = api_instance.get_notification_history(notification_id, get_notification_request_body)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->get_notification_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| The \&quot;id\&quot; of the message found in the Notification object |
 **get_notification_request_body** | [**GetNotificationRequestBody**](GetNotificationRequestBody.md)|  |

### Return type

[**NotificationHistorySuccessResponse**](NotificationHistorySuccessResponse.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications**
> NotificationSlice get_notifications(app_id)

View notifications

View the details of multiple notifications

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.notification_slice import NotificationSlice
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" # The app ID that you want to view notifications from 
    limit = 1  # How many notifications to return.  Max is 50.  Default is 50. (optional) 
    offset = 1  # Page offset.  Default is 0.  Results are sorted by queued_at in descending order.  queued_at is a representation of the time that the notification was queued at. (optional) 
    kind = 0  # Kind of notifications returned:   * unset - All notification types (default)   * `0` - Dashboard only   * `1` - API only   * `3` - Automated only  (optional) 

    # example passing only required values which don't have defaults set
    try:
        # View notifications
        api_response = api_instance.get_notifications(app_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->get_notifications: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View notifications
        api_response = api_instance.get_notifications(app_id, limit=limit, offset=offset, kind=kind)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->get_notifications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID that you want to view notifications from |
 **limit** | **int**| How many notifications to return.  Max is 50.  Default is 50. | [optional]
 **offset** | **int**| Page offset.  Default is 0.  Results are sorted by queued_at in descending order.  queued_at is a representation of the time that the notification was queued at. | [optional]
 **kind** | **int**| Kind of notifications returned:   * unset - All notification types (default)   * &#x60;0&#x60; - Dashboard only   * &#x60;1&#x60; - API only   * &#x60;3&#x60; - Automated only  | [optional]

### Return type

[**NotificationSlice**](NotificationSlice.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outcomes**
> OutcomesData get_outcomes(app_id, outcome_names)

View Outcomes

View the details of all the outcomes associated with your app  &#x1F6A7; Requires Authentication Key Requires your OneSignal App's REST API Key, available in Keys & IDs.  &#x1F6A7; Outcome Data Limitations Outcomes are only accessible for around 30 days before deleted from our servers. You will need to export this data every month if you want to keep it. 

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.outcomes_data import OutcomesData
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" # The OneSignal App ID for your app.  Available in Keys & IDs. 
    outcome_names = "outcome_names_example" # Required Comma-separated list of names and the value (sum/count) for the returned outcome data. Note: Clicks only support count aggregation. For out-of-the-box OneSignal outcomes such as click and session duration, please use the \"os\" prefix with two underscores. For other outcomes, please use the name specified by the user. Example:os__session_duration.count,os__click.count,CustomOutcomeName.sum  
    outcome_names2 = "outcome_names[]_example"  # Optional If outcome names contain any commas, then please specify only one value at a time. Example: outcome_names[]=os__click.count&outcome_names[]=Sales, Purchase.count where \"Sales, Purchase\" is the custom outcomes with a comma in the name.  (optional) 
    outcome_time_range = "outcome_time_range_example"  # Optional Time range for the returned data. The values can be 1h (for the last 1 hour data), 1d (for the last 1 day data), or 1mo (for the last 1 month data). Default is 1h if the parameter is omitted.  (optional) 
    outcome_platforms = "outcome_platforms_example"  # Optional Platform id. Refer device's platform ids for values. Example: outcome_platform=0 for iOS outcome_platform=7,8 for Safari and Firefox Default is data from all platforms if the parameter is omitted.  (optional) 
    outcome_attribution = "outcome_attribution_example"  # Optional Attribution type for the outcomes. The values can be direct or influenced or unattributed. Example: outcome_attribution=direct Default is total (returns direct+influenced+unattributed) if the parameter is omitted.  (optional) 

    # example passing only required values which don't have defaults set
    try:
        # View Outcomes
        api_response = api_instance.get_outcomes(app_id, outcome_names)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->get_outcomes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View Outcomes
        api_response = api_instance.get_outcomes(app_id, outcome_names, outcome_names2=outcome_names2, outcome_time_range=outcome_time_range, outcome_platforms=outcome_platforms, outcome_attribution=outcome_attribution)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->get_outcomes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The OneSignal App ID for your app.  Available in Keys &amp; IDs. |
 **outcome_names** | **str**| Required Comma-separated list of names and the value (sum/count) for the returned outcome data. Note: Clicks only support count aggregation. For out-of-the-box OneSignal outcomes such as click and session duration, please use the \&quot;os\&quot; prefix with two underscores. For other outcomes, please use the name specified by the user. Example:os__session_duration.count,os__click.count,CustomOutcomeName.sum  |
 **outcome_names2** | **str**| Optional If outcome names contain any commas, then please specify only one value at a time. Example: outcome_names[]&#x3D;os__click.count&amp;outcome_names[]&#x3D;Sales, Purchase.count where \&quot;Sales, Purchase\&quot; is the custom outcomes with a comma in the name.  | [optional]
 **outcome_time_range** | **str**| Optional Time range for the returned data. The values can be 1h (for the last 1 hour data), 1d (for the last 1 day data), or 1mo (for the last 1 month data). Default is 1h if the parameter is omitted.  | [optional]
 **outcome_platforms** | **str**| Optional Platform id. Refer device&#39;s platform ids for values. Example: outcome_platform&#x3D;0 for iOS outcome_platform&#x3D;7,8 for Safari and Firefox Default is data from all platforms if the parameter is omitted.  | [optional]
 **outcome_attribution** | **str**| Optional Attribution type for the outcomes. The values can be direct or influenced or unattributed. Example: outcome_attribution&#x3D;direct Default is total (returns direct+influenced+unattributed) if the parameter is omitted.  | [optional]

### Return type

[**OutcomesData**](OutcomesData.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player**
> Player get_player(app_id, player_id)

View device

View the details of an existing device in one of your OneSignal apps

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.player import Player
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" # Your app_id for this device 
    player_id = "player_id_example" # Player's OneSignal ID 
    email_auth_hash = "email_auth_hash_example"  # Email - Only required if you have enabled Identity Verification and device_type is email (11). (optional) 

    # example passing only required values which don't have defaults set
    try:
        # View device
        api_response = api_instance.get_player(app_id, player_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->get_player: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View device
        api_response = api_instance.get_player(app_id, player_id, email_auth_hash=email_auth_hash)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->get_player: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Your app_id for this device |
 **player_id** | **str**| Player&#39;s OneSignal ID |
 **email_auth_hash** | **str**| Email - Only required if you have enabled Identity Verification and device_type is email (11). | [optional]

### Return type

[**Player**](Player.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_players**
> PlayerSlice get_players(app_id)

View devices

View the details of multiple devices in one of your OneSignal apps Unavailable for Apps Over 80,000 Users For performance reasons, this method is not available for larger apps. Larger apps should use the CSV export API endpoint, which is much more performant. 

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from onesignal.model.player_slice import PlayerSlice
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" # The app ID that you want to view players from 
    limit = 1  # How many devices to return. Max is 300. Default is 300 (optional) 
    offset = 1  # Result offset. Default is 0. Results are sorted by id; (optional) 

    # example passing only required values which don't have defaults set
    try:
        # View devices
        api_response = api_instance.get_players(app_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->get_players: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View devices
        api_response = api_instance.get_players(app_id, limit=limit, offset=offset)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->get_players: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID that you want to view players from |
 **limit** | **int**| How many devices to return. Max is 300. Default is 300 | [optional]
 **offset** | **int**| Result offset. Default is 0. Results are sorted by id; | [optional]

### Return type

[**PlayerSlice**](PlayerSlice.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identify_user_by_alias**
> InlineResponse200 identify_user_by_alias(app_id, alias_label, alias_id, user_identity_request_body)



Upserts one or more Aliases to an existing User identified by (:alias_label, :alias_id).

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.user_identity_request_body import UserIdentityRequestBody
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from onesignal.model.inline_response200 import InlineResponse200
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    alias_label = "alias_label_example" 
    alias_id = "alias_id_example" 
    user_identity_request_body = UserIdentityRequestBody(
        identity=IdentityObject(),
    ) 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.identify_user_by_alias(app_id, alias_label, alias_id, user_identity_request_body)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->identify_user_by_alias: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **alias_label** | **str**|  |
 **alias_id** | **str**|  |
 **user_identity_request_body** | [**UserIdentityRequestBody**](UserIdentityRequestBody.md)|  |

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identify_user_by_subscription_id**
> UserIdentityResponse identify_user_by_subscription_id(app_id, subscription_id, user_identity_request_body)



Upserts one or more Aliases for the User identified by :subscription_id.

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.user_identity_request_body import UserIdentityRequestBody
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from onesignal.model.user_identity_response import UserIdentityResponse
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    subscription_id = "subscription_id_example" 
    user_identity_request_body = UserIdentityRequestBody(
        identity=IdentityObject(),
    ) 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.identify_user_by_subscription_id(app_id, subscription_id, user_identity_request_body)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->identify_user_by_subscription_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **subscription_id** | **str**|  |
 **user_identity_request_body** | [**UserIdentityRequestBody**](UserIdentityRequestBody.md)|  |

### Return type

[**UserIdentityResponse**](UserIdentityResponse.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_subscription**
> UserIdentityResponse transfer_subscription(app_id, subscription_id, transfer_subscription_request_body)



Transfers this Subscription to the User identified by the identity in the payload.

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.transfer_subscription_request_body import TransferSubscriptionRequestBody
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from onesignal.model.user_identity_response import UserIdentityResponse
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    subscription_id = "subscription_id_example" 
    transfer_subscription_request_body = TransferSubscriptionRequestBody(
        identity=IdentityObject(),
    ) 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.transfer_subscription(app_id, subscription_id, transfer_subscription_request_body)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->transfer_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **subscription_id** | **str**|  |
 **transfer_subscription_request_body** | [**TransferSubscriptionRequestBody**](TransferSubscriptionRequestBody.md)|  |

### Return type

[**UserIdentityResponse**](UserIdentityResponse.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app**
> App update_app(app_id, app)

Update an app

Updates the name or configuration settings of an existing OneSignal app

### Example

* Bearer Authentication (user_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.app import App
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" # An app id 
    app = App(
        name="name_example",
        android_gcm_sender_id="android_gcm_sender_id_example",
        gcm_key="gcm_key_example",
        chrome_web_origin="chrome_web_origin_example",
        chrome_key="chrome_key_example",
        chrome_web_default_notification_icon="chrome_web_default_notification_icon_example",
        chrome_web_sub_domain="chrome_web_sub_domain_example",
        apns_env="sandbox",
        apns_p12="apns_p12_example",
        apns_p12_password="apns_p12_password_example",
        safari_apns_p12="safari_apns_p12_example",
        safari_apns_p12_password="safari_apns_p12_password_example",
        apns_key_id="apns_key_id_example",
        apns_team_id="apns_team_id_example",
        apns_bundle_id="apns_bundle_id_example",
        apns_p8="apns_p8_example",
        safari_site_origin="safari_site_origin_example",
        safari_icon_256_256="safari_icon_256_256_example",
        site_name="site_name_example",
        organization_id="organization_id_example",
        additional_data_is_root_payload=True,
    ) 

    # example passing only required values which don't have defaults set
    try:
        # Update an app
        api_response = api_instance.update_app(app_id, app)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->update_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| An app id |
 **app** | [**App**](App.md)|  |

### Return type

[**App**](App.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_live_activity**
> UpdateLiveActivitySuccessResponse update_live_activity(app_id, activity_id, update_live_activity_request)

Update a Live Activity via Push

Updates a specified live activity.

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.update_live_activity_request import UpdateLiveActivityRequest
from onesignal.model.update_live_activity_success_response import UpdateLiveActivitySuccessResponse
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" # The OneSignal App ID for your app.  Available in Keys & IDs. 
    activity_id = "activity_id_example" # Live Activity record ID 
    update_live_activity_request = UpdateLiveActivityRequest(
        name="headings",
        event="update",
        event_updates={},
        dismiss_at=3.14,
    ) 

    # example passing only required values which don't have defaults set
    try:
        # Update a Live Activity via Push
        api_response = api_instance.update_live_activity(app_id, activity_id, update_live_activity_request)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->update_live_activity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The OneSignal App ID for your app.  Available in Keys &amp; IDs. |
 **activity_id** | **str**| Live Activity record ID |
 **update_live_activity_request** | [**UpdateLiveActivityRequest**](UpdateLiveActivityRequest.md)|  |

### Return type

[**UpdateLiveActivitySuccessResponse**](UpdateLiveActivitySuccessResponse.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_player**
> UpdatePlayerSuccessResponse update_player(player_id, player)

Edit device

Update an existing device in one of your OneSignal apps

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.player import Player
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from onesignal.model.update_player_success_response import UpdatePlayerSuccessResponse
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    player_id = "player_id_example" # Player's OneSignal ID 
    player = Player(
        app_id="app_id_example",
        device_type=1,
        external_user_id="external_user_id_example",
        external_user_id_auth_hash="external_user_id_auth_hash_example",
        email_auth_hash="email_auth_hash_example",
        identifier="identifier_example",
        language="language_example",
        timezone=1,
        game_version="game_version_example",
        device_model="device_model_example",
        device_os="device_os_example",
        ad_id="ad_id_example",
        sdk="sdk_example",
        session_count=1,
        tags={},
        amount_spent=3.14,
        created_at=1,
        playtime=1,
        badge_count=1,
        last_active=1,
        notification_types=1,
        test_type=1,
        long=3.14,
        lat=3.14,
        country="country_example",
    ) 

    # example passing only required values which don't have defaults set
    try:
        # Edit device
        api_response = api_instance.update_player(player_id, player)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->update_player: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| Player&#39;s OneSignal ID |
 **player** | [**Player**](Player.md)|  |

### Return type

[**UpdatePlayerSuccessResponse**](UpdatePlayerSuccessResponse.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_player_tags**
> UpdatePlayerTagsSuccessResponse update_player_tags(app_id, external_user_id)

Edit tags with external user id

Update an existing device's tags in one of your OneSignal apps using the External User ID. Warning - Android SDK Data Synchronization Tags added through the Android SDK tagging methods may not update if using the API to change or update the same tag. For example, if you use SDK method sendTag(\"key\", \"value1\") then update the tag value to \"value2\" with this API endpoint. You will not be able to set the value back to \"value1\" through the SDK, you will need to change it to something different through the SDK to be reset. Recommendations if using this Endpoint on Android Mobile Apps: 1 - Do not use the same tag keys for SDK and API updates 2 - If you want to use the same key for both SDK and API updates, call the SDK getTags method first to update the device's tags. This is only applicable on the Android Mobile App SDKs. &#128216; Deleting Tags To delete a tag, include its key and set its value to blank. Omitting a key/value will not delete it. For example, if I wanted to delete two existing tags rank and category while simultaneously adding a new tag class, the tags JSON would look like the following: \"tags\": {    \"rank\": \"\",    \"category\": \"\",    \"class\": \"my_new_value\" } 

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from onesignal.model.update_player_tags_request_body import UpdatePlayerTagsRequestBody
from onesignal.model.update_player_tags_success_response import UpdatePlayerTagsSuccessResponse
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" # The OneSignal App ID the user record is found under. 
    external_user_id = "external_user_id_example" # The External User ID mapped to teh device record in OneSignal.  Must be actively set on the device to be updated. 
    update_player_tags_request_body = UpdatePlayerTagsRequestBody(
        tags={},
    ) 

    # example passing only required values which don't have defaults set
    try:
        # Edit tags with external user id
        api_response = api_instance.update_player_tags(app_id, external_user_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->update_player_tags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit tags with external user id
        api_response = api_instance.update_player_tags(app_id, external_user_id, update_player_tags_request_body=update_player_tags_request_body)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->update_player_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The OneSignal App ID the user record is found under. |
 **external_user_id** | **str**| The External User ID mapped to teh device record in OneSignal.  Must be actively set on the device to be updated. |
 **update_player_tags_request_body** | [**UpdatePlayerTagsRequestBody**](UpdatePlayerTagsRequestBody.md)|  | [optional]

### Return type

[**UpdatePlayerTagsSuccessResponse**](UpdatePlayerTagsSuccessResponse.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription**
> update_subscription(app_id, subscription_id, update_subscription_request_body)



Updates an existing Subscription’s properties.

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.update_subscription_request_body import UpdateSubscriptionRequestBody
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    subscription_id = "subscription_id_example" 
    update_subscription_request_body = UpdateSubscriptionRequestBody(
        subscription=SubscriptionObject(
            id="id_example",
            type="iOSPush",
            token="token_example",
            enabled=True,
            notification_types=3.14,
            session_time=3.14,
            session_count=3.14,
            sdk="sdk_example",
            device_model="device_model_example",
            device_os="device_os_example",
            rooted=True,
            test_type=3.14,
            app_version="app_version_example",
            net_type=3.14,
            carrier="carrier_example",
            web_auth="web_auth_example",
            web_p256="web_p256_example",
        ),
    ) 

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_subscription(app_id, subscription_id, update_subscription_request_body)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->update_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **subscription_id** | **str**|  |
 **update_subscription_request_body** | [**UpdateSubscriptionRequestBody**](UpdateSubscriptionRequestBody.md)|  |

### Return type

void (empty response body)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | ACCEPTED |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> InlineResponse202 update_user(app_id, alias_label, alias_id, update_user_request)



Updates an existing User’s properties.

### Example

* Bearer Authentication (app_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.update_user_request import UpdateUserRequest
from onesignal.model.inline_response202 import InlineResponse202
from onesignal.model.generic_error import GenericError
from onesignal.model.rate_limiter_error import RateLimiterError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    alias_label = "alias_label_example" 
    alias_id = "alias_id_example" 
    update_user_request = UpdateUserRequest(
        properties=PropertiesObject(
            tags={},
            language="language_example",
            timezone_id="timezone_id_example",
            lat=3.14,
            long=3.14,
            country="country_example",
            first_active=3.14,
            last_active=3.14,
            amount_spent=3.14,
            purchases=[
                Purchase(
                    sku="sku_example",
                    amount="amount_example",
                    iso="iso_example",
                    count=3.14,
                ),
            ],
            ip="ip_example",
        ),
        refresh_device_metadata=False,
        deltas=PropertiesDeltas(
            session_time=3.14,
            session_count=3.14,
            purchases=[
                Purchase(
                    sku="sku_example",
                    amount="amount_example",
                    iso="iso_example",
                    count=3.14,
                ),
            ],
        ),
    ) 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_user(app_id, alias_label, alias_id, update_user_request)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **alias_label** | **str**|  |
 **alias_id** | **str**|  |
 **update_user_request** | [**UpdateUserRequest**](UpdateUserRequest.md)|  |

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | ACCEPTED |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# onesignal.DefaultApi

All URIs are relative to *https://api.onesignal.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_notification**](DefaultApi.md#cancel_notification) | **DELETE** /notifications/{notification_id} | Stop a scheduled or currently outgoing notification
[**create_alias**](DefaultApi.md#create_alias) | **PATCH** /apps/{app_id}/users/by/{alias_label}/{alias_id}/identity | 
[**create_alias_by_subscription**](DefaultApi.md#create_alias_by_subscription) | **PATCH** /apps/{app_id}/subscriptions/{subscription_id}/user/identity | 
[**create_app**](DefaultApi.md#create_app) | **POST** /apps | Create an app
[**create_notification**](DefaultApi.md#create_notification) | **POST** /notifications | Create notification
[**create_segment**](DefaultApi.md#create_segment) | **POST** /apps/{app_id}/segments | Create Segment
[**create_subscription**](DefaultApi.md#create_subscription) | **POST** /apps/{app_id}/users/by/{alias_label}/{alias_id}/subscriptions | 
[**create_user**](DefaultApi.md#create_user) | **POST** /apps/{app_id}/users | 
[**delete_alias**](DefaultApi.md#delete_alias) | **DELETE** /apps/{app_id}/users/by/{alias_label}/{alias_id}/identity/{alias_label_to_delete} | 
[**delete_segment**](DefaultApi.md#delete_segment) | **DELETE** /apps/{app_id}/segments/{segment_id} | Delete Segment
[**delete_subscription**](DefaultApi.md#delete_subscription) | **DELETE** /apps/{app_id}/subscriptions/{subscription_id} | 
[**delete_user**](DefaultApi.md#delete_user) | **DELETE** /apps/{app_id}/users/by/{alias_label}/{alias_id} | 
[**export_events**](DefaultApi.md#export_events) | **POST** /notifications/{notification_id}/export_events?app_id&#x3D;{app_id} | Export CSV of Events
[**export_subscriptions**](DefaultApi.md#export_subscriptions) | **POST** /players/csv_export?app_id&#x3D;{app_id} | Export CSV of Subscriptions
[**get_aliases**](DefaultApi.md#get_aliases) | **GET** /apps/{app_id}/users/by/{alias_label}/{alias_id}/identity | 
[**get_aliases_by_subscription**](DefaultApi.md#get_aliases_by_subscription) | **GET** /apps/{app_id}/subscriptions/{subscription_id}/user/identity | 
[**get_app**](DefaultApi.md#get_app) | **GET** /apps/{app_id} | View an app
[**get_apps**](DefaultApi.md#get_apps) | **GET** /apps | View apps
[**get_notification**](DefaultApi.md#get_notification) | **GET** /notifications/{notification_id} | View notification
[**get_notification_history**](DefaultApi.md#get_notification_history) | **POST** /notifications/{notification_id}/history | Notification History
[**get_notifications**](DefaultApi.md#get_notifications) | **GET** /notifications | View notifications
[**get_outcomes**](DefaultApi.md#get_outcomes) | **GET** /apps/{app_id}/outcomes | View Outcomes
[**get_segments**](DefaultApi.md#get_segments) | **GET** /apps/{app_id}/segments | Get Segments
[**get_user**](DefaultApi.md#get_user) | **GET** /apps/{app_id}/users/by/{alias_label}/{alias_id} | 
[**transfer_subscription**](DefaultApi.md#transfer_subscription) | **PATCH** /apps/{app_id}/subscriptions/{subscription_id}/owner | 
[**unsubscribe_email_with_token**](DefaultApi.md#unsubscribe_email_with_token) | **POST** /apps/{app_id}/notifications/{notification_id}/unsubscribe | Unsubscribe with token
[**update_app**](DefaultApi.md#update_app) | **PUT** /apps/{app_id} | Update an app
[**update_live_activity**](DefaultApi.md#update_live_activity) | **POST** /apps/{app_id}/live_activities/{activity_id}/notifications | Update a Live Activity via Push
[**update_subscription**](DefaultApi.md#update_subscription) | **PATCH** /apps/{app_id}/subscriptions/{subscription_id} | 
[**update_user**](DefaultApi.md#update_user) | **PATCH** /apps/{app_id}/users/by/{alias_label}/{alias_id} | 


# **cancel_notification**
> GenericSuccessBoolResponse cancel_notification(app_id, notification_id)

Stop a scheduled or currently outgoing notification

Used to stop a scheduled or currently outgoing notification

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
from onesignal.model.generic_success_bool_response import GenericSuccessBoolResponse
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

[**GenericSuccessBoolResponse**](GenericSuccessBoolResponse.md)

### Authorization

[rest_api_key](../README.md#rest_api_key)

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

# **create_alias**
> UserIdentityBody create_alias(app_id, alias_label, alias_id, user_identity_body)



Upserts one or more Aliases to an existing User identified by (:alias_label, :alias_id).

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
from onesignal.model.user_identity_body import UserIdentityBody
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    alias_label = "alias_label_example" 
    alias_id = "alias_id_example" 
    user_identity_body = UserIdentityBody(
        identity=IdentityObject(
            key="key_example",
        ),
    ) 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_alias(app_id, alias_label, alias_id, user_identity_body)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->create_alias: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **alias_label** | **str**|  |
 **alias_id** | **str**|  |
 **user_identity_body** | [**UserIdentityBody**](UserIdentityBody.md)|  |

### Return type

[**UserIdentityBody**](UserIdentityBody.md)

### Authorization

[rest_api_key](../README.md#rest_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_alias_by_subscription**
> UserIdentityBody create_alias_by_subscription(app_id, subscription_id, user_identity_body)



Upserts one or more Aliases for the User identified by :subscription_id.

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
from onesignal.model.user_identity_body import UserIdentityBody
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    subscription_id = "subscription_id_example" 
    user_identity_body = UserIdentityBody(
        identity=IdentityObject(
            key="key_example",
        ),
    ) 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_alias_by_subscription(app_id, subscription_id, user_identity_body)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->create_alias_by_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **subscription_id** | **str**|  |
 **user_identity_body** | [**UserIdentityBody**](UserIdentityBody.md)|  |

### Return type

[**UserIdentityBody**](UserIdentityBody.md)

### Authorization

[rest_api_key](../README.md#rest_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app**
> App create_app(app)

Create an app

Creates a new OneSignal app

### Example

* Bearer Authentication (user_auth_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.app import App
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
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

[user_auth_key](../README.md#user_auth_key)

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

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
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

[rest_api_key](../README.md#rest_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK, invalid_aliases, or No Subscribed Players If a message was successfully created, you will get a 200 response and an id for the notification. If the 200 response contains \&quot;invalid_aliases\&quot; this will mark devices that exist in the provided app_id but are no longer subscribed. If no id is returned, then a message was not created and the targeted User IDs do not exist under the provided app_id. Any User IDs sent in the request that do not exist under the specified app_id will be ignored.  |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_segment**
> CreateSegmentSuccessResponse create_segment(app_id)

Create Segment

Create a segment visible and usable in the dashboard and API - Required: OneSignal Paid Plan The Create Segment method is used when you want your server to programmatically create a segment instead of using the OneSignal Dashboard UI. Just like creating Segments from the dashboard you can pass in filters with multiple \"AND\" or \"OR\" operator's. &#x1F6A7; Does Not Update Segments This endpoint will only create segments, it does not edit or update currently created Segments. You will need to use the Delete Segment endpoint and re-create it with this endpoint to edit. 

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.create_segment_success_response import CreateSegmentSuccessResponse
from onesignal.model.create_segment_conflict_response import CreateSegmentConflictResponse
from onesignal.model.segment import Segment
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
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
            FilterExpression(None),
        ],
    ) 

    # example passing only required values which don't have defaults set
    try:
        # Create Segment
        api_response = api_instance.create_segment(app_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->create_segment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Segment
        api_response = api_instance.create_segment(app_id, segment=segment)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->create_segment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The OneSignal App ID for your app.  Available in Keys &amp; IDs. |
 **segment** | [**Segment**](Segment.md)|  | [optional]

### Return type

[**CreateSegmentSuccessResponse**](CreateSegmentSuccessResponse.md)

### Authorization

[rest_api_key](../README.md#rest_api_key)

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
> SubscriptionBody create_subscription(app_id, alias_label, alias_id, subscription_body)



Creates a new Subscription under the User provided. Useful to add email addresses and SMS numbers to the User.

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
from onesignal.model.subscription_body import SubscriptionBody
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    alias_label = "alias_label_example" 
    alias_id = "alias_id_example" 
    subscription_body = SubscriptionBody(
        subscription=Subscription(
            id="id_example",
            type="iOSPush",
            token="token_example",
            enabled=True,
            notification_types=1,
            session_time=1,
            session_count=1,
            sdk="sdk_example",
            device_model="device_model_example",
            device_os="device_os_example",
            rooted=True,
            test_type=1,
            app_version="app_version_example",
            net_type=1,
            carrier="carrier_example",
            web_auth="web_auth_example",
            web_p256="web_p256_example",
        ),
    ) 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_subscription(app_id, alias_label, alias_id, subscription_body)
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
 **subscription_body** | [**SubscriptionBody**](SubscriptionBody.md)|  |

### Return type

[**SubscriptionBody**](SubscriptionBody.md)

### Authorization

[rest_api_key](../README.md#rest_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**202** | ACCEPTED |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**409** | Operation is not permitted due to user having the maximum number of subscriptions assigned |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> User create_user(app_id, user)



Creates a User, optionally Subscriptions owned by the User as well as Aliases. Aliases provided in the payload will be used to look up an existing User.

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.user import User
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
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
            first_active=1,
            last_active=1,
            amount_spent=3.14,
            purchases=[
                Purchase(
                    sku="sku_example",
                    amount="amount_example",
                    iso="iso_example",
                    count=1,
                ),
            ],
            ip="ip_example",
        ),
        identity=IdentityObject(
            key="key_example",
        ),
        subscriptions=[
            Subscription(
                id="id_example",
                type="iOSPush",
                token="token_example",
                enabled=True,
                notification_types=1,
                session_time=1,
                session_count=1,
                sdk="sdk_example",
                device_model="device_model_example",
                device_os="device_os_example",
                rooted=True,
                test_type=1,
                app_version="app_version_example",
                net_type=1,
                carrier="carrier_example",
                web_auth="web_auth_example",
                web_p256="web_p256_example",
            ),
        ],
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

[rest_api_key](../README.md#rest_api_key)

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
> UserIdentityBody delete_alias(app_id, alias_label, alias_id, alias_label_to_delete)



Deletes an alias by alias label

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
from onesignal.model.user_identity_body import UserIdentityBody
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

[**UserIdentityBody**](UserIdentityBody.md)

### Authorization

[rest_api_key](../README.md#rest_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_segment**
> GenericSuccessBoolResponse delete_segment(app_id, segment_id)

Delete Segment

Delete a segment (not user devices) - Required: OneSignal Paid Plan You can delete a segment under your app by calling this API. You must provide an API key in the Authorization header that has admin access on the app. The segment_id can be found in the URL of the segment when viewing it in the dashboard. 

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
from onesignal.model.generic_success_bool_response import GenericSuccessBoolResponse
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" # The OneSignal App ID for your app.  Available in Keys & IDs. 
    segment_id = "segment_id_example" # The segment_id can be found in the URL of the segment when viewing it in the dashboard. 

    # example passing only required values which don't have defaults set
    try:
        # Delete Segment
        api_response = api_instance.delete_segment(app_id, segment_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->delete_segment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The OneSignal App ID for your app.  Available in Keys &amp; IDs. |
 **segment_id** | **str**| The segment_id can be found in the URL of the segment when viewing it in the dashboard. |

### Return type

[**GenericSuccessBoolResponse**](GenericSuccessBoolResponse.md)

### Authorization

[rest_api_key](../README.md#rest_api_key)

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

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
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

[rest_api_key](../README.md#rest_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | ACCEPTED |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(app_id, alias_label, alias_id)



Removes the User identified by (:alias_label, :alias_id), and all Subscriptions and Aliases

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
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

[rest_api_key](../README.md#rest_api_key)

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

# **export_events**
> ExportEventsSuccessResponse export_events(notification_id, app_id)

Export CSV of Events

Generate a compressed CSV report of all of the events data for a notification. This will return a URL immediately upon success but it may take several minutes for the CSV to become available at that URL depending on the volume of data. Only one export can be in-progress per OneSignal account at any given time.

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.export_events_success_response import ExportEventsSuccessResponse
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
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

[rest_api_key](../README.md#rest_api_key)

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

# **export_subscriptions**
> ExportSubscriptionsSuccessResponse export_subscriptions(app_id)

Export CSV of Subscriptions

Generate a compressed CSV export of all of your current user data This method can be used to generate a compressed CSV export of all of your current user data. It is a much faster alternative than retrieving this data using the /players API endpoint. The file will be compressed using GZip. The file may take several minutes to generate depending on the number of users in your app. The URL generated will be available for 3 days and includes random v4 uuid as part of the resource name to be unguessable. &#x1F6A7; 403 Error Responses          You can test if it is complete by making a GET request to the csv_file_url value. This file may take time to generate depending on how many device records are being pulled. If the file is not ready, a 403 error will be returned. Otherwise the file itself will be returned. &#x1F6A7; Requires Authentication Key Requires your OneSignal App's REST API Key, available in Keys & IDs. &#x1F6A7; Concurrent Exports Only one concurrent export is allowed per OneSignal account. Please ensure you have successfully downloaded the .csv.gz file before exporting another app. CSV File Format: - Default Columns:   | Field | Details |   | --- | --- |   | id | OneSignal Player Id |   | identifier | Push Token |   | session_count | Number of times they visited the app or site   | language | Device language code |   | timezone | Number of seconds away from UTC. Example: -28800 |   | game_version | Version of your mobile app gathered from Android Studio versionCode in your App/build.gradle and iOS uses kCFBundleVersionKey in Xcode. |   | device_os | Device Operating System Version. Example: 80 = Chrome 80, 9 = Android 9 |   | device_type | Device Operating System Type |   | device_model | Device Hardware String Code. Example: Mobile Web Subscribers will have `Linux armv` |   | ad_id | Based on the Google Advertising Id for Android, identifierForVendor for iOS. OptedOut means user turned off Advertising tracking on the device. |   | tags | Current OneSignal Data Tags on the device. |   | last_active | Date and time the user last opened the mobile app or visited the site. |   | playtime | Total amount of time in seconds the user had the mobile app open. |   | amount_spent |  Mobile only - amount spent in USD on In-App Purchases. |    | created_at | Date and time the device record was created in OneSignal. Mobile - first time they opened the app with OneSignal SDK. Web - first time the user subscribed to the site. |   | invalid_identifier | t = unsubscribed, f = subscibed |   | badge_count | Current number of badges on the device | - Extra Columns:   | Field | Details |   | --- | --- |   | external_user_id | Your User Id set on the device |   | notification_types | Notification types |   | location | Location points (Latitude and Longitude) set on the device. |   | country | Country code |   | rooted | Android device rooted or not |   | ip | IP Address of the device if being tracked. See Handling Personal Data. |   | web_auth | Web Only authorization key. |   | web_p256 | Web Only p256 key. | 

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.export_subscriptions_success_response import ExportSubscriptionsSuccessResponse
from onesignal.model.export_subscriptions_request_body import ExportSubscriptionsRequestBody
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" # The app ID that you want to export devices from 
    export_subscriptions_request_body = ExportSubscriptionsRequestBody(
        extra_fields=[
            "extra_fields_example",
        ],
        last_active_since="last_active_since_example",
        segment_name="segment_name_example",
    ) 

    # example passing only required values which don't have defaults set
    try:
        # Export CSV of Subscriptions
        api_response = api_instance.export_subscriptions(app_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->export_subscriptions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export CSV of Subscriptions
        api_response = api_instance.export_subscriptions(app_id, export_subscriptions_request_body=export_subscriptions_request_body)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->export_subscriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID that you want to export devices from |
 **export_subscriptions_request_body** | [**ExportSubscriptionsRequestBody**](ExportSubscriptionsRequestBody.md)|  | [optional]

### Return type

[**ExportSubscriptionsSuccessResponse**](ExportSubscriptionsSuccessResponse.md)

### Authorization

[rest_api_key](../README.md#rest_api_key)

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

# **get_aliases**
> UserIdentityBody get_aliases(app_id, alias_label, alias_id)



Lists all Aliases for the User identified by (:alias_label, :alias_id).

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
from onesignal.model.user_identity_body import UserIdentityBody
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
        api_response = api_instance.get_aliases(app_id, alias_label, alias_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->get_aliases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **alias_label** | **str**|  |
 **alias_id** | **str**|  |

### Return type

[**UserIdentityBody**](UserIdentityBody.md)

### Authorization

[rest_api_key](../README.md#rest_api_key)

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

# **get_aliases_by_subscription**
> UserIdentityBody get_aliases_by_subscription(app_id, subscription_id)



Lists all Aliases for the User identified by :subscription_id.

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.generic_error import GenericError
from onesignal.model.user_identity_body import UserIdentityBody
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    subscription_id = "subscription_id_example" 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_aliases_by_subscription(app_id, subscription_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->get_aliases_by_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **subscription_id** | **str**|  |

### Return type

[**UserIdentityBody**](UserIdentityBody.md)

### Authorization

[rest_api_key](../README.md#rest_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app**
> App get_app(app_id)

View an app

View the details of a single OneSignal app

### Example

* Bearer Authentication (user_auth_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.app import App
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
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

[user_auth_key](../README.md#user_auth_key)

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

* Bearer Authentication (user_auth_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.apps import Apps
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
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

[user_auth_key](../README.md#user_auth_key)

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

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
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

[rest_api_key](../README.md#rest_api_key)

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

# **get_notification_history**
> NotificationHistorySuccessResponse get_notification_history(notification_id, get_notification_history_request_body)

Notification History

-> View the devices sent a message - OneSignal Paid Plan Required This method will return all devices that were sent the given notification_id of an Email or Push Notification if used within 7 days of the date sent. After 7 days of the sending date, the message history data will be unavailable. After a successful response is received, the destination url may be polled until the file becomes available. Most exports are done in ~1-3 minutes, so setting a poll interval of 10 seconds should be adequate. For use cases that are not meant to be consumed by a script, an email will be sent to the supplied email address. &#x1F6A7; Requirements A OneSignal Paid Plan. Turn on Send History via OneSignal API in Settings -> Analytics. Cannot get data before this was turned on. Must be called within 7 days after sending the message. Messages targeting under 1000 recipients will not have \"sent\" events recorded, but will show \"clicked\" events. Requires your OneSignal App's REST API Key, available in Keys & IDs.

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.notification_history_success_response import NotificationHistorySuccessResponse
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
from onesignal.model.get_notification_history_request_body import GetNotificationHistoryRequestBody
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    notification_id = "notification_id_example" # The \"id\" of the message found in the Notification object 
    get_notification_history_request_body = GetNotificationHistoryRequestBody(
        events="sent",
        email="email_example",
        app_id="app_id_example",
    ) 

    # example passing only required values which don't have defaults set
    try:
        # Notification History
        api_response = api_instance.get_notification_history(notification_id, get_notification_history_request_body)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->get_notification_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| The \&quot;id\&quot; of the message found in the Notification object |
 **get_notification_history_request_body** | [**GetNotificationHistoryRequestBody**](GetNotificationHistoryRequestBody.md)|  |

### Return type

[**NotificationHistorySuccessResponse**](NotificationHistorySuccessResponse.md)

### Authorization

[rest_api_key](../README.md#rest_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications**
> NotificationSlice get_notifications(app_id)

View notifications

View the details of multiple notifications

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.notification_slice import NotificationSlice
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
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

[rest_api_key](../README.md#rest_api_key)

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

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.outcomes_data import OutcomesData
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
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

[rest_api_key](../README.md#rest_api_key)

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

# **get_segments**
> GetSegmentsSuccessResponse get_segments(app_id)

Get Segments

Returns an array of segments from an app.

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.get_segments_success_response import GetSegmentsSuccessResponse
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" # The OneSignal App ID for your app.  Available in Keys & IDs. 
    offset = 1  # Segments are listed in ascending order of created_at date. offset will omit that number of segments from the beginning of the list. Eg offset 5, will remove the 5 earliest created Segments. (optional) 
    limit = 1  # The amount of Segments in the response. Maximum 300. (optional) 

    # example passing only required values which don't have defaults set
    try:
        # Get Segments
        api_response = api_instance.get_segments(app_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->get_segments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Segments
        api_response = api_instance.get_segments(app_id, offset=offset, limit=limit)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->get_segments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The OneSignal App ID for your app.  Available in Keys &amp; IDs. |
 **offset** | **int**| Segments are listed in ascending order of created_at date. offset will omit that number of segments from the beginning of the list. Eg offset 5, will remove the 5 earliest created Segments. | [optional]
 **limit** | **int**| The amount of Segments in the response. Maximum 300. | [optional]

### Return type

[**GetSegmentsSuccessResponse**](GetSegmentsSuccessResponse.md)

### Authorization

[rest_api_key](../README.md#rest_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(app_id, alias_label, alias_id)



Returns the User’s properties, Aliases, and Subscriptions.

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.user import User
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
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
        api_response = api_instance.get_user(app_id, alias_label, alias_id)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->get_user: %s\n" % e)
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

[rest_api_key](../README.md#rest_api_key)

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

# **transfer_subscription**
> UserIdentityBody transfer_subscription(app_id, subscription_id, transfer_subscription_request_body)



Transfers this Subscription to the User identified by the identity in the payload.

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.transfer_subscription_request_body import TransferSubscriptionRequestBody
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
from onesignal.model.user_identity_body import UserIdentityBody
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    subscription_id = "subscription_id_example" 
    transfer_subscription_request_body = TransferSubscriptionRequestBody(
        identity={
            "key": "key_example",
        },
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

[**UserIdentityBody**](UserIdentityBody.md)

### Authorization

[rest_api_key](../README.md#rest_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_email_with_token**
> GenericSuccessBoolResponse unsubscribe_email_with_token(app_id, notification_id, token)

Unsubscribe with token

Unsubscribe an email with a token when using your own custom email unsubscribe landing page

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
from onesignal.model.generic_success_bool_response import GenericSuccessBoolResponse
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" # The OneSignal App ID for your app.  Available in Keys & IDs. 
    notification_id = "notification_id_example" # The id of the message found in the creation notification POST response, View Notifications GET response, or URL within the Message Report. 
    token = "token_example" # The unsubscribe token that is generated via liquid syntax in {{subscription.unsubscribe_token}} when personalizing an email. 

    # example passing only required values which don't have defaults set
    try:
        # Unsubscribe with token
        api_response = api_instance.unsubscribe_email_with_token(app_id, notification_id, token)
        pprint(api_response)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->unsubscribe_email_with_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The OneSignal App ID for your app.  Available in Keys &amp; IDs. |
 **notification_id** | **str**| The id of the message found in the creation notification POST response, View Notifications GET response, or URL within the Message Report. |
 **token** | **str**| The unsubscribe token that is generated via liquid syntax in {{subscription.unsubscribe_token}} when personalizing an email. |

### Return type

[**GenericSuccessBoolResponse**](GenericSuccessBoolResponse.md)

### Authorization

[rest_api_key](../README.md#rest_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app**
> App update_app(app_id, app)

Update an app

Updates the name or configuration settings of an existing OneSignal app

### Example

* Bearer Authentication (user_auth_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.app import App
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
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

[user_auth_key](../README.md#user_auth_key)

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

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.update_live_activity_request import UpdateLiveActivityRequest
from onesignal.model.update_live_activity_success_response import UpdateLiveActivitySuccessResponse
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" # The OneSignal App ID for your app.  Available in Keys & IDs. 
    activity_id = "activity_id_example" # Live Activity record ID 
    update_live_activity_request = UpdateLiveActivityRequest(
        name="name_example",
        event="update",
        event_updates={},
        contents=LanguageStringMap(
            en="en_example",
            ar="ar_example",
            bs="bs_example",
            bg="bg_example",
            ca="ca_example",
            zh_hans="zh_hans_example",
            zh_hant="zh_hant_example",
            zh="zh_example",
            hr="hr_example",
            cs="cs_example",
            da="da_example",
            nl="nl_example",
            et="et_example",
            fi="fi_example",
            fr="fr_example",
            ka="ka_example",
            de="de_example",
            el="el_example",
            hi="hi_example",
            he="he_example",
            hu="hu_example",
            id="id_example",
            it="it_example",
            ja="ja_example",
            ko="ko_example",
            lv="lv_example",
            lt="lt_example",
            ms="ms_example",
            nb="nb_example",
            pl="pl_example",
            fa="fa_example",
            pt="pt_example",
            pa="pa_example",
            ro="ro_example",
            ru="ru_example",
            sr="sr_example",
            sk="sk_example",
            es="es_example",
            sv="sv_example",
            th="th_example",
            tr="tr_example",
            uk="uk_example",
            vi="vi_example",
        ),
        headings=LanguageStringMap(
            en="en_example",
            ar="ar_example",
            bs="bs_example",
            bg="bg_example",
            ca="ca_example",
            zh_hans="zh_hans_example",
            zh_hant="zh_hant_example",
            zh="zh_example",
            hr="hr_example",
            cs="cs_example",
            da="da_example",
            nl="nl_example",
            et="et_example",
            fi="fi_example",
            fr="fr_example",
            ka="ka_example",
            de="de_example",
            el="el_example",
            hi="hi_example",
            he="he_example",
            hu="hu_example",
            id="id_example",
            it="it_example",
            ja="ja_example",
            ko="ko_example",
            lv="lv_example",
            lt="lt_example",
            ms="ms_example",
            nb="nb_example",
            pl="pl_example",
            fa="fa_example",
            pt="pt_example",
            pa="pa_example",
            ro="ro_example",
            ru="ru_example",
            sr="sr_example",
            sk="sk_example",
            es="es_example",
            sv="sv_example",
            th="th_example",
            tr="tr_example",
            uk="uk_example",
            vi="vi_example",
        ),
        sound="sound_example",
        stale_date=1,
        dismissal_date=1,
        priority=1,
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

[rest_api_key](../README.md#rest_api_key)

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

# **update_subscription**
> update_subscription(app_id, subscription_id, subscription_body)



Updates an existing Subscription’s properties.

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
from onesignal.model.subscription_body import SubscriptionBody
from pprint import pprint

# Enter a context with an instance of the API client
with onesignal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    app_id = "app_id_example" 
    subscription_id = "subscription_id_example" 
    subscription_body = SubscriptionBody(
        subscription=Subscription(
            id="id_example",
            type="iOSPush",
            token="token_example",
            enabled=True,
            notification_types=1,
            session_time=1,
            session_count=1,
            sdk="sdk_example",
            device_model="device_model_example",
            device_os="device_os_example",
            rooted=True,
            test_type=1,
            app_version="app_version_example",
            net_type=1,
            carrier="carrier_example",
            web_auth="web_auth_example",
            web_p256="web_p256_example",
        ),
    ) 

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_subscription(app_id, subscription_id, subscription_body)
    except onesignal.ApiException as e:
        print("Exception when calling DefaultApi->update_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **subscription_id** | **str**|  |
 **subscription_body** | [**SubscriptionBody**](SubscriptionBody.md)|  |

### Return type

void (empty response body)

### Authorization

[rest_api_key](../README.md#rest_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> PropertiesBody update_user(app_id, alias_label, alias_id, update_user_request)



Updates an existing User’s properties.

### Example

* Bearer Authentication (rest_api_key):

```python
import onesignal
from onesignal.api import default_api
from onesignal.model.update_user_request import UpdateUserRequest
from onesignal.model.properties_body import PropertiesBody
from onesignal.model.rate_limit_error import RateLimitError
from onesignal.model.generic_error import GenericError
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
            first_active=1,
            last_active=1,
            amount_spent=3.14,
            purchases=[
                Purchase(
                    sku="sku_example",
                    amount="amount_example",
                    iso="iso_example",
                    count=1,
                ),
            ],
            ip="ip_example",
        ),
        refresh_device_metadata=False,
        deltas=PropertiesDeltas(
            session_time=1,
            session_count=1,
            purchases=[
                Purchase(
                    sku="sku_example",
                    amount="amount_example",
                    iso="iso_example",
                    count=1,
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

[**PropertiesBody**](PropertiesBody.md)

### Authorization

[rest_api_key](../README.md#rest_api_key)

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


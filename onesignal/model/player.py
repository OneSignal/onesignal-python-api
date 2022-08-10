"""
    OneSignal

    A powerful way to send personalized messages at scale and build effective customer engagement strategies. Learn more at onesignal.com  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: devrel@onesignal.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from onesignal.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from onesignal.exceptions import ApiAttributeError



class Player(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'id': (str,),  # noqa: E501
            'device_type': (int,),  # noqa: E501
            'invalid_identifier': (bool,),  # noqa: E501
            'app_id': (str,),  # noqa: E501
            'external_user_id': (str, none_type,),  # noqa: E501
            'external_user_id_auth_hash': (str,),  # noqa: E501
            'email_auth_hash': (str,),  # noqa: E501
            'identifier': (str, none_type,),  # noqa: E501
            'language': (str,),  # noqa: E501
            'timezone': (int, none_type,),  # noqa: E501
            'game_version': (str, none_type,),  # noqa: E501
            'device_model': (str, none_type,),  # noqa: E501
            'device_os': (str, none_type,),  # noqa: E501
            'ad_id': (str, none_type,),  # noqa: E501
            'sdk': (str, none_type,),  # noqa: E501
            'session_count': (int,),  # noqa: E501
            'tags': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'amount_spent': (float,),  # noqa: E501
            'created_at': (int,),  # noqa: E501
            'playtime': (int,),  # noqa: E501
            'badge_count': (int,),  # noqa: E501
            'last_active': (int,),  # noqa: E501
            'notification_types': (int,),  # noqa: E501
            'test_type': (int, none_type,),  # noqa: E501
            'long': (float,),  # noqa: E501
            'lat': (float,),  # noqa: E501
            'country': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'device_type': 'device_type',  # noqa: E501
        'invalid_identifier': 'invalid_identifier',  # noqa: E501
        'app_id': 'app_id',  # noqa: E501
        'external_user_id': 'external_user_id',  # noqa: E501
        'external_user_id_auth_hash': 'external_user_id_auth_hash',  # noqa: E501
        'email_auth_hash': 'email_auth_hash',  # noqa: E501
        'identifier': 'identifier',  # noqa: E501
        'language': 'language',  # noqa: E501
        'timezone': 'timezone',  # noqa: E501
        'game_version': 'game_version',  # noqa: E501
        'device_model': 'device_model',  # noqa: E501
        'device_os': 'device_os',  # noqa: E501
        'ad_id': 'ad_id',  # noqa: E501
        'sdk': 'sdk',  # noqa: E501
        'session_count': 'session_count',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'amount_spent': 'amount_spent',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'playtime': 'playtime',  # noqa: E501
        'badge_count': 'badge_count',  # noqa: E501
        'last_active': 'last_active',  # noqa: E501
        'notification_types': 'notification_types',  # noqa: E501
        'test_type': 'test_type',  # noqa: E501
        'long': 'long',  # noqa: E501
        'lat': 'lat',  # noqa: E501
        'country': 'country',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'invalid_identifier',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, device_type, *args, **kwargs):  # noqa: E501
        """Player - a model defined in OpenAPI

        Args:
            id (str): The device's OneSignal ID
            device_type (int): Required The device's platform:   0 = iOS   1 = Android   2 = Amazon   3 = WindowsPhone (MPNS)   4 = Chrome Apps / Extensions   5 = Chrome Web Push   6 = Windows (WNS)   7 = Safari   8 = Firefox   9 = MacOS   10 = Alexa   11 = Email   13 = For Huawei App Gallery Builds SDK Setup. Not for Huawei Devices using FCM   14 = SMS 

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            invalid_identifier (bool): If true, this is the equivalent of a user being Unsubscribed. [optional]  # noqa: E501
            app_id (str): [optional]  # noqa: E501
            external_user_id (str, none_type): a custom user ID. [optional]  # noqa: E501
            external_user_id_auth_hash (str): Only required if you have enabled Identity Verification and device_type is NOT 11 email.. [optional]  # noqa: E501
            email_auth_hash (str): Email - Only required if you have enabled Identity Verification and device_type is email (11).. [optional]  # noqa: E501
            identifier (str, none_type): Recommended: For Push Notifications, this is the Push Token Identifier from Google or Apple. For Apple Push identifiers, you must strip all non alphanumeric characters. Examples: iOS: 7abcd558f29d0b1f048083e2834ad8ea4b3d87d8ad9c088b33c132706ff445f0 Android: APA91bHbYHk7aq-Uam_2pyJ2qbZvqllyyh2wjfPRaw5gLEX2SUlQBRvOc6sck1sa7H7nGeLNlDco8lXj83HWWwzV... For Email Addresses, set the full email address email@email.com and make sure to set device_type to 11. . [optional]  # noqa: E501
            language (str): Language code. Typically lower case two letters, except for Chinese where it must be one of zh-Hans or zh-Hant. Example: en . [optional]  # noqa: E501
            timezone (int, none_type): Number of seconds away from UTC. Example: -28800 . [optional]  # noqa: E501
            game_version (str, none_type): Version of your app. Example: 1.1 . [optional]  # noqa: E501
            device_model (str, none_type): Device make and model. Example: iPhone5,1 . [optional]  # noqa: E501
            device_os (str, none_type): Device operating system version. Example: 7.0.4 . [optional]  # noqa: E501
            ad_id (str, none_type): The ad id for the device's platform: Android = Advertising Id iOS = identifierForVendor WP8.0 = DeviceUniqueId WP8.1 = AdvertisingId . [optional]  # noqa: E501
            sdk (str, none_type): Name and version of the sdk/plugin that's calling this API method (if any). [optional]  # noqa: E501
            session_count (int): Number of times the user has played the game, defaults to 1. [optional]  # noqa: E501
            tags ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): Custom tags for the player. Only support string and integer key value pairs. Does not support arrays or other nested objects. Setting a tag value to null or an empty string will remove the tag. Example: {\"foo\":\"bar\",\"this\":\"that\"} Limitations: - 100 tags per call - Android SDK users: tags cannot be removed or changed via API if set through SDK sendTag methods. Recommended to only tag devices with 1 kilobyte of data Please consider using your own Database to save more than 1 kilobyte of data. See: Internal Database & CRM . [optional]  # noqa: E501
            amount_spent (float): Amount the user has spent in USD, up to two decimal places. [optional]  # noqa: E501
            created_at (int): Unixtime when the player joined the game. [optional]  # noqa: E501
            playtime (int): Seconds player was running your app.. [optional]  # noqa: E501
            badge_count (int): Current iOS badge count displayed on the app icon NOTE: Not supported for apps created after June 2018, since badge count for apps created after this date are handled on the client. . [optional]  # noqa: E501
            last_active (int): Unixtime when the player was last active. [optional]  # noqa: E501
            notification_types (int): 1 = subscribed -2 = unsubscribed iOS - These values are set each time the user opens the app from the SDK. Use the SDK function set Subscription instead. Android - You may set this but you can no longer use the SDK method setSubscription later in your app as it will create synchronization issues. . [optional]  # noqa: E501
            test_type (int, none_type): This is used in deciding whether to use your iOS Sandbox or Production push certificate when sending a push when both have been uploaded. Set to the iOS provisioning profile that was used to build your app. 1 = Development 2 = Ad-Hoc Omit this field for App Store builds. . [optional]  # noqa: E501
            long (float): Longitude of the device, used for geotagging to segment on.. [optional]  # noqa: E501
            lat (float): Latitude of the device, used for geotagging to segment on.. [optional]  # noqa: E501
            country (str): Country code in the ISO 3166-1 Alpha 2 format. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.device_type = device_type
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, device_type, *args, **kwargs):  # noqa: E501
        """Player - a model defined in OpenAPI

            device_type (int): Required The device's platform:   0 = iOS   1 = Android   2 = Amazon   3 = WindowsPhone (MPNS)   4 = Chrome Apps / Extensions   5 = Chrome Web Push   6 = Windows (WNS)   7 = Safari   8 = Firefox   9 = MacOS   10 = Alexa   11 = Email   13 = For Huawei App Gallery Builds SDK Setup. Not for Huawei Devices using FCM   14 = SMS 

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            invalid_identifier (bool): If true, this is the equivalent of a user being Unsubscribed. [optional]  # noqa: E501
            app_id (str): [optional]  # noqa: E501
            external_user_id (str, none_type): a custom user ID. [optional]  # noqa: E501
            external_user_id_auth_hash (str): Only required if you have enabled Identity Verification and device_type is NOT 11 email.. [optional]  # noqa: E501
            email_auth_hash (str): Email - Only required if you have enabled Identity Verification and device_type is email (11).. [optional]  # noqa: E501
            identifier (str, none_type): Recommended: For Push Notifications, this is the Push Token Identifier from Google or Apple. For Apple Push identifiers, you must strip all non alphanumeric characters. Examples: iOS: 7abcd558f29d0b1f048083e2834ad8ea4b3d87d8ad9c088b33c132706ff445f0 Android: APA91bHbYHk7aq-Uam_2pyJ2qbZvqllyyh2wjfPRaw5gLEX2SUlQBRvOc6sck1sa7H7nGeLNlDco8lXj83HWWwzV... For Email Addresses, set the full email address email@email.com and make sure to set device_type to 11. . [optional]  # noqa: E501
            language (str): Language code. Typically lower case two letters, except for Chinese where it must be one of zh-Hans or zh-Hant. Example: en . [optional]  # noqa: E501
            timezone (int, none_type): Number of seconds away from UTC. Example: -28800 . [optional]  # noqa: E501
            game_version (str, none_type): Version of your app. Example: 1.1 . [optional]  # noqa: E501
            device_model (str, none_type): Device make and model. Example: iPhone5,1 . [optional]  # noqa: E501
            device_os (str, none_type): Device operating system version. Example: 7.0.4 . [optional]  # noqa: E501
            ad_id (str, none_type): The ad id for the device's platform: Android = Advertising Id iOS = identifierForVendor WP8.0 = DeviceUniqueId WP8.1 = AdvertisingId . [optional]  # noqa: E501
            sdk (str, none_type): Name and version of the sdk/plugin that's calling this API method (if any). [optional]  # noqa: E501
            session_count (int): Number of times the user has played the game, defaults to 1. [optional]  # noqa: E501
            tags ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): Custom tags for the player. Only support string and integer key value pairs. Does not support arrays or other nested objects. Setting a tag value to null or an empty string will remove the tag. Example: {\"foo\":\"bar\",\"this\":\"that\"} Limitations: - 100 tags per call - Android SDK users: tags cannot be removed or changed via API if set through SDK sendTag methods. Recommended to only tag devices with 1 kilobyte of data Please consider using your own Database to save more than 1 kilobyte of data. See: Internal Database & CRM . [optional]  # noqa: E501
            amount_spent (float): Amount the user has spent in USD, up to two decimal places. [optional]  # noqa: E501
            created_at (int): Unixtime when the player joined the game. [optional]  # noqa: E501
            playtime (int): Seconds player was running your app.. [optional]  # noqa: E501
            badge_count (int): Current iOS badge count displayed on the app icon NOTE: Not supported for apps created after June 2018, since badge count for apps created after this date are handled on the client. . [optional]  # noqa: E501
            last_active (int): Unixtime when the player was last active. [optional]  # noqa: E501
            notification_types (int): 1 = subscribed -2 = unsubscribed iOS - These values are set each time the user opens the app from the SDK. Use the SDK function set Subscription instead. Android - You may set this but you can no longer use the SDK method setSubscription later in your app as it will create synchronization issues. . [optional]  # noqa: E501
            test_type (int, none_type): This is used in deciding whether to use your iOS Sandbox or Production push certificate when sending a push when both have been uploaded. Set to the iOS provisioning profile that was used to build your app. 1 = Development 2 = Ad-Hoc Omit this field for App Store builds. . [optional]  # noqa: E501
            long (float): Longitude of the device, used for geotagging to segment on.. [optional]  # noqa: E501
            lat (float): Latitude of the device, used for geotagging to segment on.. [optional]  # noqa: E501
            country (str): Country code in the ISO 3166-1 Alpha 2 format. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.device_type = device_type
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

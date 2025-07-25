"""
    OneSignal

    A powerful way to send personalized messages at scale and build effective customer engagement strategies. Learn more at onesignal.com  # noqa: E501

    The version of the OpenAPI document: 5.2.0
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



class LanguageStringMap(ModelNormal):
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
            'en': (str,),  # noqa: E501
            'ar': (str,),  # noqa: E501
            'bs': (str,),  # noqa: E501
            'bg': (str,),  # noqa: E501
            'ca': (str,),  # noqa: E501
            'zh_hans': (str,),  # noqa: E501
            'zh_hant': (str,),  # noqa: E501
            'zh': (str,),  # noqa: E501
            'hr': (str,),  # noqa: E501
            'cs': (str,),  # noqa: E501
            'da': (str,),  # noqa: E501
            'nl': (str,),  # noqa: E501
            'et': (str,),  # noqa: E501
            'fi': (str,),  # noqa: E501
            'fr': (str,),  # noqa: E501
            'ka': (str,),  # noqa: E501
            'de': (str,),  # noqa: E501
            'el': (str,),  # noqa: E501
            'hi': (str,),  # noqa: E501
            'he': (str,),  # noqa: E501
            'hu': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'it': (str,),  # noqa: E501
            'ja': (str,),  # noqa: E501
            'ko': (str,),  # noqa: E501
            'lv': (str,),  # noqa: E501
            'lt': (str,),  # noqa: E501
            'ms': (str,),  # noqa: E501
            'nb': (str,),  # noqa: E501
            'pl': (str,),  # noqa: E501
            'fa': (str,),  # noqa: E501
            'pt': (str,),  # noqa: E501
            'pa': (str,),  # noqa: E501
            'ro': (str,),  # noqa: E501
            'ru': (str,),  # noqa: E501
            'sr': (str,),  # noqa: E501
            'sk': (str,),  # noqa: E501
            'es': (str,),  # noqa: E501
            'sv': (str,),  # noqa: E501
            'th': (str,),  # noqa: E501
            'tr': (str,),  # noqa: E501
            'uk': (str,),  # noqa: E501
            'vi': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'en': 'en',  # noqa: E501
        'ar': 'ar',  # noqa: E501
        'bs': 'bs',  # noqa: E501
        'bg': 'bg',  # noqa: E501
        'ca': 'ca',  # noqa: E501
        'zh_hans': 'zh-Hans',  # noqa: E501
        'zh_hant': 'zh-Hant',  # noqa: E501
        'zh': 'zh',  # noqa: E501
        'hr': 'hr',  # noqa: E501
        'cs': 'cs',  # noqa: E501
        'da': 'da',  # noqa: E501
        'nl': 'nl',  # noqa: E501
        'et': 'et',  # noqa: E501
        'fi': 'fi',  # noqa: E501
        'fr': 'fr',  # noqa: E501
        'ka': 'ka',  # noqa: E501
        'de': 'de',  # noqa: E501
        'el': 'el',  # noqa: E501
        'hi': 'hi',  # noqa: E501
        'he': 'he',  # noqa: E501
        'hu': 'hu',  # noqa: E501
        'id': 'id',  # noqa: E501
        'it': 'it',  # noqa: E501
        'ja': 'ja',  # noqa: E501
        'ko': 'ko',  # noqa: E501
        'lv': 'lv',  # noqa: E501
        'lt': 'lt',  # noqa: E501
        'ms': 'ms',  # noqa: E501
        'nb': 'nb',  # noqa: E501
        'pl': 'pl',  # noqa: E501
        'fa': 'fa',  # noqa: E501
        'pt': 'pt',  # noqa: E501
        'pa': 'pa',  # noqa: E501
        'ro': 'ro',  # noqa: E501
        'ru': 'ru',  # noqa: E501
        'sr': 'sr',  # noqa: E501
        'sk': 'sk',  # noqa: E501
        'es': 'es',  # noqa: E501
        'sv': 'sv',  # noqa: E501
        'th': 'th',  # noqa: E501
        'tr': 'tr',  # noqa: E501
        'uk': 'uk',  # noqa: E501
        'vi': 'vi',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """LanguageStringMap - a model defined in OpenAPI

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
            en (str): Text in English.  Will be used as a fallback. [optional]  # noqa: E501
            ar (str): Text in Arabic.. [optional]  # noqa: E501
            bs (str): Text in Bosnian.. [optional]  # noqa: E501
            bg (str): Text in Bulgarian.. [optional]  # noqa: E501
            ca (str): Text in Catalan.. [optional]  # noqa: E501
            zh_hans (str): Text in Chinese (Simplified).. [optional]  # noqa: E501
            zh_hant (str): Text in Chinese (Traditional).. [optional]  # noqa: E501
            zh (str): Alias for zh-Hans.. [optional]  # noqa: E501
            hr (str): Text in Croatian.. [optional]  # noqa: E501
            cs (str): Text in Czech.. [optional]  # noqa: E501
            da (str): Text in Danish.. [optional]  # noqa: E501
            nl (str): Text in Dutch.. [optional]  # noqa: E501
            et (str): Text in Estonian.. [optional]  # noqa: E501
            fi (str): Text in Finnish.. [optional]  # noqa: E501
            fr (str): Text in French.. [optional]  # noqa: E501
            ka (str): Text in Georgian.. [optional]  # noqa: E501
            de (str): Text in German.. [optional]  # noqa: E501
            el (str): Text in Greek.. [optional]  # noqa: E501
            hi (str): Text in Hindi.. [optional]  # noqa: E501
            he (str): Text in Hebrew.. [optional]  # noqa: E501
            hu (str): Text in Hungarian.. [optional]  # noqa: E501
            id (str): Text in Indonesian.. [optional]  # noqa: E501
            it (str): Text in Italian.. [optional]  # noqa: E501
            ja (str): Text in Japanese.. [optional]  # noqa: E501
            ko (str): Text in Korean.. [optional]  # noqa: E501
            lv (str): Text in Latvian.. [optional]  # noqa: E501
            lt (str): Text in Lithuanian.. [optional]  # noqa: E501
            ms (str): Text in Malay.. [optional]  # noqa: E501
            nb (str): Text in Norwegian.. [optional]  # noqa: E501
            pl (str): Text in Polish.. [optional]  # noqa: E501
            fa (str): Text in Persian.. [optional]  # noqa: E501
            pt (str): Text in Portugese.. [optional]  # noqa: E501
            pa (str): Text in Punjabi.. [optional]  # noqa: E501
            ro (str): Text in Romanian.. [optional]  # noqa: E501
            ru (str): Text in Russian.. [optional]  # noqa: E501
            sr (str): Text in Serbian.. [optional]  # noqa: E501
            sk (str): Text in Slovak.. [optional]  # noqa: E501
            es (str): Text in Spanish.. [optional]  # noqa: E501
            sv (str): Text in Swedish.. [optional]  # noqa: E501
            th (str): Text in Thai.. [optional]  # noqa: E501
            tr (str): Text in Turkish.. [optional]  # noqa: E501
            uk (str): Text in Ukrainian.. [optional]  # noqa: E501
            vi (str): Text in Vietnamese.. [optional]  # noqa: E501
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
    def __init__(self, *args, **kwargs):  # noqa: E501
        """LanguageStringMap - a model defined in OpenAPI

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
            en (str): Text in English.  Will be used as a fallback. [optional]  # noqa: E501
            ar (str): Text in Arabic.. [optional]  # noqa: E501
            bs (str): Text in Bosnian.. [optional]  # noqa: E501
            bg (str): Text in Bulgarian.. [optional]  # noqa: E501
            ca (str): Text in Catalan.. [optional]  # noqa: E501
            zh_hans (str): Text in Chinese (Simplified).. [optional]  # noqa: E501
            zh_hant (str): Text in Chinese (Traditional).. [optional]  # noqa: E501
            zh (str): Alias for zh-Hans.. [optional]  # noqa: E501
            hr (str): Text in Croatian.. [optional]  # noqa: E501
            cs (str): Text in Czech.. [optional]  # noqa: E501
            da (str): Text in Danish.. [optional]  # noqa: E501
            nl (str): Text in Dutch.. [optional]  # noqa: E501
            et (str): Text in Estonian.. [optional]  # noqa: E501
            fi (str): Text in Finnish.. [optional]  # noqa: E501
            fr (str): Text in French.. [optional]  # noqa: E501
            ka (str): Text in Georgian.. [optional]  # noqa: E501
            de (str): Text in German.. [optional]  # noqa: E501
            el (str): Text in Greek.. [optional]  # noqa: E501
            hi (str): Text in Hindi.. [optional]  # noqa: E501
            he (str): Text in Hebrew.. [optional]  # noqa: E501
            hu (str): Text in Hungarian.. [optional]  # noqa: E501
            id (str): Text in Indonesian.. [optional]  # noqa: E501
            it (str): Text in Italian.. [optional]  # noqa: E501
            ja (str): Text in Japanese.. [optional]  # noqa: E501
            ko (str): Text in Korean.. [optional]  # noqa: E501
            lv (str): Text in Latvian.. [optional]  # noqa: E501
            lt (str): Text in Lithuanian.. [optional]  # noqa: E501
            ms (str): Text in Malay.. [optional]  # noqa: E501
            nb (str): Text in Norwegian.. [optional]  # noqa: E501
            pl (str): Text in Polish.. [optional]  # noqa: E501
            fa (str): Text in Persian.. [optional]  # noqa: E501
            pt (str): Text in Portugese.. [optional]  # noqa: E501
            pa (str): Text in Punjabi.. [optional]  # noqa: E501
            ro (str): Text in Romanian.. [optional]  # noqa: E501
            ru (str): Text in Russian.. [optional]  # noqa: E501
            sr (str): Text in Serbian.. [optional]  # noqa: E501
            sk (str): Text in Slovak.. [optional]  # noqa: E501
            es (str): Text in Spanish.. [optional]  # noqa: E501
            sv (str): Text in Swedish.. [optional]  # noqa: E501
            th (str): Text in Thai.. [optional]  # noqa: E501
            tr (str): Text in Turkish.. [optional]  # noqa: E501
            uk (str): Text in Ukrainian.. [optional]  # noqa: E501
            vi (str): Text in Vietnamese.. [optional]  # noqa: E501
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

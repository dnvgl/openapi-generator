# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3
import functools  # noqa: F401
from urllib3._collections import HTTPHeaderDict

from petstore_api import api_client, exceptions
import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401

# query params


class EnumQueryStringArraySchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.SchemaEnumMakerClsFactory(
                enum_value_to_name={
                    ">": "GREATER_THAN",
                    "$": "DOLLAR",
                }
            ),
            schemas.StrSchema
        ):
            
            @classmethod
            @property
            def GREATER_THAN(cls):
                return cls(">")
            
            @classmethod
            @property
            def DOLLAR(cls):
                return cls("$")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'EnumQueryStringArraySchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class EnumQueryStringSchema(
    schemas.SchemaEnumMakerClsFactory(
        enum_value_to_name={
            "_abc": "_ABC",
            "-efg": "EFG",
            "(xyz)": "XYZ",
        }
    ),
    schemas.StrSchema
):
    
    @classmethod
    @property
    def _ABC(cls):
        return cls("_abc")
    
    @classmethod
    @property
    def EFG(cls):
        return cls("-efg")
    
    @classmethod
    @property
    def XYZ(cls):
        return cls("(xyz)")


class EnumQueryIntegerSchema(
    schemas.SchemaEnumMakerClsFactory(
        enum_value_to_name={
            1: "POSITIVE_1",
            -2: "NEGATIVE_2",
        }
    ),
    schemas.Int32Schema
):
    
    @classmethod
    @property
    def POSITIVE_1(cls):
        return cls(1)
    
    @classmethod
    @property
    def NEGATIVE_2(cls):
        return cls(-2)


class EnumQueryDoubleSchema(
    schemas.SchemaEnumMakerClsFactory(
        enum_value_to_name={
            1.1: "POSITIVE_1_PT_1",
            -1.2: "NEGATIVE_1_PT_2",
        }
    ),
    schemas.Float64Schema
):
    
    @classmethod
    @property
    def POSITIVE_1_PT_1(cls):
        return cls(1.1)
    
    @classmethod
    @property
    def NEGATIVE_1_PT_2(cls):
        return cls(-1.2)
# header params


class EnumHeaderStringArraySchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.SchemaEnumMakerClsFactory(
                enum_value_to_name={
                    ">": "GREATER_THAN",
                    "$": "DOLLAR",
                }
            ),
            schemas.StrSchema
        ):
            
            @classmethod
            @property
            def GREATER_THAN(cls):
                return cls(">")
            
            @classmethod
            @property
            def DOLLAR(cls):
                return cls("$")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'EnumHeaderStringArraySchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class EnumHeaderStringSchema(
    schemas.SchemaEnumMakerClsFactory(
        enum_value_to_name={
            "_abc": "_ABC",
            "-efg": "EFG",
            "(xyz)": "XYZ",
        }
    ),
    schemas.StrSchema
):
    
    @classmethod
    @property
    def _ABC(cls):
        return cls("_abc")
    
    @classmethod
    @property
    def EFG(cls):
        return cls("-efg")
    
    @classmethod
    @property
    def XYZ(cls):
        return cls("(xyz)")
# body param


class SchemaForRequestBodyApplicationXWwwFormUrlencoded(
    schemas.DictSchema
):


    class MetaOapg:
        class properties:
            
            
            class enum_form_string_array(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.SchemaEnumMakerClsFactory(
                            enum_value_to_name={
                                ">": "GREATER_THAN",
                                "$": "DOLLAR",
                            }
                        ),
                        schemas.StrSchema
                    ):
                        
                        @classmethod
                        @property
                        def GREATER_THAN(cls):
                            return cls(">")
                        
                        @classmethod
                        @property
                        def DOLLAR(cls):
                            return cls("$")
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'enum_form_string_array':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class enum_form_string(
                schemas.SchemaEnumMakerClsFactory(
                    enum_value_to_name={
                        "_abc": "_ABC",
                        "-efg": "EFG",
                        "(xyz)": "XYZ",
                    }
                ),
                schemas.StrSchema
            ):
                
                @classmethod
                @property
                def _ABC(cls):
                    return cls("_abc")
                
                @classmethod
                @property
                def EFG(cls):
                    return cls("-efg")
                
                @classmethod
                @property
                def XYZ(cls):
                    return cls("(xyz)")
            __annotations__ = {
                "enum_form_string_array": enum_form_string_array,
                "enum_form_string": enum_form_string,
            }
        additional_properties = schemas.AnyTypeSchema
    
    enum_form_string_array: MetaOapg.properties.enum_form_string_array
    enum_form_string: MetaOapg.properties.enum_form_string
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["enum_form_string_array"]) -> MetaOapg.properties.enum_form_string_array: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["enum_form_string"]) -> MetaOapg.properties.enum_form_string: ...
    
    def __getitem__(self, name: str) -> MetaOapg.additional_properties:
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        enum_form_string_array: typing.Union[MetaOapg.properties.enum_form_string_array, tuple, schemas.Unset] = schemas.unset,
        enum_form_string: typing.Union[MetaOapg.properties.enum_form_string, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
    ) -> 'SchemaForRequestBodyApplicationXWwwFormUrlencoded':
        return super().__new__(
            cls,
            *args,
            enum_form_string_array=enum_form_string_array,
            enum_form_string=enum_form_string,
            _configuration=_configuration,
            **kwargs,
        )
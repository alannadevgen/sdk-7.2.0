# coding: utf-8

"""
    Tenant API

    Tenant API

    The version of the OpenAPI document: 0.0.1
    Contact: abc@layer.fr
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ResourceType(str, Enum):
    """
    ResourceType
    """

    """
    allowed enum values
    """
    CATALOG = 'catalog'
    DATABASE = 'database'
    JOB = 'job'
    PROJECT = 'project'
    TABLE = 'table'
    USER = 'user'
    WORKFLOW = 'workflow'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ResourceType from a JSON string"""
        return cls(json.loads(json_str))



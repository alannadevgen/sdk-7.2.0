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
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from graalsystems.models.library import Library
from graalsystems.models.notifications import Notifications
from graalsystems.models.options import Options
from graalsystems.models.schedule import Schedule
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Job(BaseModel):
    """
    Job
    """ # noqa: E501
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    project_id: Optional[StrictStr] = None
    identity_id: Optional[StrictStr] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None
    timeout_seconds: Optional[StrictInt] = None
    max_retries: Optional[StrictInt] = None
    secrets: Optional[List[StrictStr]] = None
    libraries: Optional[List[Library]] = None
    options: Optional[Options] = None
    schedule: Optional[Schedule] = None
    notifications: Optional[Notifications] = None
    parameters: Optional[List[StrictStr]] = None
    labels: Optional[Dict[str, StrictStr]] = None
    metadata: Optional[Dict[str, Dict[str, Any]]] = None
    __properties: ClassVar[List[str]] = ["id", "name", "description", "project_id", "identity_id", "created", "updated", "timeout_seconds", "max_retries", "secrets", "libraries", "options", "schedule", "notifications", "parameters", "labels", "metadata"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Job from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in libraries (list)
        _items = []
        if self.libraries:
            for _item in self.libraries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['libraries'] = _items
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict['options'] = self.options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of schedule
        if self.schedule:
            _dict['schedule'] = self.schedule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of notifications
        if self.notifications:
            _dict['notifications'] = self.notifications.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Job from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "project_id": obj.get("project_id"),
            "identity_id": obj.get("identity_id"),
            "created": obj.get("created"),
            "updated": obj.get("updated"),
            "timeout_seconds": obj.get("timeout_seconds"),
            "max_retries": obj.get("max_retries"),
            "secrets": obj.get("secrets"),
            "libraries": [Library.from_dict(_item) for _item in obj.get("libraries")] if obj.get("libraries") is not None else None,
            "options": Options.from_dict(obj.get("options")) if obj.get("options") is not None else None,
            "schedule": Schedule.from_dict(obj.get("schedule")) if obj.get("schedule") is not None else None,
            "notifications": Notifications.from_dict(obj.get("notifications")) if obj.get("notifications") is not None else None,
            "parameters": obj.get("parameters"),
            "labels": obj.get("labels"),
            "metadata": obj.get("metadata")
        })
        return _obj



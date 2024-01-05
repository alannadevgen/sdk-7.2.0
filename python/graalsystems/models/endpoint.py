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
from pydantic import BaseModel, StrictStr
from graalsystems.models.file_library import FileLibrary
from graalsystems.models.uri import Uri
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Endpoint(BaseModel):
    """
    Endpoint
    """ # noqa: E501
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    version: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    library: Optional[FileLibrary] = None
    uri: Optional[Uri] = None
    instance_type: Optional[StrictStr] = None
    owner: Optional[StrictStr] = None
    infrastructure_id: Optional[StrictStr] = None
    device_id: Optional[StrictStr] = None
    public_url: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None
    labels: Optional[Dict[str, StrictStr]] = None
    metadata: Optional[Dict[str, Dict[str, Any]]] = None
    __properties: ClassVar[List[str]] = ["id", "name", "description", "version", "type", "library", "uri", "instance_type", "owner", "infrastructure_id", "device_id", "public_url", "status", "created", "updated", "labels", "metadata"]

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
        """Create an instance of Endpoint from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of library
        if self.library:
            _dict['library'] = self.library.to_dict()
        # override the default output from pydantic by calling `to_dict()` of uri
        if self.uri:
            _dict['uri'] = self.uri.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Endpoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "version": obj.get("version"),
            "type": obj.get("type"),
            "library": FileLibrary.from_dict(obj.get("library")) if obj.get("library") is not None else None,
            "uri": Uri.from_dict(obj.get("uri")) if obj.get("uri") is not None else None,
            "instance_type": obj.get("instance_type"),
            "owner": obj.get("owner"),
            "infrastructure_id": obj.get("infrastructure_id"),
            "device_id": obj.get("device_id"),
            "public_url": obj.get("public_url"),
            "status": obj.get("status"),
            "created": obj.get("created"),
            "updated": obj.get("updated"),
            "labels": obj.get("labels"),
            "metadata": obj.get("metadata")
        })
        return _obj


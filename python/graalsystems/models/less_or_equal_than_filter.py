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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class LessOrEqualThanFilter(BaseModel):
    """
    Filter values that are smaller or equal to a given value.  Attributes ---------- type : RelationalOperatorType     Type of the filter.
    """ # noqa: E501
    left: StrictStr = Field(description="Left operator for filter.")
    right: StrictStr = Field(description="Right operator for filter.")
    type: Optional[StrictStr] = Field(default='less_or_equal', description="Operator for LESS OR EQUAL filter.")
    __properties: ClassVar[List[str]] = ["left", "right", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('less_or_equal'):
            raise ValueError("must be one of enum values ('less_or_equal')")
        return value

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
        """Create an instance of LessOrEqualThanFilter from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of LessOrEqualThanFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "left": obj.get("left"),
            "right": obj.get("right"),
            "type": obj.get("type") if obj.get("type") is not None else 'less_or_equal'
        })
        return _obj



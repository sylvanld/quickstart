from enum import Enum
from re import Pattern
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, validator
from yaml import safe_load as safe_load_yaml


class ExtendedConfig(BaseModel):
    @classmethod
    def from_yaml_file(cls, path: str):
        with open(path, "r", encoding="utf-8") as file:
            raw_config = safe_load_yaml(file)
            return cls.parse_obj(raw_config)


class VariableType(Enum):
    BOOLEAN = "boolean"
    INTEGER = "integer"
    FLOAT = "float"
    STRING = "string"
    LIST = "list"


class InputVariable(BaseModel):
    name: str
    type: VariableType
    prompt: str = None
    required: bool = True
    regex: Optional[Pattern] = None
    choices: Optional[List[str]] = None

    @validator("regex")
    def validate_regex(cls, value, values):
        if value is None:
            return
        if values["type"] not in (VariableType.STRING, VariableType.LIST):
            raise ValueError(
                "Variables of type %s cannot define regular expression."
                % values["type"].value
            )

    @validator("choices")
    def validate_choices(cls, value, values):
        if value is None:
            return
        if values["type"] not in (VariableType.STRING, VariableType.LIST):
            raise ValueError(
                "Variables of type %s cannot define regular choices."
                % values["type"].value
            )
        return value


class TemplateConfig(ExtendedConfig):
    description: str
    version: str = Field(default="0.0.1")
    variables: List[InputVariable] = Field(default_factory=list)


class Context(ExtendedConfig):
    variables: Dict[str, str] = Field(default_factory=dict)

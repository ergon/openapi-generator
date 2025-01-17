# coding: utf-8

from datetime import date, datetime

from typing import Dict, List, Optional

from pydantic import BaseModel, EmailStr, validator


class ApiResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ApiResponse - a model defined in OpenAPI

        code: The code of this ApiResponse [Optional].
        type: The type of this ApiResponse [Optional].
        message: The message of this ApiResponse [Optional].
    """

    code: Optional[int] = None
    type: Optional[str] = None
    message: Optional[str] = None

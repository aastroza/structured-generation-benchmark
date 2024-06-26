# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:55:28+00:00

from __future__ import annotations

from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class SpecialtyEnum(Enum):
    Civil = 'Civil'
    Divorce = 'Divorce'
    Immigration = 'Immigration'
    Business = 'Business'
    Criminal = 'Criminal'


class LawyerFindNearby(BaseModel):
    city: str = Field(..., description='The city and state, e.g. Chicago, IL.')
    specialty: List[SpecialtyEnum] = Field(
        ..., description='Specialization of the lawyer.'
    )
    fee: int = Field(..., description='Hourly fee charged by lawyer')

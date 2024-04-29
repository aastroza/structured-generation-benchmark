# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:53:55+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ExplorationType(Enum):
    nature = 'nature'
    urban = 'urban'
    history = 'history'
    culture = 'culture'


class TravelItineraryGenerator(BaseModel):
    destination: str = Field(..., description='Destination city of the trip.')
    days: int = Field(..., description='Number of days for the trip.')
    daily_budget: int = Field(..., description='The maximum daily budget for the trip.')
    exploration_type: Optional[ExplorationType] = Field(
        'urban', description='The preferred exploration type.'
    )

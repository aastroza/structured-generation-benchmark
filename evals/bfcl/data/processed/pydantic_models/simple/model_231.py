# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:13+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class EventTypeEnum(Enum):
    War = 'War'
    Revolutions = 'Revolutions'
    Diplomacy = 'Diplomacy'
    Economy = 'Economy'


class HistoryGetKeyEvents(BaseModel):
    country: str = Field(
        ..., description='The name of the country for which history is queried.'
    )
    start_year: int = Field(
        ..., description='Start year of the period for which history is queried.'
    )
    end_year: int = Field(
        ..., description='End year of the period for which history is queried.'
    )
    event_type: Optional[List[EventTypeEnum]] = Field(
        [EventTypeEnum.War, EventTypeEnum.Revolutions, EventTypeEnum.Diplomacy, EventTypeEnum.Economy],
        description="Types of event. Default to 'all', which all types will be considered.",
    )

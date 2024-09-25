# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:17+00:00

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class SpecificInfo(Enum):
    Start_Date = 'Start Date'
    End_Date = 'End Date'
    Participants = 'Participants'
    Result = 'Result'
    Notable_Figures = 'Notable Figures'
    Importance_in_History = 'Importance in History'


class UsHistoryGetEventInfo(BaseModel):
    event_name: str = Field(..., description='The name of the event.')
    specific_info: SpecificInfo = Field(
        ..., description='Specific aspect of information related to event.'
    )
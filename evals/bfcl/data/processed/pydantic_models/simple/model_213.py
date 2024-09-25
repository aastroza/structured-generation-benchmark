# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:01+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class FlightBook(BaseModel):
    departure_location: str = Field(
        ..., description='The location you are departing from.'
    )
    destination_location: str = Field(
        ..., description='The location you are flying to.'
    )
    date: str = Field(
        ...,
        description='The date of the flight. Accepts standard date format e.g., 2022-04-28.',
    )
    time: Optional[str] = Field(
        'morning', description="Preferred time of flight. Default is 'morning'."
    )
    direct_flight: Optional[bool] = Field(
        False,
        description='If set to true, only direct flights will be searched. Default is false.',
    )
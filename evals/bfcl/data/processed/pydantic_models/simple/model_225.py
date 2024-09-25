# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:09+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class PsychResearchGetPreference(BaseModel):
    category: str = Field(
        ...,
        description='The societal category the preference data is about. E.g. reading, transportation, food',
    )
    option_one: str = Field(..., description='The first option people could prefer.')
    option_two: str = Field(..., description='The second option people could prefer.')
    demographic: Optional[str] = Field(
        'all',
        description='Specific demographic of society to narrow down the research.',
    )
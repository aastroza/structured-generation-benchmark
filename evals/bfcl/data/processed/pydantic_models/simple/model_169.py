# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:55:30+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class CourtCaseSearch(BaseModel):
    docket_number: str = Field(..., description='The docket number for the case.')
    location: str = Field(
        ...,
        description='The location where the case is registered, in the format: state, e.g., Texas',
    )
    full_text: Optional[bool] = Field(
        False, description='Option to return the full text of the case ruling.'
    )
# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:53+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class PriceRange(Enum):
    free = 'free'
    cheap = 'cheap'
    moderate = 'moderate'
    expensive = 'expensive'


class ConcertSearch(BaseModel):
    genre: str = Field(..., description='Genre of the concert.')
    location: str = Field(..., description='City of the concert.')
    date: str = Field(
        ...,
        description='Date of the concert, e.g. this weekend, today, tomorrow, or date string.',
    )
    price_range: Optional[PriceRange] = Field(
        PriceRange.free,
        description="Expected price range of the concert tickets. Default is 'free'.",
    )

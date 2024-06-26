# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:55:14+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class StockPrice(BaseModel):
    company: str = Field(..., description='The company name.')
    days: int = Field(
        ..., description='The number of previous days to retrieve data for.'
    )
    data_type: Optional[str] = Field(
        'Close',
        description="The type of price data to retrieve (e.g., 'Open', 'Close', 'High', 'Low'). Default is 'Close'.",
    )

# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:58:07+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class ConvertCurrency(BaseModel):
    base_currency: str = Field(
        ..., description='The base currency in which the original amount is present.'
    )
    target_currency: str = Field(
        ..., description='The currency to which you want to convert.'
    )
    amount: int = Field(..., description='The amount you want to convert.')

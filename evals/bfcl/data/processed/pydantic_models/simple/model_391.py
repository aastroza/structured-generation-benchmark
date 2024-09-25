# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:58:06+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class GetExchangeRateWithFee(BaseModel):
    base_currency: str = Field(..., description='The base currency.')
    target_currency: str = Field(..., description='The target currency.')
    fee: float = Field(
        ...,
        description='The transaction fee in percentage. Default is 0%. This is a float type value.',
    )
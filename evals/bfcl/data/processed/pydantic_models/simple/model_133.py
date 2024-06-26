# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:55:05+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class FinancePredictFutureValue(BaseModel):
    present_value: int = Field(..., description='The present value of the investment.')
    annual_interest_rate: float = Field(
        ...,
        description='The annual interest rate of the investment. This is a float type value.',
    )
    compounding_periods_per_year: Optional[int] = Field(
        1,
        description='The number of times that interest is compounded per year. Default is 1 (annually).',
    )
    time_years: int = Field(..., description='The investment horizon in years.')

# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:53:59+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class CalculateElectricField(BaseModel):
    charge: int = Field(
        ..., description='Charge in coulombs producing the electric field.'
    )
    distance: int = Field(
        ...,
        description='Distance from the charge in meters where the field is being measured.',
    )
    permitivity: Optional[float] = Field(
        8.854e-12,
        description='Permitivity of the space where field is being calculated, default is 8.854e-12. This is a float type value.',
    )

# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:14+00:00

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class ActivityLevel(Enum):
    sedentary = 'sedentary'
    lightly_active = 'lightly active'
    moderately_active = 'moderately active'
    very_active = 'very active'
    extra_active = 'extra active'


class DiabetesPrediction(BaseModel):
    weight: int = Field(..., description='Weight of the person in lbs.')
    height: int = Field(..., description='Height of the person in inches.')
    activity_level: ActivityLevel = Field(
        ..., description='Physical activity level of the person.'
    )

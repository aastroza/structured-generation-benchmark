# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:57:44+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class FindRecipe(BaseModel):
    recipeName: str = Field(..., description="The recipe's name.")
    maxCalories: Optional[int] = Field(
        1000, description='The maximum calorie content of the recipe.'
    )

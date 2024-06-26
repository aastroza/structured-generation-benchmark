# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:57:40+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class DishType(Enum):
    soup = 'soup'
    main_dish = 'main dish'
    dessert = 'dessert'
    salad = 'salad'


class GetVeganRecipe(BaseModel):
    dish_type: DishType = Field(
        ..., description='The type of dish, e.g. soup, dessert, etc.'
    )
    cooking_time: int = Field(
        ..., description='The maximum cooking time for the recipe in minutes.'
    )
    ingredient_preference: Optional[List[str]] = Field(
        [],
        description='Preferred ingredients to be included in the recipe, if any. Default to not use it if not provided.',
    )

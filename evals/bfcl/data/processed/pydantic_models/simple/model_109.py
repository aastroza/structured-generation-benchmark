# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:48+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class RandomForestTrain(BaseModel):
    n_estimators: int = Field(..., description='The number of trees in the forest.')
    max_depth: int = Field(..., description='The maximum depth of the tree.')
    data: str = Field(..., description='The training data for the model.')

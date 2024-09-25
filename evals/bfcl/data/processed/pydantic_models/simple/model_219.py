# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:05+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class GetNeuronCoordinates(BaseModel):
    neuron_type: str = Field(
        ..., description='Type of neuron to find. For instance, GABA, Glutamate, etc.'
    )
    brain_region: str = Field(..., description='The region of the brain to consider.')
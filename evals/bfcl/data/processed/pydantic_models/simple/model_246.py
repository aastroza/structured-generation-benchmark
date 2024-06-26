# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:24+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class ScienceHistoryGetDiscoveryDetails(BaseModel):
    discovery: str = Field(..., description='The name of the discovery, e.g. Gravity')
    method_used: Optional[str] = Field(
        'default',
        description="The method used for the discovery, default value is 'default' which gives the most accepted method.",
    )

# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:59:19+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class NfilibraryIsmemberreadable(BaseModel):
    symbol: str = Field(..., description='The symbol to check for readability.')
    recursive: Optional[str] = Field(
        None,
        description='The InteropLibrary instance used for recursive checks (automatically provided by the runtime). Default null',
    )
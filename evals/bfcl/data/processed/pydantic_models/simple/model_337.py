# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:57:28+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class PokerGameWinner(BaseModel):
    players: List[str] = Field(..., description='Names of the players in a list.')
    cards: Dict[str, List[str]] = Field(
        ...,
        description='An object containing the player name as key and the cards as values in a list.',
    )
    type: Optional[str] = Field(
        'Texas Holdem', description="Type of poker game. Defaults to 'Texas Holdem'"
    )

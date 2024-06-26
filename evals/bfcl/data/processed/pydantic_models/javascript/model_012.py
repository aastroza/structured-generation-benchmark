# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:59:31+00:00

from __future__ import annotations

from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class RequestConfig(BaseModel):
    method: Optional[str] = Field(
        [], description='The HTTP method to be used for the request.'
    )
    headers: Optional[Dict[str, Any]] = Field(
        [], description='Any headers to be included in the request.'
    )
    body: Optional[str] = Field(
        [], description='The request payload, if needed for methods like POST.'
    )


class PerformDataFetch(BaseModel):
    apiEndpoint: str = Field(
        ...,
        description='The URL of the API endpoint from which the data will be fetched.',
    )
    requestConfig: RequestConfig = Field(
        ..., description='The configuration object for the API request.'
    )
    expectedResponse: Dict[str, Any] = Field(
        ..., description='The JSON object expected to be returned by the API call.'
    )
    handleErrors: Optional[str] = Field(
        None,
        description='If true, the function will handle errors gracefully and provide appropriate feedback. Default false',
    )

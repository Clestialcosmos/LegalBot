from typing import Any

from pydantic import BaseModel, Field


class APIResponse(BaseModel):
    """
    Standard API response used by all endpoints.
    """

    success: bool = Field(
        ...,
        description="Whether the request was successful.",
        examples=[True],
    )

    message: str = Field(
        ...,
        description="Human-readable response message.",
        examples=["Response generated successfully"],
    )

    data: Any | None = Field(
        default=None,
        description="Response payload.",
    )
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """
    User chat request.
    """

    message: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="User's legal query.",
        examples=["What is an FIR?"],
    )


class ChatResponse(BaseModel):
    """
    Chat response.
    """

    answer: str
import logging
import time

from groq import (
    Groq,
    GroqError,
    RateLimitError,
)

from app.config.settings import settings

logger = logging.getLogger(__name__)

MODEL_NAME = "llama-3.3-70b-versatile"


def get_client():

    if not settings.GROQ_API_KEY:

        raise ValueError(
            "GROQ_API_KEY is not configured."
        )

    return Groq(
        api_key=settings.GROQ_API_KEY,
    )


def generate_response(
    prompt: str,
    retries: int = 3,
) -> str:

    if not prompt.strip():

        return "Prompt is empty."

    client = get_client()

    for attempt in range(retries):

        try:

            response = client.chat.completions.create(

                model=MODEL_NAME,

                temperature=0.1,

                max_tokens=1200,

                top_p=0.95,

                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )

            answer = (
                response
                .choices[0]
                .message
                .content
                .strip()
            )

            if answer:

                return answer

        except RateLimitError:

            logger.warning(
                "Groq rate limit reached."
            )

            if attempt < retries - 1:

                time.sleep(3)

                continue

            return (
                "The AI service is currently busy. "
                "Please try again in a few minutes."
            )

        except GroqError as exc:

            logger.exception(exc)

            if attempt < retries - 1:

                time.sleep(2)

                continue

            return (
                "Unable to communicate with the AI service."
            )

        except Exception as exc:

            logger.exception(exc)

            if attempt < retries - 1:

                time.sleep(2)

                continue

            return (
                "Something went wrong while generating the response."
            )

    return (
        "Unable to generate a response."
    )
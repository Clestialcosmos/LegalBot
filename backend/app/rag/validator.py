import logging

logger = logging.getLogger(__name__)


REQUIRED_FIELDS = [
    "id",
    "domain",
    "category",
    "subcategory",
    "act",
    "section",
    "jurisdiction",
    "severity",
    "urgency",
    "intent",
    "keywords",
    "search_text",
    "translations",
    "source",
]


class ValidationError(Exception):
    pass


def _require(entry, field):

    if field not in entry:
        raise ValidationError(
            f"Missing field: {field}"
        )

    if entry[field] in (
        "",
        None,
    ):
        raise ValidationError(
            f"Empty field: {field}"
        )


def validate_translation(
    translation,
    language,
):

    if language not in translation:
        raise ValidationError(
            f"Missing translation: {language}"
        )

    obj = translation[language]

    required = [
        "title",
        "content",
        "steps",
        "documents_required",
    ]

    for field in required:

        if field not in obj:

            raise ValidationError(
                f"{language}.{field} missing"
            )


def validate_entry(entry):

    for field in REQUIRED_FIELDS:

        _require(
            entry,
            field,
        )

    validate_translation(
        entry["translations"],
        "en",
    )

    validate_translation(
        entry["translations"],
        "hi",
    )

    validate_translation(
        entry["translations"],
        "hinglish",
    )

    if len(entry["keywords"]) == 0:
        raise ValidationError(
            "No keywords"
        )

    if len(entry["intent"]) == 0:
        raise ValidationError(
            "No intent"
        )

    return True


def validate_entries(entries):

    ids = set()

    for entry in entries:

        validate_entry(entry)

        if entry["id"] in ids:

            raise ValidationError(
                f"Duplicate id {entry['id']}"
            )

        ids.add(
            entry["id"]
        )

    logger.info(
        "Validated %d entries",
        len(entries),
    )

    return True
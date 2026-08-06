from pathlib import Path


def clean_act_name(source: str) -> str:
    """
    Convert PDF filename into a readable Act name.
    """

    filename = Path(source).stem

    return filename.replace("_", " ")
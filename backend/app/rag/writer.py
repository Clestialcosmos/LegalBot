import json
from pathlib import Path


OUTPUT_DIR = Path("data/knowledge")

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


class KnowledgeWriter:

    def __init__(self):

        self.counter = {}

    def generate_id(
        self,
        domain: str,
    ):

        prefix = domain.upper()

        if prefix not in self.counter:
            self.counter[prefix] = 1

        value = self.counter[prefix]

        self.counter[prefix] += 1

        return f"{prefix}-{value:03d}"

    def save(
        self,
        domain: str,
        entries: list,
    ):

        filename = (
            OUTPUT_DIR
            / f"{domain.lower()}.json"
        )

        with open(
            filename,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                entries,
                f,
                indent=2,
                ensure_ascii=False,
            )

        print(
            f"Saved {len(entries)} entries -> {filename}"
        )
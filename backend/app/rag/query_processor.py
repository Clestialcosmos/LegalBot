import re


class QueryProcessor:

    def __init__(self):

        self.synonyms = {
            "constitution": [
                "constitution",
                "constitutional",
                "article",
                "article 14",
                "article 19",
                "article 21",
                "fundamental rights",
                "fundamental duties",
                "directive principles",
                "dpsp",
                "preamble",
                "writ",
                "habeas corpus",
                "mandamus",
                "certiorari",
                "prohibition",
                "quo warranto"
            ],

            "fir": [
                "fir",
                "first information report",
                "police complaint"
            ],

            "bail": [
                "bail",
                "anticipatory bail",
                "regular bail"
            ],

            "consumer": [
                "consumer",
                "customer",
                "buyer"
            ],

            "property": [
                "property",
                "land",
                "house",
                "flat"
            ],

            "cyber": [
                "cyber",
                "online",
                "internet",
                "digital",
                "hacking"
            ],

            "women": [
                "woman",
                "women",
                "wife",
                "girl",
                "domestic violence"
            ],

            "labour": [
                "labour",
                "employee",
                "worker",
                "salary",
                "wages"
            ],

            "family": [
                "family",
                "divorce",
                "marriage",
                "maintenance",
                "custody"
            ],

            "senior": [
                "senior citizen",
                "elder",
                "parents"
            ],

            "msme": [
                "msme",
                "business",
                "startup",
                "enterprise"
            ],

            "rti": [
                "rti",
                "right to information"
            ]

        }

    def clean(self, query: str):

        query = query.lower()

        query = re.sub(r"\s+", " ", query)

        query = re.sub(r"[^\w\s]", "", query)
        query = re.sub(
            r"article\s+(\d+[a-zA-Z]*)",
            r"article_\1",
            query,
        )

        query = re.sub(
            r"section\s+(\d+[a-zA-Z]*)",
            r"section_\1",
            query,
        )

        return query.strip()

    def expand(self, query: str):

        expanded = [query]

        for values in self.synonyms.values():

            for word in values:

                if re.search(rf"\b{re.escape(word)}\b", query):

                    expanded.extend(values)
                    break

        expanded = list(dict.fromkeys(expanded))

        result = " ".join(expanded)

        result = result.replace("article_", "article ")
        result = result.replace("section_", "section ")

        return result

    def process(self, query: str):

        cleaned = self.clean(query)

        expanded = self.expand(cleaned)

        return expanded


processor = QueryProcessor()
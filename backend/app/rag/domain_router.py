class DomainRouter:

    def __init__(self):

        self.domains = {
            "constitution": [
                "constitution",
                "constitutional",
                "article",
                "article 14",
                "article 19",
                "article 21",
                "fundamental rights",
                "directive principles",
                "dpsp",
                "preamble",
                "fundamental duties",
                "citizenship",
                "supreme court",
                "high court",
                "writ",
                "habeas corpus",
                "mandamus",
                "certiorari",
                "prohibition",
                "quo warranto"
            ],

            "consumer": [
                "consumer",
                "customer",
                "buyer",
                "refund",
                "defective",
                "complaint"
            ],

            "property": [
                "property",
                "land",
                "house",
                "flat",
                "sale",
                "gift",
                "lease",
                "mortgage"
            ],

            "family": [
                "family",
                "marriage",
                "divorce",
                "maintenance",
                "custody",
                "adoption"
            ],

            "women": [
                "woman",
                "women",
                "wife",
                "dowry",
                "domestic violence",
                "sexual harassment",
                "rape",
                "girl"
            ],

            "labour": [
                "labour",
                "worker",
                "employee",
                "salary",
                "wages",
                "employer",
                "termination"
            ],

            "cyber": [
                "cyber",
                "hacking",
                "online",
                "internet",
                "otp",
                "upi",
                "fraud",
                "phishing"
            ],

            "fir_bail": [
                "fir",
                "police",
                "complaint",
                "arrest",
                "bail",
                "anticipatory bail"
            ],

            "rti": [
                "rti",
                "right to information",
                "information officer",
                "public authority"
            ],

            "senior": [
                "senior citizen",
                "elder",
                "parents",
                "maintenance of parents"
            ],

            "msme": [
                "msme",
                "startup",
                "enterprise",
                "small business",
                "udyam"
            ]

        }

    def detect(self, query: str):
        print("=" * 50)
        print("USING DOMAIN ROUTER")

        query = query.lower()

        scores = {}

        for domain, keywords in self.domains.items():

            score = 0

            for keyword in keywords:

                if keyword in query:

                    if " " in keyword:
                        score += 3
                    else:
                        score += 1

            scores[domain] = score

        best_domain = max(scores, key=scores.get)

        if scores[best_domain] == 0:
            return "general"

        return best_domain


router = DomainRouter()
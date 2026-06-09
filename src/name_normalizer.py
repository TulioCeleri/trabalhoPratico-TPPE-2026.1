class NameNormalizer:

    @staticmethod
    def normalize(name: str) -> str:

        normalized = name.replace("`", "'")
        normalized = normalized.replace("’", "'")

        normalized = " ".join(
            normalized.split()
        )

        return normalized.title()
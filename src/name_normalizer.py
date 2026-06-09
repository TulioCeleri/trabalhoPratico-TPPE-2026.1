class NameNormalizer:

    @staticmethod
    def normalize(name: str) -> str:

        normalized = name.replace("`", "'")
        normalized = normalized.replace("’", "'")

        return normalized.title()
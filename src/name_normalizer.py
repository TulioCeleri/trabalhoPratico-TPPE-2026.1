class NameNormalizer:

    @staticmethod
    def normalize(name: str) -> str:
        return name.replace("`", "'").title()
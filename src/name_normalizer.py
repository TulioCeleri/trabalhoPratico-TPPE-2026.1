class NameNormalizer:

    @staticmethod
    def normalize(name: str) -> str:

        if not name:
            raise ValueError(
                "Nome não pode ser vazio"
            )

        normalized = name.replace("`", "'")
        normalized = normalized.replace("’", "'")

        normalized = " ".join(
            normalized.split()
        )

        return normalized.title()
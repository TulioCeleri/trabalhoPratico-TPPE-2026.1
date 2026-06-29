class NameTokenizer:
    PARTICLES = {"de", "da", "do", "dos", "das"}

    @staticmethod
    def tokens_without_particles(name: str) -> list[str]:
        tokens = name.split()

        normalized_tokens = [
            token.lower().replace(".", "")
            for token in tokens
        ]

        return [
            token
            for token in normalized_tokens
            if token not in NameTokenizer.PARTICLES
        ]
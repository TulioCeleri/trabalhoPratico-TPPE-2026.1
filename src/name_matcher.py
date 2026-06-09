class NameMatcher:

    PARTICLES = {"de", "da", "do", "dos", "das"}

    @staticmethod
    def are_equivalent(name_a: str, name_b: str) -> bool:
        tokens_a = NameMatcher._tokens_without_particles(name_a)
        tokens_b = NameMatcher._tokens_without_particles(name_b)

        if NameMatcher._matches_surname_with_initials(
            tokens_a,
            tokens_b
        ):
            return True

        if NameMatcher._matches_surname_with_initials(
            tokens_b,
            tokens_a
        ):
            return True

        return False

    @staticmethod
    def _tokens_without_particles(name: str) -> list[str]:
        tokens = name.split()

        return [
            token.lower()
            for token in tokens
            if token.lower() not in NameMatcher.PARTICLES
        ]

    @staticmethod
    def _matches_surname_with_initials(
        abbreviated_tokens: list[str],
        full_name_tokens: list[str]
    ) -> bool:
        if len(abbreviated_tokens) < 2:
            return False

        if len(full_name_tokens) < 2:
            return False

        surname = abbreviated_tokens[0]
        initials = abbreviated_tokens[1:]

        full_surname = full_name_tokens[-1]
        full_given_names = full_name_tokens[:-1]

        if surname != full_surname:
            return False

        if len(initials) != len(full_given_names):
            return False

        for initial, full_name in zip(
            initials,
            full_given_names
        ):
            if len(initial) != 1:
                return False

            if not full_name.startswith(initial):
                return False

        return True
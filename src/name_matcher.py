class NameMatcher:

    PARTICLES = {"de", "da", "do", "dos", "das"}

    @staticmethod
    def are_equivalent(name_a: str, name_b: str) -> bool:
        tokens_a = [
            token.lower()
            for token in name_a.split()
            if token.lower() not in NameMatcher.PARTICLES
        ]

        tokens_b = [
            token.lower()
            for token in name_b.split()
            if token.lower() not in NameMatcher.PARTICLES
        ]

        if len(tokens_a) < 2 or len(tokens_b) < 2:
            return False

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
    def _matches_surname_with_initials(
        abbreviated_tokens: list[str],
        full_name_tokens: list[str]
    ) -> bool:
        surname = abbreviated_tokens[0]
        initials = abbreviated_tokens[1:]

        full_surname = full_name_tokens[-1]
        full_given_names = full_name_tokens[:-1]

        if surname != full_surname:
            return False

        if len(initials) != len(full_given_names):
            return False

        for initial, full_name in zip(initials, full_given_names):
            if len(initial) != 1:
                return False

            if not full_name.startswith(initial):
                return False

        return True
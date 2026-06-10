class NameMatcher:

    PARTICLES = {"de", "da", "do", "dos", "das"}

    @staticmethod
    def are_equivalent(name_a: str, name_b: str) -> bool:
        NameMatcher._validate_names(name_a, name_b)

        tokens_a = NameMatcher._tokens_without_particles(name_a)
        tokens_b = NameMatcher._tokens_without_particles(name_b)

        if NameMatcher._matches_grouped_initials_in_any_order(
            tokens_a,
            tokens_b
        ):
            return True

        return (
            NameMatcher._same_tokens_or_initials(
                tokens_a,
                tokens_b
            )
            or
            NameMatcher._matches_surname_with_initials_in_any_order(
                tokens_a,
                tokens_b
            )
        )

    @staticmethod
    def _validate_names(name_a: str, name_b: str) -> None:
        if not name_a or not name_b:
            raise ValueError("Nomes não podem ser vazios")

    @staticmethod
    def _tokens_without_particles(name: str) -> list[str]:
        tokens = name.split()

        normalized_tokens = [
            token.lower().replace(".", "")
            for token in tokens
        ]

        return [
            token
            for token in normalized_tokens
            if token not in NameMatcher.PARTICLES
        ]

    @staticmethod
    def _matches_grouped_initials_in_any_order(
        tokens_a: list[str],
        tokens_b: list[str]
    ) -> bool:
        return (
            NameMatcher._matches_grouped_initials(
                tokens_a,
                tokens_b
            )
            or
            NameMatcher._matches_grouped_initials(
                tokens_b,
                tokens_a
            )
        )

    @staticmethod
    def _matches_grouped_initials(
        abbreviated_tokens: list[str],
        full_name_tokens: list[str]
    ) -> bool:
        if len(abbreviated_tokens) != 2:
            return False

        grouped_initials = abbreviated_tokens[0]
        surname = abbreviated_tokens[1]

        if surname != full_name_tokens[-1]:
            return False

        full_given_names = full_name_tokens[:-1]

        if len(grouped_initials) != len(full_given_names):
            return False

        for initial, full_name in zip(
            grouped_initials,
            full_given_names
        ):
            if not full_name.startswith(initial):
                return False

        return True

    @staticmethod
    def _same_tokens_or_initials(
        tokens_a: list[str],
        tokens_b: list[str]
    ) -> bool:
        if len(tokens_a) != len(tokens_b):
            return False

        for token_a, token_b in zip(
            tokens_a,
            tokens_b
        ):
            if token_a == token_b:
                continue

            if len(token_a) == 1 and token_b.startswith(token_a):
                continue

            if len(token_b) == 1 and token_a.startswith(token_b):
                continue

            return False

        return True

    @staticmethod
    def _matches_surname_with_initials_in_any_order(
        tokens_a: list[str],
        tokens_b: list[str]
    ) -> bool:
        return (
            NameMatcher._matches_surname_with_initials(
                tokens_a,
                tokens_b
            )
            or
            NameMatcher._matches_surname_with_initials(
                tokens_b,
                tokens_a
            )
        )

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
from src.name_matcher import NameMatcher


class AuthorDeduplicator:

    @staticmethod
    def deduplicate(authors):
        if len(authors) < 2:
            return authors

        first_author = authors[0]
        second_author = authors[1]

        if NameMatcher.are_equivalent(
            first_author.name,
            second_author.name
        ):
            return [
                AuthorDeduplicator._author_with_smallest_id(
                    first_author,
                    second_author
                )
            ]

        return authors

    @staticmethod
    def _author_with_smallest_id(
        first_author,
        second_author
    ):
        if (
            first_author.author_id
            <=
            second_author.author_id
        ):
            return first_author

        return second_author
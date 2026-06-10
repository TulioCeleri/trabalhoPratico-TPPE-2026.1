from src.name_matcher import NameMatcher


class AuthorDeduplicator:

    @staticmethod
    def deduplicate(authors):
        deduplicated_authors = []

        for author in authors:
            AuthorDeduplicator._add_author(
                author,
                deduplicated_authors
            )

        return deduplicated_authors

    @staticmethod
    def _add_author(
        author,
        deduplicated_authors
    ):
        duplicate_index = (
            AuthorDeduplicator._find_duplicate(
                author,
                deduplicated_authors
            )
        )

        if duplicate_index == -1:
            deduplicated_authors.append(author)
            return

        existing_author = (
            deduplicated_authors[
                duplicate_index
            ]
        )

        deduplicated_authors[
            duplicate_index
        ] = (
            AuthorDeduplicator
            ._author_with_smallest_id(
                existing_author,
                author
            )
        )

    @staticmethod
    def _find_duplicate(
        author,
        deduplicated_authors
    ):
        for index, existing_author in enumerate(
            deduplicated_authors
        ):
            if NameMatcher.are_equivalent(
                author.name,
                existing_author.name
            ):
                return index

        return -1

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
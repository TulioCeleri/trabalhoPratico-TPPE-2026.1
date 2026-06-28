from src.author_record import AuthorRecord
from src.name_matcher import NameMatcher


class AddAuthorCommand:
    def __init__(self, author: AuthorRecord, deduplicated_authors: list[AuthorRecord]):
        self.author = author
        self.deduplicated_authors = deduplicated_authors

    def execute(self) -> None:
        duplicate_index = AuthorDeduplicator._find_duplicate(
            self.author,
            self.deduplicated_authors
        )

        if duplicate_index == -1:
            self.deduplicated_authors.append(self.author)
            return

        existing_author = self.deduplicated_authors[duplicate_index]

        self.deduplicated_authors[duplicate_index] = (
            AuthorDeduplicator._author_with_smallest_id(
                existing_author,
                self.author
            )
        )

class AuthorDeduplicator:

    @staticmethod
    def deduplicate(
        authors: list[AuthorRecord]
    ) -> list[AuthorRecord]:
        deduplicated_authors = []

        for author in authors:
            AuthorDeduplicator._add_author(
                author,
                deduplicated_authors
            )

        return deduplicated_authors

    @staticmethod
    def _add_author(
        author: AuthorRecord,
        deduplicated_authors: list[AuthorRecord]
    ) -> None:
        command = AddAuthorCommand(
            author,
            deduplicated_authors
        )
        command.execute()

    @staticmethod
    def _find_duplicate(
        author: AuthorRecord,
        deduplicated_authors: list[AuthorRecord]
    ) -> int:
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
        first_author: AuthorRecord,
        second_author: AuthorRecord
    ) -> AuthorRecord:
        if AuthorDeduplicator._is_id_smaller_or_equal(first_author, second_author):
            return first_author

        return second_author

    @staticmethod
    def _is_id_smaller_or_equal(
        first_author: AuthorRecord,
        second_author: AuthorRecord
    ) -> bool:
        return first_author.author_id <= second_author.author_id
import pytest

from src.author_record import AuthorRecord
from src.author_deduplicator import AuthorDeduplicator


@pytest.mark.case5
def test_duplicate_authors_keep_only_one_record():
    authors = [
        AuthorRecord(
            10,
            "AM Seabra"
        ),
        AuthorRecord(
            5,
            "Ana de Mattos Seabra"
        )
    ]

    deduplicated_authors = AuthorDeduplicator.deduplicate(
        authors
    )

    assert len(deduplicated_authors) == 1
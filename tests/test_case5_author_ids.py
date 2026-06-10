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


@pytest.mark.case5
def test_duplicate_authors_keep_smallest_identifier():
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

    assert deduplicated_authors[0].author_id == 5


@pytest.mark.case5
def test_deduplicate_multiple_authors():
    authors = [
        AuthorRecord(
            10,
            "AM Seabra"
        ),
        AuthorRecord(
            5,
            "Ana de Mattos Seabra"
        ),
        AuthorRecord(
            20,
            "Cassius de Souza"
        )
    ]

    deduplicated_authors = AuthorDeduplicator.deduplicate(
        authors
    )

    assert len(deduplicated_authors) == 2

    author_ids = sorted(
        author.author_id
        for author in deduplicated_authors
    )

    assert author_ids == [5, 20]
import pytest

from src.name_matcher import NameMatcher


@pytest.mark.case2
def test_surname_with_initials_without_dots_matches_full_name():
    assert NameMatcher.are_equivalent(
        "Seabra A M",
        "Ana de Mattos Seabra"
    )


@pytest.mark.case2
def test_surname_with_dotted_initial_matches_full_name():
    assert NameMatcher.are_equivalent(
        "Souza C.",
        "Cassius de Souza"
    )
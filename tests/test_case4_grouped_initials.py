import pytest

from src.name_matcher import NameMatcher


@pytest.mark.case4
def test_grouped_initials_match_full_name():
    assert NameMatcher.are_equivalent(
        "AM Seabra",
        "Ana de Mattos Seabra"
    )
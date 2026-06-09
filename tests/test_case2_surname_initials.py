import pytest

from src.name_matcher import NameMatcher


@pytest.mark.case2
@pytest.mark.parametrize(
    "abbreviated_name, full_name",
    [
        (
            "Seabra A M",
            "Ana de Mattos Seabra"
        ),
        (
            "Souza C.",
            "Cassius de Souza"
        ),
    ]
)
def test_surname_with_initials_matches_full_name(
    abbreviated_name,
    full_name
):
    assert NameMatcher.are_equivalent(
        abbreviated_name,
        full_name
    )
import pytest

from src.name_matcher import NameMatcher


@pytest.mark.case3
def test_optional_particles_match_full_name():
    assert NameMatcher.are_equivalent(
        "Luiz Oliveira Souza",
        "Luiz de Oliveira de Souza"
    )


@pytest.mark.case3
def test_middle_initial_with_dot_matches_full_name():
    assert NameMatcher.are_equivalent(
        "Luiz de O. de Souza",
        "Luiz de Oliveira de Souza"
    )
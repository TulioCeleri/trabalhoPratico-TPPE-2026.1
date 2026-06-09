import pytest

from src.name_matcher import NameMatcher


@pytest.mark.case3
def test_optional_particles_match_full_name():
    assert NameMatcher.are_equivalent(
        "Luiz Oliveira Souza",
        "Luiz de Oliveira de Souza"
    )
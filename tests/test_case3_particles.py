import pytest

from src.name_matcher import NameMatcher


@pytest.mark.case3
@pytest.mark.parametrize(
    "variant_name, full_name",
    [
        (
            "Luiz Oliveira Souza",
            "Luiz de Oliveira de Souza"
        ),
        (
            "Luiz de O. de Souza",
            "Luiz de Oliveira de Souza"
        ),
    ]
)
def test_particles_and_dots_are_optional(
    variant_name,
    full_name
):
    assert NameMatcher.are_equivalent(
        variant_name,
        full_name
    )
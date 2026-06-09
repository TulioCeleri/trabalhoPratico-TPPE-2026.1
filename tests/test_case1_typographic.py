import pytest

from src.name_normalizer import NameNormalizer


def test_replace_backtick_apostrophe():
    assert (
        NameNormalizer.normalize(
            "Monica Hirata Sant`anna"
        )
        ==
        "Monica Hirata Sant'Anna"
    )


def test_replace_curly_apostrophe():
    assert (
        NameNormalizer.normalize(
            "Monica Hirata Sant’anna"
        )
        ==
        "Monica Hirata Sant'Anna"
    )


def test_remove_extra_spaces():
    assert (
        NameNormalizer.normalize(
            "Monica    Hirata    Sant`anna"
        )
        ==
        "Monica Hirata Sant'Anna"
    )


def test_empty_name():

    with pytest.raises(ValueError):
        NameNormalizer.normalize("")
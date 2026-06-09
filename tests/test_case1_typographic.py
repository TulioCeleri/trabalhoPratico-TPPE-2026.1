import pytest

from src.name_normalizer import NameNormalizer


@pytest.mark.case1
class TestCase1Typographic:

    def test_replace_backtick_apostrophe(self):
        assert (
            NameNormalizer.normalize(
                "Monica Hirata Sant`anna"
            )
            ==
            "Monica Hirata Sant'Anna"
        )

    def test_replace_curly_apostrophe(self):
        assert (
            NameNormalizer.normalize(
                "Monica Hirata Sant’anna"
            )
            ==
            "Monica Hirata Sant'Anna"
        )

    def test_remove_extra_spaces(self):
        assert (
            NameNormalizer.normalize(
                "Monica    Hirata    Sant`anna"
            )
            ==
            "Monica Hirata Sant'Anna"
        )

    def test_empty_name(self):
        with pytest.raises(ValueError):
            NameNormalizer.normalize("")
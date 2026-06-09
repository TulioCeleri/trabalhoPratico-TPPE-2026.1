from src.name_normalizer import NameNormalizer


def test_replace_backtick_apostrophe():
    assert (
        NameNormalizer.normalize(
            "Monica Hirata Sant`anna"
        )
        ==
        "Monica Hirata Sant'Anna"
    )
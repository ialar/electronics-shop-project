import pytest


def test_repr(kb):
    assert repr(kb) == "Keyboard('Dark Project KD87A', 9600, 5)"


def test_str(kb):
    assert str(kb) == "Dark Project KD87A"


def test_change_lang(kb):
    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"

    with pytest.raises(AttributeError):
        kb.language = 'CH'

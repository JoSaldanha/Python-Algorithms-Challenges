import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message_positive_even():
    assert encrypt_message("message", 4) == "ega_ssem"


def test_encrypt_message_positive_odd():
    assert encrypt_message("message", 3) == "sem_egas"


def test_encrypt_message_negative():
    assert encrypt_message("message", -1) == "egassem"


def test_encrypt_message_key_string():
    with pytest.raises(TypeError):
        encrypt_message("message", "abc")


def test_encrypt_message_message_integer():
    with pytest.raises(TypeError):
        encrypt_message(5, 5)

from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("message", 4) == "ega_ssem"
    assert encrypt_message("message", 3) == "sem_egas"
    assert encrypt_message("message", -1) == "egassem"
    with pytest.raises(TypeError):
        encrypt_message("message", "abc")
    with pytest.raises(TypeError):
        encrypt_message(5, 5)

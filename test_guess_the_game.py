from guess_the_word import choose_word, process_guess, word_list


def test_word_is_from_predefined_list():
    word = choose_word()
    assert word in word_list


def test_correct_guess():
    secret = "tape"
    display = ["_", "_", "_", "_"]

    result = process_guess(secret, "t", display)

    assert result == "correct"
    assert display == ["t", "_", "_", "_"]


def test_incorrect_guess():
    secret = "tape"
    display = ["_", "_", "_", "_"]

    result = process_guess(secret, "z", display)

    assert result == "incorrect"

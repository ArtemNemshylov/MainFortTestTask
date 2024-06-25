from toolkit import tokenize


def test_tokenize_simple():
    text = "Привіт, як справи?"
    expected_tokens = ["Привіт", ",", "як", "справи", "?"]
    assert tokenize(text) == expected_tokens


def test_tokenize_empty():
    text = ""
    expected_tokens = []
    assert tokenize(text) == expected_tokens


def test_tokenize_punctuation():
    text = "Hello!!! How are you???"
    expected_tokens = ["Hello", "!", "!", "!", "How", "are", "you", "?", "?", "?"]
    assert tokenize(text) == expected_tokens


def main():
    test_tokenize_simple()
    test_tokenize_empty()
    test_tokenize_punctuation()


if __name__ == "__main__":
    main()

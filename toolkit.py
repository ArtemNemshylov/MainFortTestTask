import nltk
from nltk.tokenize import word_tokenize


def tokenize(text):
    return word_tokenize(text)


if __name__ == "__main__":
    nltk.download('punkt')

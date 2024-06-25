import nltk
from nltk.tokenize import word_tokenize


def tokenize_text(text):
    return word_tokenize(text)


def pos_tag_text(text):
    return nltk.pos_tag(tokenize_text(text))


def chunk_text(text):
    return nltk.ne_chunk(pos_tag_text(text))


if __name__ == "__main__":
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('maxent_ne_chunker')
    nltk.download('words')

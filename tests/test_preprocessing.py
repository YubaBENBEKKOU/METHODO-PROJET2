# tests/test_preprocessing.py

from src.preprocessing import tokenize, clean_tokens, clean_text

def test_tokenize():
    assert tokenize("Hello world!") == ["hello", "world"]

def test_clean_tokens():
    tokens = ["Hi", "123", ".", "the", "cat", "on", "mat"]
    cleaned = clean_tokens(tokens)
    assert "123" not in cleaned
    assert "." not in cleaned
    assert "the" not in cleaned
    assert all(len(t) >= 3 for t in cleaned)

def test_clean_text_empty():
    assert clean_text("") == ""

def test_clean_text_stopwords():
    text = "This is a test of stopwords"
    cleaned = clean_text(text)
    assert "this" not in cleaned
    assert "is" not in cleaned
    assert "of" not in cleaned

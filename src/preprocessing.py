# src/preprocessing.py

import re
import string
from typing import List
from collections import Counter

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

STOPWORDS = set(stopwords.words('english'))
STEMMER = PorterStemmer()
LEMMATIZER = WordNetLemmatizer()


def tokenize(text: str) -> List[str]:
    """Découpe un texte en tokens (version simplifiée sans NLTK)."""
    return re.findall(r'\b\w+\b', text.lower())


def clean_tokens(tokens: List[str],
                 remove_stopwords: bool = True,
                 use_stemming: bool = False,
                 use_lemmatization: bool = True) -> List[str]:
    """Nettoie une liste de tokens : ponctuation, chiffres, mots courts, stopwords, stemming/lemmatisation."""
    cleaned = []
    for token in tokens:
        token = token.lower()
        token = token.strip(string.punctuation)
        if token.isdigit():
            continue
        if len(token) < 3:
            continue
        if remove_stopwords and token in STOPWORDS:
            continue
        if use_stemming:
            token = STEMMER.stem(token)
        elif use_lemmatization:
            token = LEMMATIZER.lemmatize(token)
        cleaned.append(token)
    return cleaned


def clean_text(text: str) -> str:
    """Pipeline complet : tokenisation, nettoyage, reconstitution du texte."""
    tokens = tokenize(text)
    cleaned_tokens = clean_tokens(tokens)
    return ' '.join(cleaned_tokens)


def corpus_statistics(corpus: List[str]) -> dict:
    """Retourne quelques stats sur le corpus nettoyé."""
    all_tokens = []
    for text in corpus:
        tokens = text.split()
        all_tokens.extend(tokens)
    total_tokens = len(all_tokens)
    unique_tokens = len(set(all_tokens))
    single_occurrence = sum(1 for word, count in Counter(all_tokens).items() if count == 1)
    return {
        "total_tokens": total_tokens,
        "unique_tokens": unique_tokens,
        "single_occurrence": single_occurrence
    }


def visualize_wordcloud(corpus: List[str], output_path: str = "wordcloud.png"):
    """Crée et sauvegarde un WordCloud du corpus."""
    from wordcloud import WordCloud
    text = ' '.join(corpus)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    wordcloud.to_file(output_path)
    print(f"WordCloud saved to {output_path}")

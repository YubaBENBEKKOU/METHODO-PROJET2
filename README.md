#  Tweet Classifier – Analyse, nettoyage et classification de tweets avec Python, Pytest et Docker

Bienvenue dans le projet *Tweet Classifier*, un pipeline complet pour analyser, nettoyer et classifier automatiquement des tweets à l’aide de Python.  
Le projet utilise nltk (avec une tokenisation simplifiée), scikit-learn pour la modélisation, pytest pour les tests unitaires, et *Docker* pour exécuter le tout de manière reproductible.

---

##  Fonctionnalités

-  *Analyse exploratoire (EDA)* : comprendre les données textuelles.
- *Prétraitement du texte* : tokenisation simple, stopwords, lemmatisation.
-  *Modélisation* : entraînement d’un modèle de classification supervisée.
- *Tests unitaires* : fiabilité assurée avec pytest.
-  *Docker* : exécution portable, sans configuration locale.

---

## Prérequis

-  Docker (Windows, macOS ou Linux)
-  (Optionnel) Python 3.11+ si tu veux exécuter localement sans Docker



pip install -r requirements.txt

### Lance Python dans le terminal :
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

python -W ignore::DeprecationWarning -m pytest

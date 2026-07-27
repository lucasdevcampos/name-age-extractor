# Name-Age-Extractor

Natural Language Processing with spaCy, Pandas & Regex.

## 📋 Description
Python tool that extracts **person names** (using spaCy NER) and **ages** (using Regex) from `.txt` files. The output is a clean Pandas DataFrame with duplicates and empty values removed.

## 🚀 Technologies
- Python 3.x
- Pandas
- spaCy (en_core_web_sm)
- Regex

## 📦 Installation

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm

OUTPUT
                      NAMES AGE
0       Andromeda  52
1     Marcus Webb  34
2       Sara Chen  12
3  Thomas Richter  47
4      Maya Patel  29
5            Maya  41
6          Thomas  38

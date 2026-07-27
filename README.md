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
0  Marcus Webb  52
1   Sara Chen   34
2  Thomas Richter 47
3    Maya Patel  29
4   Elena Rossi  41
5  James Okafor  38

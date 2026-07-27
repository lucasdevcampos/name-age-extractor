import re
import pandas as pd
import spacy

# --- OPEN DOC WITH TEXT ---
with open("crew.txt", 'r', encoding='utf-8') as archive:
    content = archive.read()

# --- CONF. LLM MODELING PROCESS NAMES ---
lang_processing = spacy.load("en_core_web_sm")
text_alt = lang_processing(content)
names = []

# --- FUNCTION FIND NAMES ---
def find_names():
    for ent in text_alt.ents:
        if ent.label_ == "PERSON":
            names.append(ent.text)
find_names()

# --- CONF SEARCH REGEX TO GET AGE ---
key = 2
numbers = rf'\d{{{key}}}'
search = re.findall(numbers, content)

# --- GENERAL TEXT CONF. ---
name_df = pd.DataFrame({'NAMES': names})
search_df = pd.DataFrame({'AGE': search})

# --- MERGING DATAFRAMES NAMES/AGE ---
data_1 = pd.concat([name_df, search_df], axis=1)

# REMOVE DUPLICATES AND EMPTY DATA
final_data = data_1.drop_duplicates().dropna()

# DATAFRAME FINAL
print(final_data)

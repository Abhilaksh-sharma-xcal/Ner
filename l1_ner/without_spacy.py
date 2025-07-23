import nltk
import re

text = """
Patient has a history of Type 2 Diabetes and is currently taking metformin.
There is no evidence of diabetic retinopathy. He denies having an insulin pump.
"""

sentences = nltk.sent_tokenize(text)

target_terms = ["diabetes mellitus", "Type 2 Diabetes", "T2DM", "metformin", "Glucophage"]
pattern = r'\b(' + '|'.join(target_terms) + r')\b'

for sentence in sentences:
    for match in re.finditer(pattern, sentence, re.IGNORECASE):
        print(f"Found Entity: '{match.group(0)}' in sentence: '{sentence}'")


print(sentences)
import spacy

# Load a powerful pre-trained English model (the 'trf' model is great)
# You may need to run: python -m spacy download en_core_web_trf
nlp = spacy.load("en_core_web_trf")

text = "Sundar Pichai from Google visited the new campus in Bengaluru."

doc = nlp(text)

print("--- Part-of-Speech (POS) Tagging for EVERY Token ---")

print(f"{'Text':<15} | {'POS Tag':<10} | {'Explanation'}")
print(f"{'-'*15} | {'-'*10} | {'-'*20}")

for token in doc:
    print(f"{token.text:<15} | {token.pos_:<10} | {spacy.explain(token.pos_)}")

print("\n--- For comparison, here is the NER output which 'skips' words ---")
for ent in doc.ents:
    print(f"- '{ent.text}' -> {ent.label_}")
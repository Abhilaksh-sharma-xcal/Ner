import stanza


stanza.download('en')
nlp = stanza.Pipeline('en')

text = """Show me allergies for the patient

Search using this additional information: patient_id: 022ad6b0-4df4-f85f-efed-fc245f20ff74

Return the final response as normal text"""

doc = nlp(text)

terms = []
for sentence in doc.sentences:
    for word in sentence.words:
        # 'upos' is the universal POS tag
        terms.append({'text': word.text, 'pos': word.upos})
print(terms)
import spacy
import pandas as pd
nlp = spacy.load("en_core_sci_sm")




text = """
Here are the documented conditions and significant findings for this patient: 
 - Stress (multiple entries, including 2022-2025 and earlier years)
 - Severe anxiety (panic) (2013-2019)
 - Social isolation (2019-2021)
 - Acute bronchitis (June 2021)
 - Acute viral pharyngitis (January 2017)
 - Viral sinusitis (multiple episodes: Feb 2019, Dec 2021)
 - Victim of intimate partner abuse (2013-2016)
 - Medication review due (various periods, including currently as of 2025)
 - Employment and educational statuses (part-time, full-time employment; not in labor force; higher educationùthese provide social context to the health record)


"""

doc = nlp(text)
truth = nlp(truth_values)


    
doc_entity_texts = {ent.text.lower().strip() for ent in doc.ents}
missing = []
missed = 0
correct = 0
for i in truth.ents:
    if i.text.lower().strip() in doc_entity_texts:
        correct += 1
    else:
        missed += 1
        missing.append(i.text)
    # print(i)


print("correctly identified :", correct)
print("incorrect :",missed)
print("one which were missing were: ", missing)
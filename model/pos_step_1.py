import pandas as pd
import spacy
from difflib import SequenceMatcher
from collections import defaultdict

nlp = spacy.load("en_core_web_sm")



def extract_pos_filtered_terms(text):
    doc = nlp(text)
    terms = []
    
    for token in doc:
        terms.append({token:token.lemma_,
                      'pos': token.pos_})
        # if (token.pos_ in ['NOUN', 'ADJ', 'PROPN'] and 
        #     not token.is_stop and 
        #     not token.is_punct and 
        #     len(token.text) > 1):
        #     terms.append({
        #         'text': token.text,
        #         'lemma': token.lemma_,
        #         'pos': token.pos_
        #     })
    
    return terms

# def extract_pos_filtered_terms(text):
#     doc = nlp(text)
#     terms = []
    
#     for token in doc:

#         if (token.pos_ in ['NOUN', 'ADJ', 'PROPN'] and 
#             not token.is_stop and 
#             not token.is_punct and 
#             len(token.text) > 1):
#             terms.append({
#                 'text': token.text,
#                 'lemma': token.lemma_,
#                 'pos': token.pos_
#             })
    
#     return terms

x = extract_pos_filtered_terms("""Show me allergies for the patient

 
 Search using this additional information: patient_id: 022ad6b0-4df4-f85f-efed-fc245f20ff74
 
  Return the final response as normal text"""
)


print(x)
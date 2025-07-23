import spacy
import medspacy
from medspacy.target_matcher import TargetRule
# nlp = spacy.load("en_core_web_sm", disable=["ner"])

nlp = spacy.blank("en")

nlp.add_pipe("medspacy_pyrush", first=True) 
nlp.add_pipe("medspacy_target_matcher") 
nlp.add_pipe("medspacy_context") 

print(nlp.pipe_names) #['medspacy_pyrush', 'tok2vec', 'tagger', 'parser', 'attribute_ruler', 'lemmatizer', 'medspacy_target_matcher', 'medspacy_context']

target_rules = [

    TargetRule(literal="diabetes mellitus", category="PROBLEM"),
    TargetRule(literal="Type 2 Diabetes", category="PROBLEM"),
    TargetRule(literal="T2DM", category="PROBLEM"),
    
    TargetRule(literal="metformin", category="TREATMENT"),
    TargetRule(literal="Glucophage", category="TREATMENT") 
]


target_matcher = nlp.get_pipe("medspacy_target_matcher")
target_matcher.add(target_rules)


text = """
Patient has a history of Type 2 Diabetes and is currently taking metformin. 
There is no evidence of diabetic retinopathy. He denies having an insulin pump.
"""


doc = nlp(text)
print("Extracted Entities:")
for ent in doc.ents:
    print(f"- Entity: '{ent.text}', Label: '{ent.label_}'")
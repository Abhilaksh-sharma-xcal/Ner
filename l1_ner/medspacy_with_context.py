import spacy
import medspacy
from medspacy.target_matcher import TargetRule
import os
import pandas as pd
import pyConTextNLP.pyConText as pyConText
import pyConTextNLP.itemData as itemData
from medspacy.context import ConTextRule

target_rules = []
def entity(inp_path):
    df = pd.read_csv(path)
    dataframe = df
    columns_to_use = df.columns.tolist()
    for column_name in columns_to_use:
        if column_name in dataframe.columns:
            for term in dataframe[column_name].dropna().unique():
                rule = TargetRule(literal=str(term), category=column_name.upper())
                target_rules.append(rule)
                
    
    
query_table = ["allergyintolerance","careplan","careplan_activity","careteam", "condition","diagnosticreport", "diagnosticreport_result", "encounter", "encounter_diagnosis", "encounter", "encounter_finding", "immunization", "medicationrequest", "medicationstatement", "medicationstatement_indication", "medicationstatement_precondition", "observation", "observation_component", "patient", "procedure", "questionnaire"]


for i in query_table:
    path = "D:/xcaliber/study/database/"
    path += i
    path +=".csv"
    entity(inp_path=path)
    
context_rules = [
    ConTextRule(literal="history of", category="HISTORICAL", direction="FORWARD"),
    ConTextRule(literal="h/o", category="HISTORICAL", direction="FORWARD"),
    ConTextRule(literal="past episodes of", category="HISTORICAL", direction="FORWARD"),
    ConTextRule(literal="patient was diagnosed with", category="HISTORICAL", direction="FORWARD"),

    ConTextRule(literal="denies", category="NEGATED_EXISTENCE", direction="FORWARD"),
    ConTextRule(literal="no signs of", category="NEGATED_EXISTENCE", direction="FORWARD"),
    ConTextRule(literal="ruled out", category="NEGATED_EXISTENCE", direction="BACKWARD"),
    ConTextRule(literal="without any", category="NEGATED_EXISTENCE", direction="FORWARD"),

    ConTextRule(literal="if", category="HYPOTHETICAL", direction="FORWARD"),
    ConTextRule(literal="what if", category="HYPOTHETICAL", direction="FORWARD"),
    ConTextRule(literal="potential for", category="HYPOTHETICAL", direction="FORWARD"),

    ConTextRule(literal="family history of", category="FAMILY", direction="FORWARD"),
    ConTextRule(literal="mother has", category="FAMILY", direction="FORWARD"),
    ConTextRule(literal="father has", category="FAMILY", direction="FORWARD"),
]

nlp = spacy.blank("en")

nlp.add_pipe("medspacy_pyrush", first=True)
nlp.add_pipe("medspacy_target_matcher") 
nlp.add_pipe("medspacy_context")

target_matcher = nlp.get_pipe("medspacy_target_matcher")
target_matcher.add(target_rules)

context = nlp.get_pipe("medspacy_context")
context.add(context_rules)

text = """
he has not sign of Hives.
if he has a allerfy of Hives.
 
"""

doc = nlp(text)
print("Extracted Entities:")
print(doc.ents)
for ent in doc.ents:
    print(f"Entity: '{ent.text}', Label: '{ent.label_}', Family: '{ent._.is_family}', Hypothetical: '{ent._.is_hypothetical}', Historical: '{ent._.is_historical}', Negated: '{ent._.is_negated}'")
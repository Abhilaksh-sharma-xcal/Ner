import spacy
import medspacy
from medspacy.target_matcher import TargetRule
import os
import json
import pandas as pd
# import pyConTextNLP.pyConText as pyConText
# import pyConTextNLP.itemData as itemData
from medspacy.context import ConTextRule



target_rules = []
def entity(inp_path):
    df = pd.read_csv(path)
    dataframe = df
    columns_to_use = df.columns.tolist()
    for column_name in columns_to_use:
        if column_name in dataframe.columns:
            for term in dataframe[column_name].dropna().unique():
                if (len(str(term)) > 2 or term) or str(term)[0].isdigit():
                    rule = TargetRule(literal=str(term), category=column_name.upper())
                    target_rules.append(rule)
                
    
    
query_table = ["allergyintolerance","careplan","careplan_activity","careteam", "condition","diagnosticreport", "diagnosticreport_result", "encounter", "encounter_diagnosis", "encounter", "encounter_finding", "immunization", "medicationrequest", "medicationstatement", "medicationstatement_indication", "medicationstatement_precondition", "observation", "observation_component", "patient", "procedure", "questionnaire"]

another_db = ["TRANSFERS", "PROCEDURES_ICD", "PROCEDUREEVENTS_MV", "PRESCRIPTIONS", "PATIENTS", "OUTPUTEVENTS", "NOTEEVENTS", "MICROBIOLOGYEVENTS", "LABEVENTS", "INPUTEVENTS_MV", "INPUTEVENTS_MV", "ICUSTAYS", "D_LABITEMS", "D_ITEMS", "D_ICD_PROCEDURES", "D_ICD_DIAGNOSES", "D_CPT", "DRGCODES", "DIAGNOSES_ICD", "DATETIMEEVENTS", "CPTEVENTS", "CHARTEVENTS", "CAREGIVERS", "CALLOUT", "ADMISSIONS"]

for i in query_table:
    path = "D:/xcaliber/study/database/"
    path += i
    path +=".csv"
    entity(inp_path=path)
    
for i in another_db:
    path = "D:/xcaliber/study/mimic-iii-clinical-database-demo-1.4/"
    path += i
    path +=".csv"
    entity(inp_path=path)    



rules_list = target_rules

    
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
target_matcher.add(rules_list)



with open(r"D:\xcaliber\study\data\patient_data_logs.json") as json_file:
    json_data = json.load(json_file)
    # print(json_data)

full = [ ]

for i in json_data:
    json_object = {}
    for key in i :
        print(key)
        if key == "patient":
            print("herer")
            continue
        x = []
        if i[key] == None:
            i[key] = "None"
        key_annotated = str(key+"_annotated")
        doc = nlp(i[key])
        
        # out["Entity"]= []
        # out["Label"]= []
        for ent in doc.ents:
            out = {}
            out["Entity"]= ent.text
            out["Label"] = ent.label_
            x.append(out)
        
        # json_object[key] = i[key]
        json_object[key_annotated] = x

        
    full.append(json_object)

final_file = r"D:\xcaliber\study\another_try_to_ner\files\x1.json"
with open(final_file,"w") as out:
    json.dump(full, out, indent=2)

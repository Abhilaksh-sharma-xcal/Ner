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
    
    




out_file = "rules.txt"
with open(out_file,"w") as file:
    # json.dump(target_rules, file)
    file.write(str(target_rules))
    
    
    

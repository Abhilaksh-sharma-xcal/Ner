from dotenv import load_dotenv
import os
import json 
import spacy
import medspacy
from medspacy.target_matcher import TargetRule
import pandas as pd
# import pyConTextNLP.pyConText as pyConText
# import pyConTextNLP.itemData as itemData
from medspacy.context import ConTextRule
from collections import namedtuple



load_dotenv()

data_sources = {
    "hie_database": {
        "path": r"D:\xcaliber\study\database\hie_database",
        "tables": {"allergyintolerance":[], "careplan":[], "careplan_activity":[], "careteam":[], "condition":[], "diagnosticreport":[], "diagnosticreport_result":[], "encounter":[], "encounter_diagnosis":[], "encounter_finding":[], "immunization":[], "medicationrequest":[], "medicationstatement":[], "medicationstatement_indication":[], "medicationstatement_precondition":[], "observation":[], "observation_component":[], "patient":[], "procedure":[], "questionnaire":[]}
    },
    "synt_database": {
        "path": r"D:\xcaliber\study\database\synt_database",
        "tables": {'allergies':[], 'careplans':[], 'claims':[], 'claims_transactions':[], 'conditions':[], 'devices':[], 'encounters':[], 'imaging_studies':[], 'immunizations':[], 'medications':[], 'observations':[], 'organizations':[], 'patients':[], 'payers':[], 'payer_transactions':[], 'procedures':[], 'providers':[]}
    },
    "mimic_demo": {
        "path": "D:/xcaliber/study/mimic-iii-clinical-database-demo-1.4/",
        "tables": {"TRANSFERS":[], "PROCEDURES_ICD":[], "PRESCRIPTIONS":[], "PATIENTS":[], "OUTPUTEVENTS":[], "NOTEEVENTS":[], "MICROBIOLOGYEVENTS":[], "LABEVENTS":[], "INPUTEVENTS_MV":[], "ICUSTAYS":[], "D_LABITEMS":[], "D_ITEMS":[], "D_ICD_PROCEDURES":[], "D_ICD_DIAGNOSES":[], "D_CPT":[], "DRGCODES":[], "DIAGNOSES_ICD":[], "DATETIMEEVENTS":[], "CPTEVENTS":[], "CHARTEVENTS":[], "CAREGIVERS":[], "CALLOUT":[], "ADMISSIONS":[]}
    }
}

with open(os.getenv("Original_logs"), "r") as file:
    x = file.read()


class l1_ner:
    def __init__(self, ner_rules):
        self.dicationary = ner_rules
        self.all_rules = []


    def rules_generation(self):
        # for i in self.dicationary:
        #     db = data_sources[i]
        #     source_name = db['path']
        for source_name, source_info in data_sources.items():
            base_path = source_info["path"]
            for table_name in source_info["tables"]:
                # self.all_rules.append(TargetRule(literal=table_name, category="Table"))
                file_path = os.path.join(base_path, f"{table_name}.csv")
    
                rules_from_file = create_entity_rules_from_file(file_path,self.all_rules)
    
            if rules_from_file:
                    self.all_rules.extend(rules_from_file)
        



def create_entity_rules_from_file(path,list_till_now):
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print(f"Warning: File not found at {path}, skipping.")
        return
    for column_name in df.columns:
        print(column_name)
        
        terms = df[column_name]
        # print(term)
        for term in terms:
            uni = str(term)
            if len(str(term)) > 2 or str(term)[0].isdigit():
                list_till_now.append(TargetRule(literal=uni, category=column_name))
            
            
    
    
    # target_rules = []
    
    # for column_name in df.columns:
    #     target_rules.append(TargetRule(literal=column_name, category='COLUMN'))
    #     if column_name in mapping_dict:
    #         category = mapping_dict[column_name]
    #         unique_terms = df[column_name].dropna().unique()
            
    #         for term in unique_terms:
    #             term_str = str(term)
    #             if len(term_str) > 2:
    #                 rule = TargetRule(literal=term_str, category=category)
    #                 target_rules.append(rule)
    #                 # print("appending somethings")
                    
    # return target_rules

        

x = l1_ner(data_sources)
x.rules_generation()


# with open("rules_start_1.txt","w") as file:
#     file.write(str(x.all_rules))
    
with open("rules_start_1.json", 'w') as f:
    for i in x.all_rules:
        json.dump(i, f)
    
# print(x.all_rules)
print(len(x.all_rules))


import pickle


# with open('rules_start_1.pkl', 'wb') as f:
#     pickle.dump(x.all_rules, f)
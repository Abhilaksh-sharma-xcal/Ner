import os
import pandas as pd
from medspacy.target_matcher import TargetRule
from collections import namedtuple

COLUMN_TO_NER_CATEGORY = {
    # Group 1: Medical Conditions / Diagnoses
    'reaction': 'MEDICAL_CONDITION',
    'diagnosis': 'MEDICAL_CONDITION',
    'health_status': 'MEDICAL_CONDITION',
    'condition_display': 'MEDICAL_CONDITION',
    'problem_display': 'MEDICAL_CONDITION',
    'finding_display': 'MEDICAL_CONDITION',
    'icd9_code': 'MEDICAL_CONDITION',
    'short_title': 'MEDICAL_CONDITION',
    'long_title': 'MEDICAL_CONDITION',
    'drg_code': 'MEDICAL_CONDITION',
    'indication_name': 'MEDICAL_CONDITION',

    # Group 2: Medications / Treatments
    'substance': 'MEDICATION',
    'drug': 'MEDICATION',
    'drug_name_poe': 'MEDICATION',
    'drug_name_generic': 'MEDICATION',
    'medication_name': 'MEDICATION',
    'vaccine_display': 'MEDICATION',
    'formulary_drug_cd': 'MEDICATION',
    'ndc': 'MEDICATION', # National Drug Code
    'fluid': 'MEDICATION',

    # Group 3: Medical Procedures
    'procedure_display': 'PROCEDURE',
    'cpt_cd': 'PROCEDURE', # CPT codes are for procedures

    # Group 4: Laboratory Tests & Vital Signs
    'report_display': 'LAB_TEST',
    'result_display': 'LAB_TEST',
    'observation_display': 'LAB_TEST',
    'component_display': 'LAB_TEST',
    'label': 'LAB_TEST', # from d_items/d_labitems
    'abbreviation': 'LAB_TEST',
    'loinc_code': 'LAB_TEST',
    'org_name': 'LAB_TEST', # Organism name
    'spec_type_desc': 'LAB_TEST', # Specimen type

    # Group 5: Test/Observation Values
    'result_value': 'MEASUREMENT',
    'value': 'MEASUREMENT',
    'valuenum': 'MEASUREMENT',
    'valueuom': 'MEASUREMENT',
    'component_value': 'MEASUREMENT',
    'interpretation': 'MEASUREMENT', # e.g., 'High', 'Normal'

    # Group 6: Dates and Times
    'onset_date': 'DATE_TIME',
    'end_date': 'DATE_TIME',
    'chartdate': 'DATE_TIME',
    'charttime': 'DATE_TIME',
    'admittime': 'DATE_TIME',
    'dischtime': 'DATE_TIME',
    'dob': 'DATE_TIME',

    # Group 7: Anatomy / Body Part
    'target_site_display': 'ANATOMY',
    
    # Group 8: Demographics & Personal/Provider Info
    'given_name': 'PERSON_NAME',
    'family_name': 'PERSON_NAME',
    'performer_name': 'PERSON_NAME',
    'gender': 'DEMOGRAPHIC',
    'ethnicity': 'DEMOGRAPHIC',
    'marital_status': 'DEMOGRAPHIC',
    'language': 'DEMOGRAPHIC',
}


TargetRule = namedtuple("TargetRule", ["literal", "category"])



def create_entity_rules_from_file(csv_path, mapping_dict):
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Warning: File not found at {csv_path}, skipping.")
        return []
    except Exception as e:
        print(f"Error reading {csv_path}: {e}")
        return []

    target_rules = []
    
    for column_name in df.columns:
        if column_name in mapping_dict:
            category = mapping_dict[column_name]
            unique_terms = df[column_name].dropna().unique()
            
            for term in unique_terms:
                term_str = str(term)
                if len(term_str) > 2:
                    rule = TargetRule(literal=term_str, category=category)
                    target_rules.append(rule)
                    
    return target_rules


data_sources = {
    "database": {
        "path": "D:/xcaliber/study/database/",
        "tables": ["allergyintolerance", "careplan", "careplan_activity", "careteam", "condition", "diagnosticreport", "diagnosticreport_result", "encounter", "encounter_diagnosis", "encounter_finding", "immunization", "medicationrequest", "medicationstatement", "medicationstatement_indication", "medicationstatement_precondition", "observation", "observation_component", "patient", "procedure", "questionnaire"]
    },
    "mimic_demo": {
        "path": "D:/xcaliber/study/mimic-iii-clinical-database-demo-1.4/",
        "tables": ["TRANSFERS", "PROCEDURES_ICD", "PRESCRIPTIONS", "PATIENTS", "OUTPUTEVENTS", "NOTEEVENTS", "MICROBIOLOGYEVENTS", "LABEVENTS", "INPUTEVENTS_MV", "ICUSTAYS", "D_LABITEMS", "D_ITEMS", "D_ICD_PROCEDURES", "D_ICD_DIAGNOSES", "D_CPT", "DRGCODES", "DIAGNOSES_ICD", "DATETIMEEVENTS", "CPTEVENTS", "CHARTEVENTS", "CAREGIVERS", "CALLOUT", "ADMISSIONS"]
    }
}


all_rules = []



for source_name, source_info in data_sources.items():
    print(f"\nProcessing source: {source_name}")
    base_path = source_info["path"]
    for table_name in source_info["tables"]:

        file_path = os.path.join(base_path, f"{table_name}.csv")
        
        print(f"  -> Reading {file_path}")
        

        rules_from_file = create_entity_rules_from_file(file_path, COLUMN_TO_NER_CATEGORY)
        
        if rules_from_file:
            all_rules.extend(rules_from_file)
            print(f"     Generated {len(rules_from_file)} rules from {table_name}.")

print(f"\nTotal rules generated from all files: {len(all_rules)}")

out_file = "rules_try_3.txt"
with open(out_file,"w") as file:
    # json.dump(target_rules, file)
    file.write(str(target_rules))

unique_rules = list(set(all_rules))
print(f"Total unique rules: {len(unique_rules)}")
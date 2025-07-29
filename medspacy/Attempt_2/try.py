


import pandas as pd

target_rules = []
def entity(inp_path):
    df = pd.read_csv(path)
    dataframe = df
    columns_to_use = df.columns.tolist()
    for column_name in columns_to_use:
        if column_name in dataframe.columns:


                    
            target_rules.append(column_name)
                
    
    
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
print(target_rules)


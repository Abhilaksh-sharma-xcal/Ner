import spacy
import medspacy
from medspacy.target_matcher import TargetRule
import os
import pandas as pd


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
    path = "D:/xcaliber/study/full_data/"
    path += i
    path +=".csv"
    entity(inp_path=path)


nlp = spacy.blank("en")

nlp.add_pipe("medspacy_pyrush", first=True)
nlp.add_pipe("medspacy_target_matcher") 


target_matcher = nlp.get_pipe("medspacy_target_matcher")
target_matcher.add(target_rules)


text = """
Return the final response as normal text",,Show me conditions for patient with ID 022ad6b0-4df4-f85f-efed-fc245f20ff74.,"Here are the medical and social conditions for the patient with ID 022ad6b0-4df4-f85f-efed-fc245f20ff74:
 1. Risk activity involvement (finding) Ã¹ SNOMED: 160968000 Ã¹ Active since 1980-01-24
 2. Received higher education (finding) Ã¹ SNOMED: 224299000 Ã¹ Active since 1981-01-29
 3. Chronic sinusitis (disorder) Ã¹ SNOMED: 40055000 Ã¹ Active since 1986-08-29
 4. Prediabetes (finding) Ã¹ SNOMED: 714628002 Ã¹ Active since 1991-02-14
 5. Anemia (disorder) Ã¹ SNOMED: 271737000 Ã¹ Active since 1994-02-17
 6. Body mass index 30+ - obesity (finding) Ã¹ SNOMED: 162864005 Ã¹ Active since 1994-02-17
 7. Victim of intimate partner abuse Ã¹ SNOMED: 706893006 Ã¹ From 2008-12-25 to 2023-02-02
 8. Has a criminal record (finding) Ã¹ SNOMED: 266948004 Ã¹ Active since 2011-01-20
 9. Stress (finding) Ã¹ SNOMED: 73595000 Ã¹ From 2012-12-06 to 2016-03-31, 2016-12-29 to 2019-01-10, and since 2020-01-16 (active)
 10. Full-time employment (finding) Ã¹ SNOMED: 160903007 Ã¹ 2014-12-18 to 2020-01-16, again active since 2021-01-21
 11. Social isolation (finding) Ã¹ SNOMED: 422650009 Ã¹ 2015-12-24 to 2016-03-31, 2019-01-10 to 2020-01-16
 12. Acute bronchitis (disorder) Ã¹ SNOMED: 10509002 Ã¹ 2016-03-22 to 2016-04-08
 13. Viral sinusitis (disorder) Ã¹ SNOMED: 444814009 Ã¹ 2016-08-24 to 2016-09-08, 2019-01-03 to 2019-01-12, 2024-12-20 to 2024-12-28
 14. Acute bacterial sinusitis (disorder) Ã¹ SNOMED: 75498004 Ã¹ 2017-02-14 to 2017-03-06
 15. Localized primary osteoarthritis of the hand Ã¹ SNOMED: 201834006 Ã¹ Active since 2019-04-03
 16. Gingivitis (disorder) Ã¹ SNOMED: 66383009 Ã¹ Episodes starting on 2020-01-16, 2022-01-27, 2023-02-02
 17. Gingival disease (disorder) Ã¹ SNOMED: 18718003 Ã¹ Since 2022-02-10 and 2023-02-16
 18. Medication review due (situation) Ã¹ SNOMED: 314529007 Ã¹ Multiple dates between 2015 and 2025
 19. Part-time employment (finding) Ã¹ SNOMED: 160904001 Ã¹ 2020-01-16 to 2021-01-21
 20. Sprain (morphologic abnormality) Ã¹ SNOMED: 384709000 Ã¹ 2024-07-06 to 2024-07-24
 21. Sprain of wrist (disorder) Ã¹ SNOMED: 70704007 Ã¹ 2024-07-06 to 2024-07-24
 22. Misuses drugs (finding) Ã¹ SNOMED: 361055000 Ã¹ Active since 2025-02-13
 If you would like more detail for any particular condition or would like to filter to current/active only, please let me know!","The following conditions are in the patient's medical record:
 
 1. Chronic sinusitis (active since 1986-08-29)
 2. Prediabetes (active since 1991-02-14)
 3. Anemia (active since 1994-02-17)
 4. Obesity (active since 1994-02-17)
 5. Stress (multiple episodes, currently active since 2020-01-16)
 6. Osteoarthritis of the hand (active since 2019-04-03)
 7. Gingivitis and gingival disease (multiple episodes, latest starting 2023)
 8. Drug misuse (active since 2025-02-13)
 9. Other medical/social findings: risk activity involvement, higher education, history of intimate partner abuse, criminal record, history of social isolation, employment details, past episodes of bronchitis, sinusitis (viral/bacterial), medication review due, and wrist sprain.
 
 Let me know if you want details/clarification for any specific condition.","Chronic sinusitis (DISEASE), 1986-08-29 (DATE), Prediabetes (DISEASE), 1991-02-14 (DATE), Anemia (DISEASE), 1994-02-17 (DATE), Obesity (DISEASE), 1994-02-17 (DATE), Stress (DISEASE), 2020-01-16 (DATE), Osteoarthritis of the hand (DISEASE), 2019-04-03 (DATE), Gingivitis and gingival disease (DISEASE), 2023 (DATE), Drug misuse (DISEASE), 2025-02-13 (DATE), risk activity involvement (SIGN_SYMPTOM), higher education (SIGN_SYMPTOM), history of intimate partner abuse (SIGN_SYMPTOM), criminal record (SIGN_SYMPTOM), history of social isolation (SIGN_SYMPTOM), employment details (SIGN_SYMPTOM), bronchitis (DISEASE), sinusitis (viral/bacterial) (DISEASE), medication review due (PROCEDURE), wrist sprain (DISEASE)","Here are the main conditions listed in the medical record for the patient:
 
 - Chronic sinusitis (ongoing since August 29, 1986)
 - Prediabetes (ongoing since February 14, 1991)
 - Anemia (ongoing since February 17, 1994)
 - Obesity, BMI over 30 (ongoing since February 17, 1994)
 - Stress, including multiple episodes, most recently active since January 16, 2020
 - Osteoarthritis of the hand (ongoing since April 3, 2019)
 - Gingivitis and other gum disease (multiple episodes, latest in 2023)
 - Drug misuse (noted as active since February 13, 2025)
 
"""

doc = nlp(text)
print("Extracted Entities:")
print(doc.ents)
for ent in doc.ents:
    print(f"Entity: '{ent.text}', Label: '{ent.label_}',{ent._.is_family},{ent._.is_hypothetical},{ent._.is_historical},{ent._.is_negated}")
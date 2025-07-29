import os
import pandas as pd
from medspacy.target_matcher import TargetRule
from collections import namedtuple
{
    # System Identifiers
    'id': 'SYSTEM_ID',
    'patient_id': 'SYSTEM_ID',
    'subject_id': 'SYSTEM_ID',
    'hadm_id': 'SYSTEM_ID',
    'icustay_id': 'SYSTEM_ID',
    'row_id': 'SYSTEM_ID',
    'template_id': 'SYSTEM_ID',
    'care_plan_id': 'SYSTEM_ID',
    'member_id': 'SYSTEM_ID',
    'organization_id': 'SYSTEM_ID',
    'problem_id': 'SYSTEM_ID',
    'diagnostic_report_id': 'SYSTEM_ID',
    'encounter_id': 'SYSTEM_ID',
    'linked_medication_statement_id': 'SYSTEM_ID',
    'medication_statement_id': 'SYSTEM_ID',
    'observation_id': 'SYSTEM_ID',
    'identifier': 'SYSTEM_ID',
    'cgid': 'SYSTEM_ID',
    'orderid': 'SYSTEM_ID',
    'linkorderid': 'SYSTEM_ID',
    'ticket_id_seq': 'SYSTEM_ID',
    'seq_num': 'SYSTEM_ID',
    'isolate_num': 'SYSTEM_ID',
    'conceptid': 'SYSTEM_ID',

    # Medical Conditions & Diagnoses
    'reaction': 'MEDICAL_CONDITION',
    'reaction_code': 'MEDICAL_CONDITION',
    'health_status': 'MEDICAL_CONDITION',
    'condition_code': 'MEDICAL_CONDITION',
    'condition_display': 'MEDICAL_CONDITION',
    'problem_code': 'MEDICAL_CONDITION',
    'problem_display': 'MEDICAL_CONDITION',
    'diagnosis': 'MEDICAL_CONDITION',
    'diagnosis_code': 'MEDICAL_CONDITION',
    'diagnosis_display': 'MEDICAL_CONDITION',
    'finding_code': 'MEDICAL_CONDITION',
    'finding_display': 'MEDICAL_CONDITION',
    'indication_name': 'MEDICAL_CONDITION',
    'indication_code': 'MEDICAL_CONDITION',
    'precondition_code': 'MEDICAL_CONDITION',
    'precondition_display': 'MEDICAL_CONDITION',
    'icd9_code': 'MEDICAL_CONDITION',
    'long_title': 'MEDICAL_CONDITION',
    'short_title': 'MEDICAL_CONDITION',
    'drg_code': 'MEDICAL_CONDITION',
    'drg_type': 'MEDICAL_CONDITION',

    # Medications & Treatments
    'substance': 'MEDICATION',
    'substance_code': 'MEDICATION',
    'vaccine_code': 'MEDICATION',
    'vaccine_display': 'MEDICATION',
    'supply_product_code': 'MEDICATION',
    'supply_product_display': 'MEDICATION',
    'medication_name': 'MEDICATION',
    'drug_vehicle_code': 'MEDICATION',
    'drug_vehicle_display': 'MEDICATION',
    'drug_type': 'MEDICATION',
    'drug': 'MEDICATION',
    'drug_name_poe': 'MEDICATION',
    'drug_name_generic': 'MEDICATION',
    'formulary_drug_cd': 'MEDICATION',
    'gsn': 'MEDICATION',
    'ndc': 'MEDICATION',
    'fluid': 'MEDICATION',
    'ab_name': 'MEDICATION',
    'ab_itemid': 'MEDICATION',

    # Medical Procedures
    'plan_code': 'PROCEDURE',
    'plan_display': 'PROCEDURE',
    'activity_code': 'PROCEDURE',
    'activity_display': 'PROCEDURE',
    'encounter_type': 'PROCEDURE',
    'code': 'PROCEDURE',
    'procedure_code': 'PROCEDURE',
    'procedure_display': 'PROCEDURE',
    'cpt_cd': 'PROCEDURE',
    'cpt_number': 'PROCEDURE',

    # Lab & Test Names
    'report_type': 'LAB_TEST',
    'report_code': 'LAB_TEST',
    'report_display': 'LAB_TEST',
    'result_code': 'LAB_TEST',
    'result_display': 'LAB_TEST',
    'observation_code': 'LAB_TEST',
    'observation_display': 'LAB_TEST',
    'component_code': 'LAB_TEST',
    'component_display': 'LAB_TEST',
    'itemid': 'LAB_TEST',
    'label': 'LAB_TEST',
    'loinc_code': 'LAB_TEST',
    'spec_type_desc': 'LAB_TEST',
    'org_name': 'LAB_TEST',

    # Measurements & Values
    'severity': 'MEASUREMENT',
    'severity_code': 'MEASUREMENT',
    'age_at_onset_value': 'MEASUREMENT',
    'age_at_onset_unit': 'MEASUREMENT',
    'result_value': 'MEASUREMENT',
    'result_unit': 'MEASUREMENT',
    'interpretation': 'MEASUREMENT',
    'dose_value': 'MEASUREMENT',
    'dose_unit': 'MEASUREMENT',
    'repeat_number': 'MEASUREMENT',
    'quantity': 'MEASUREMENT',
    'dose_amount': 'MEASUREMENT',
    'rate_value': 'MEASUREMENT',
    'rate_unit': 'MEASUREMENT',
    'value_numeric': 'MEASUREMENT',
    'value_unit': 'MEASUREMENT',
    'component_value': 'MEASUREMENT',
    'component_unit': 'MEASUREMENT',
    'value': 'MEASUREMENT',
    'valueuom': 'MEASUREMENT',
    'prod_strength': 'MEASUREMENT',
    'dose_val_rx': 'MEASUREMENT',
    'dose_unit_rx': 'MEASUREMENT',
    'form_val_disp': 'MEASUREMENT',
    'form_unit_disp': 'MEASUREMENT',
    'dilution_value': 'MEASUREMENT',
    'valuenum': 'MEASUREMENT',
    'amount': 'MEASUREMENT',
    'amountuom': 'MEASUREMENT',
    'rate': 'MEASUREMENT',
    'rateuom': 'MEASUREMENT',
    'totalamount': 'MEASUREMENT',
    'totalamountuom': 'MEASUREMENT',
    'originalamount': 'MEASUREMENT',
    'originalrate': 'MEASUREMENT',

    # Personal & Demographic Info
    'prefix': 'PERSONAL_INFO',
    'given_name': 'PERSONAL_INFO',
    'family_name': 'PERSONAL_INFO',
    'telecom_value': 'PERSONAL_INFO',
    'gender': 'PERSONAL_INFO',
    'dob': 'PERSONAL_INFO',
    'dod': 'PERSONAL_INFO',
    'dod_hosp': 'PERSONAL_INFO',
    'dod_ssn': 'PERSONAL_INFO',
    'language': 'PERSONAL_INFO',
    'religion': 'PERSONAL_INFO',
    'marital_status': 'PERSONAL_INFO',
    'ethnicity': 'PERSONAL_INFO',
    'patientweight': 'PERSONAL_INFO',
    'performer_name': 'PERSONAL_INFO',
    'performer_prefix': 'PERSONAL_INFO',
    'performer_given': 'PERSONAL_INFO',
    'performer_family': 'PERSONAL_INFO',
    'author_prefix': 'PERSONAL_INFO',
    'author_given': 'PERSONAL_INFO',
    'author_family': 'PERSONAL_INFO',

    # Location Information
    'address_street': 'LOCATION_INFO',
    'address_city': 'LOCATION_INFO',
    'address_state': 'LOCATION_INFO',
    'address_postal_code': 'LOCATION_INFO',
    'address_country': 'LOCATION_INFO',
    'address_line': 'LOCATION_INFO',
    'organization_name': 'LOCATION_INFO',
    'organization_telecom_value': 'LOCATION_INFO',
    'organization_street': 'LOCATION_INFO',
    'organization_city': 'LOCATION_INFO',
    'organization_state': 'LOCATION_INFO',
    'organization_postal_code': 'LOCATION_INFO',
    'organization_country': 'LOCATION_INFO',
    'location_name': 'LOCATION_INFO',
    'location_street': 'LOCATION_INFO',
    'location_city': 'LOCATION_INFO',
    'location_state': 'LOCATION_INFO',
    'location_postal_code': 'LOCATION_INFO',
    'location_country': 'LOCATION_INFO',
    'performer_street': 'LOCATION_INFO',
    'performer_city': 'LOCATION_INFO',
    'performer_state': 'LOCATION_INFO',
    'performer_postal_code': 'LOCATION_INFO',
    'performer_country': 'LOCATION_INFO',
    'location_code': 'LOCATION_INFO',
    'location_display': 'LOCATION_INFO',
    'prev_careunit': 'LOCATION_INFO',
    'curr_careunit': 'LOCATION_INFO',
    'prev_wardid': 'LOCATION_INFO',
    'curr_wardid': 'LOCATION_INFO',
    'location': 'LOCATION_INFO',
    'first_careunit': 'LOCATION_INFO',
    'last_careunit': 'LOCATION_INFO',
    'first_wardid': 'LOCATION_INFO',
    'last_wardid': 'LOCATION_INFO',
    'submit_wardid': 'LOCATION_INFO',
    'submit_careunit': 'LOCATION_INFO',
    'callout_wardid': 'LOCATION_INFO',
    'discharge_wardid': 'LOCATION_INFO',
    'admission_location': 'LOCATION_INFO',
    'discharge_location': 'LOCATION_INFO',

    # Date & Time
    'onset_date': 'DATE_TIME',
    'end_date': 'DATE_TIME',
    'created_at': 'DATE_TIME',
    'effective_time_center': 'DATE_TIME',
    'effective_time_low': 'DATE_TIME',
    'effective_time_high': 'DATE_TIME',
    'effective_date': 'DATE_TIME',
    'encounter_date': 'DATE_TIME',
    'diagnosis_date': 'DATE_TIME',
    'problem_date': 'DATE_TIME',
    'finding_date': 'DATE_TIME',
    'immunization_date': 'DATE_TIME',
    'effective_start': 'DATE_TIME',
    'effective_end': 'DATE_TIME',
    'start_date': 'DATE_TIME',
    'birth_date': 'DATE_TIME',
    'effective_time': 'DATE_TIME',
    'intime': 'DATE_TIME',
    'outtime': 'DATE_TIME',
    'starttime': 'DATE_TIME',
    'endtime': 'DATE_TIME',
    'storetime': 'DATE_TIME',
    'startdate': 'DATE_TIME',
    'enddate': 'DATE_TIME',
    'chartdate': 'DATE_TIME',
    'charttime': 'DATE_TIME',
    'createtime': 'DATE_TIME',
    'updatetime': 'DATE_TIME',
    'acknowledgetime': 'DATE_TIME',
    'outcometime': 'DATE_TIME',
    'firstreservationtime': 'DATE_TIME',
    'currentreservationtime': 'DATE_TIME',
    'admittime': 'DATE_TIME',
    'dischtime': 'DATE_TIME',
    'deathtime': 'DATE_TIME',
    'edregtime': 'DATE_TIME',
    'edouttime': 'DATE_TIME',

    # Financial Info
    'insurance': 'FINANCIAL',
    'costcenter': 'FINANCIAL',

    # Metadata & Other System Info
    'substance_system': 'METADATA',
    'reaction_system': 'METADATA',
    'severity_system': 'METADATA',
    'status': 'METADATA',
    'status_code': 'METADATA',
    'status_system': 'METADATA',
    'plan_system': 'METADATA',
    'plan_system_name': 'METADATA',
    'title': 'METADATA',
    'goal': 'METADATA',
    'mood_code': 'METADATA',
    'class_code': 'METADATA',
    'activity_root': 'METADATA',
    'activity_extension': 'METADATA',
    'activity_system': 'METADATA',
    'activity_system_name': 'METADATA',
    'instruction_text': 'METADATA',
    'instruction_status': 'METADATA',
    'member_type': 'METADATA',
    'telecom_use': 'METADATA',
    'organization_telecom_use': 'METADATA',
    'description': 'METADATA',
    'health_status_code': 'METADATA',
    'health_status_system': 'METADATA',
    'health_status_display': 'METADATA',
    'status_observation_code': 'METADATA',
    'status_observation_system': 'METADATA',
    'status_observation_display': 'METADATA',
    'report_system': 'METADATA',
    'report_system_name': 'METADATA',
    'result_system': 'METADATA',
    'result_system_name': 'METADATA',
    'interpretation_code': 'METADATA',
    'interpretation_system': 'METADATA',
    'reference_range_text': 'METADATA',
    'reference_range_low': 'METADATA',
    'reference_range_high': 'METADATA',
    'reference_range_unit': 'METADATA',
    'extension_code': 'METADATA',
    'code_system': 'METADATA',
    'code_system_version': 'METADATA',
    'performer_extension': 'METADATA',
    'performer_role_code': 'METADATA',
    'performer_role_system': 'METADATA',
    'performer_role_name': 'METADATA',
    'location_service_code': 'METADATA',
    'location_service_system': 'METADATA',
    'location_service_name': 'METADATA',
    'diagnosis_system': 'METADATA',
    'diagnosis_status': 'METADATA',
    'problem_system': 'METADATA',
    'problem_status': 'METADATA',
    'finding_system': 'METADATA',
    'finding_status': 'METADATA',
    'vaccine_system': 'METADATA',
    'vaccine_original_text': 'METADATA',
    'manufacturer': 'METADATA',
    'education': 'METADATA',
    'supply_product_system': 'METADATA',
    'performer_telecom': 'METADATA',
    'author_family': 'METADATA',
    'fill_instructions': 'METADATA',
    'dose_form': 'METADATA',
    'dose_route': 'METADATA',
    'frequency_interval': 'METADATA',
    'frequency_unit': 'METADATA',
    'duration_days': 'METADATA',
    'directions': 'METADATA',
    'manufacturer_name': 'METADATA',
    'performer_organization': 'METADATA',
    'drug_vehicle_system': 'METADATA',
    'indication_system': 'METADATA',
    'precondition_system': 'METADATA',
    'observation_type': 'METADATA',
    'observation_root': 'METADATA',
    'observation_extension': 'METADATA',
    'observation_system': 'METADATA',
    'text_reference': 'METADATA',
    'value_code': 'METADATA',
    'value_system': 'METADATA',
    'value_display': 'METADATA',
    'component_system': 'METADATA',
    'name_use': 'METADATA',
    'marital_status_code': 'METADATA',
    'marital_status_display': 'METADATA',
    'marital_status_system': 'METADATA',
    'telecom_system': 'METADATA',
    'procedure_root': 'METADATA',
    'procedure_extension': 'METADATA',
    'procedure_system': 'METADATA',
    'procedure_system_name': 'METADATA',
    'original_text_ref': 'METADATA',
    'priority_code': 'METADATA',
    'priority_system': 'METADATA',
    'priority_display': 'METADATA',
    'target_site_code': 'METADATA',
    'target_site_system': 'METADATA',
    'target_site_display': 'METADATA',
    'performer_org_name': 'METADATA',
    'location_system': 'METADATA',
    'questionnaire_code': 'METADATA',
    'questionnaire_system': 'METADATA',
    'questionnaire_system_name': 'METADATA',
    'questionnaire_display': 'METADATA',
    'text_content': 'METADATA',
    'dbsource': 'METADATA',
    'eventtype': 'METADATA',
    'los': 'METADATA',
    'locationcategory': 'METADATA',
    'ordercategoryname': 'METADATA',
    'secondaryordercategoryname': 'METADATA',
    'ordercategorydescription': 'METADATA',
    'isopenbag': 'METADATA',
    'continueinnextdept': 'METADATA',
    'cancelreason': 'METADATA',
    'statusdescription': 'METADATA',
    'comments_editedby': 'METADATA',
    'comments_canceledby': 'METADATA',
    'comments_date': 'METADATA',
    'expire_flag': 'METADATA',
    'stopped': 'METADATA',
    'newbottle': 'METADATA',
    'iserror': 'METADATA',
    'category': 'METADATA',
    'text': 'METADATA',
    'spec_itemid': 'METADATA',
    'org_itemid': 'METADATA',
    'dilution_text': 'METADATA',
    'dilution_comparison': 'METADATA',
    'flag': 'METADATA',
    'ordercomponenttypedescription': 'METADATA',
    'abbreviation': 'METADATA',
    'linksto': 'METADATA',
    'unitname': 'METADATA',
    'param_type': 'METADATA',
    'sectionrange': 'METADATA',
    'sectionheader': 'METADATA',
    'subsectionrange': 'METADATA',
    'subsectionheader': 'METADATA',
    'codesuffix': 'METADATA',
    'mincodeinsubsection': 'METADATA',
    'maxcodeinsubsection': 'METADATA',
    'drg_severity': 'METADATA',
    'drg_mortality': 'METADATA',
    'warning': 'METADATA',
    'error': 'METADATA',
    'resultstatus': 'METADATA',
    'cpt_suffix': 'METADATA',
    'callout_service': 'METADATA',
    'request_tele': 'METADATA',
    'request_resp': 'METADATA',
    'request_cdiff': 'METADATA',
    'request_mrsa': 'METADATA',
    'request_vre': 'METADATA',
    'callout_status': 'METADATA',
    'callout_outcome': 'METADATA',
    'acknowledge_status': 'METADATA',
    'admission_type': 'METADATA',
    'hospital_expire_flag': 'METADATA',
    'has_chartevents_data': 'METADATA',
    'problem_class_code': 'METADATA',
    'problem_mood_code': 'METADATA',
    'problem_status_code': 'METADATA',
    'problem_effective_time_low': 'METADATA',
    'problem_value_code': 'METADATA',
    'problem_value_system': 'METADATA',
    'problem_value_display': 'METADATA',
    'problem_extension': 'METADATA',
    'problem_template_id': 'METADATA'
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
    file.write(str(all_rules))

unique_rules = list(set(all_rules))
print(f"Total unique rules: {len(unique_rules)}")
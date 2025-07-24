import pandas as pd
import json


input_csv_file = r"D:\xcaliber\study\data\data_agent_logs - structured_logs_1.csv" 


output_json_file = 'converted_data_1.json'
all_records = []


print(f"Reading data from '{input_csv_file}'...")

try:
    # Read the CSV into a pandas DataFrame
    df = pd.read_csv(input_csv_file)
    df = df.astype(object).where(pd.notna(df), None)
except FileNotFoundError:
    print(f"ERROR: The file '{input_csv_file}' was not found. Please check the file name.")
    exit()


for index, row in df.iterrows():

    json_record = {
            'patient': row['patient'],
            'Orchestrator Input': row['Orchestrator Input'],
            'Data Navigator Input': row['Data Navigator Input'],
            'Data Navigator Output': row['Data Navigator Output'],
            'Annotation Agent Input': row['Annotation Agent Input'],
            'Annotation Agent Output': row['Annotation Agent Output'],
            'Final Response(orchestrator)': row['Final Response(orchestrator)'],
        }
    all_records.append(json_record)

with open(output_json_file, 'w') as outfile:

    json.dump(all_records, outfile, indent=2) 

print(f"✅ Success! Data converted and saved to '{output_json_file}'.")
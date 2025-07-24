import json
import re

# Define the input and output file names
input_filename = r"D:\xcaliber\study\output.json"
output_filename = "cleaned_output.json"

# Open the input file to read and the output file to write
with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
    # Process each line in the original file
    for line in infile:
        # Skip any blank lines
        if not line.strip():
            continue
        
        # Load the line of text as a JSON object (a dictionary)
        data = json.loads(line)
        
        # --- Your cleaning logic ---
        # 1. Clean the patient name
        clean_patient_name = data.get("patient", "").replace('"', '')

        # 2. Extract annotations from the final response
        final_response_str = data.get("Final Response(orchestrator)", "")
        clean_annotations = []
        match = re.search(r'(\[.*\])$', final_response_str)
        if match:
            annotations_str = match.group(1)
            try:
                # Parse the extracted string into a list
                clean_annotations = json.loads(annotations_str)
            except json.JSONDecodeError:
                # Handle cases where the extracted string isn't valid JSON
                print(f"Could not parse annotations for: {clean_patient_name}")
        
        # 3. Create the clean dictionary
        clean_data = {
            "patient": clean_patient_name,
            "annotations": clean_annotations
        }
        
        outfile.write(json.dumps(clean_data) + '\n')

print(f"Processing complete. Clean data saved to '{output_filename}'.")
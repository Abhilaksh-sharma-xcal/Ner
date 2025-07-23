import re

# Raw data from your input
detected_raw = """
Entity: documented | Label: ENTITY
Entity: conditions | Label: ENTITY
Entity: findings | Label: ENTITY
Entity: patient | Label: ENTITY
Entity: Stress | Label: ENTITY
Entity: multiple entries | Label: ENTITY
Entity: years | Label: ENTITY
Entity: Severe | Label: ENTITY
Entity: anxiety | Label: ENTITY
Entity: panic | Label: ENTITY
Entity: Social isolation | Label: ENTITY
Entity: Acute bronchitis | Label: ENTITY
Entity: Acute | Label: ENTITY
Entity: viral pharyngitis | Label: ENTITY
Entity: Viral sinusitis | Label: ENTITY
Entity: episodes | Label: ENTITY
Entity: Victim | Label: ENTITY
Entity: intimate partner abuse | Label: ENTITY
Entity: Medication review | Label: ENTITY
Entity: periods | Label: ENTITY
Entity: Employment | Label: ENTITY
Entity: educational statuses | Label: ENTITY
Entity: part-time | Label: ENTITY
Entity: full-time employment | Label: ENTITY
Entity: labor force | Label: ENTITY
Entity: educationthese | Label: ENTITY
Entity: social context | Label: ENTITY
Entity: health record | Label: ENTITY
"""

truth_raw = """
Entity: finding | Label: ENTITY
Entity: finding | Label: ENTITY
Entity: anxiety | Label: ENTITY
Entity: panic | Label: ENTITY
Entity: finding | Label: ENTITY
Entity: Medication review | Label: ENTITY
Entity: Part-time employment | Label: ENTITY
Entity: finding | Label: ENTITY
Entity: Medication review | Label: ENTITY
Entity: Viral sinusitis | Label: ENTITY
Entity: disorder | Label: ENTITY
Entity: higher | Label: ENTITY
Entity: education | Label: ENTITY
Entity: finding | Label: ENTITY
Entity: Victim | Label: ENTITY
Entity: intimate partner abuse | Label: ENTITY
Entity: finding | Label: ENTITY
Entity: Viral sinusitis | Label: ENTITY
Entity: disorder | Label: ENTITY
Entity: Acute bronchitis | Label: ENTITY
Entity: disorder | Label: ENTITY
Entity: Acute viral pharyngitis | Label: ENTITY
Entity: disorder | Label: ENTITY
Entity: Social isolation | Label: ENTITY
Entity: finding | Label: ENTITY
Entity: labor force | Label: ENTITY
Entity: finding | Label: ENTITY
Entity: Full-time employment | Label: ENTITY
Entity: finding | Label: ENTITY
Entity: Full-time employment | Label: ENTITY
Entity: finding | Label: ENTITY
"""

def parse_entities(raw_text):
    """Parses the raw text to extract a clean list of entities."""
    entities = []
    # Regex to find text between "Entity:" and "|"
    matches = re.findall(r'Entity:\s*(.*?)\s*\|', raw_text)
    for entity in matches:
        # Clean up: lowercase and remove leading/trailing whitespace
        clean_entity = entity.strip().lower()

        if clean_entity != 'finding':
            entities.append(clean_entity)

    return sorted(list(set(entities)))


detected_entities = parse_entities(detected_raw)
truth_entities = parse_entities(truth_raw)

print("--- Cleaned and Unique Entities ---")
print(f"Detected ({len(detected_entities)}): {detected_entities}")
print(f"Truth ({len(truth_entities)}): {truth_entities}")
print("-" * 35)


detected_set = set(detected_entities)
truth_set = set(truth_entities)


true_positives = detected_set.intersection(truth_set)
false_positives = detected_set.difference(truth_set)
false_negatives = truth_set.difference(detected_set)

TP = len(true_positives)
FP = len(false_positives)
FN = len(false_negatives)

print("\n--- Performance Evaluation (Strict, Case-Insensitive Match) ---")
print(f"True Positives (TP): {TP}")
print(f"  {sorted(list(true_positives))}\n")

print(f"False Positives (FP): {FP} (Detected but not in Truth)")
print(f"  {sorted(list(false_positives))}\n")

print(f"False Negatives (FN): {FN} (In Truth but not Detected)")
print(f"  {sorted(list(false_negatives))}\n")

# 4. Calculate Precision, Recall, and F1-Score
precision = TP / (TP + FP) if (TP + FP) > 0 else 0
recall = TP / (TP + FN) if (TP + FN) > 0 else 0
f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

print("--- Metrics ---")
print(f"Precision: {precision:.2%}")
print(f"Recall:    {recall:.2%}")
print(f"F1-Score:  {f1_score:.2%}")
print("-" * 35)
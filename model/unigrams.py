from collections import Counter
import re
import pandas as pd
import spacy


nlp = spacy.load("en_core_web_sm")


csv_file = r"D:\xcaliber\study\condition_03c5.csv"
df = pd.read_csv(csv_file)

expected = " ".join(df['description'].tolist())
print(expected)
agent = """
Here are the documented conditions and significant findings for this patient: - Stress (multiple entries, including 2022-2025 and earlier years)
 - Severe anxiety (panic) (2013-2019)
 - Social isolation (2019-2021)
 - Acute bronchitis (June 2021)
 - Acute viral pharyngitis (January 2017)
 - Viral sinusitis (multiple episodes: Feb 2019, Dec 2021)
 - Victim of intimate partner abuse (2013-2016)
 - Medication review due (various periods, including currently as of 2025)
 - Employment and educational statuses (part-time, full-time employment; not in labor force; higher educationùthese provide social context to the health record)


"""


def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

def clean_and_lemmatize(text):
    text = text.lower()
    text = re.sub(r'[\(\)\[\]\{\},.;:]', '', text)
    doc = nlp(text)
    print(doc)
    return [token.lemma_ for token in doc if not token.is_stop and not token.is_punct and token.text.strip() != ""]


def rouge_1(candidate, reference):

    agent_tokens = clean_and_lemmatize(candidate)
    expected_tokens = clean_and_lemmatize(reference)

    print("agent_tokens\n",agent_tokens)
    print("expected_tokens\n",agent_tokens)

    cand_counts = Counter(agent_tokens)
    expected_counts = Counter(expected_tokens)


    overlap = sum(min(cand_counts[word], expected_counts[word]) for word in cand_counts if word in expected_counts)


    recall = overlap / len(expected_tokens) if expected_tokens else 0.0
    precision = overlap / len(agent_tokens) if agent_tokens else 0.0
    f1_score = (2 * precision * recall) / (precision + recall) if precision + recall > 0 else 0.0

    return {
        "rouge-1": {
            "precision": precision,
            "recall": recall,
            "f1": f1_score
        }
    }



scores = rouge_1(agent, expected)
print(scores)
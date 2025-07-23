import re

# Dictionaries and Rule Sets
PRONOUNS = {
    'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us',
    'them', 'who', 'what', 'which', 'myself', 'yourself'
}
DETERMINERS = {'a', 'an', 'the', 'my', 'your', 'his', 'her', 'its', 'our', 'their'}
NOUN_SUFFIXES = ['tion', 'ment', 'ness', 'ity', 'er', 'ist', 'ism']
COMMON_NOUNS = {'friend', 'car', 'city', 'idea', 'work', 'home', 'world', 'health', 'patient', 'abuse', 'review'}

# STOP LIST: Words that are often mis-tagged as nouns by our simple rules
ADJECTIVE_STOP_LIST = {'severe', 'social', 'acute', 'viral', 'earlier', 'higher', 'documented'}


def improved_find_nouns_and_pronouns(text):
    words = re.findall(r'\b\w+\b', text)
    results = []
    
    # Get the indices of words that start a sentence (first word, or word after a period)
    sentence_starts = {0}
    for i, word in enumerate(words[:-1]):
        if word.endswith('.'):
            sentence_starts.add(i + 1)

    for i, word in enumerate(words):
        lower_word = word.lower()
        tag = None

        if lower_word in ADJECTIVE_STOP_LIST:
            continue

        if lower_word in PRONOUNS:
            tag = 'PRONOUN'
        
        elif lower_word in COMMON_NOUNS:
            tag = 'NOUN'
        
        elif any(lower_word.endswith(suffix) for suffix in NOUN_SUFFIXES):
            tag = 'NOUN'
            
        elif i > 0 and words[i-1].lower() in DETERMINERS:
            tag = 'NOUN'
            

        elif word.istitle() and i not in sentence_starts:
            if lower_word in {'january', 'february', 'march', 'april', 'may', 'june', 
                              'july', 'august', 'september', 'october', 'november', 'december',
                              'jan', 'feb', 'dec'}:
                 tag = 'PROPER NOUN (Month)'
            else:
                 if lower_word not in PRONOUNS and not any(lower_word.endswith(s) for s in ['ly', 'al']):
                    tag = 'NOUN'

        if tag:
            results.append((word, tag))
            
    return results

# --- Example Usage with your text ---
text_to_analyze = """
Here are the documented conditions and significant findings for this patient: 
- Stress (multiple entries, including 2022-2025 and earlier years)
- Severe anxiety (panic) (2013-2019)
- Social isolation (2019-2021)
- Acute bronchitis (June 2021)
- Acute viral pharyngitis (January 2017)
- Viral sinusitis (multiple episodes: Feb 2019, Dec 2021)
- Victim of intimate partner abuse (2013-2016)
- Medication review due (various periods, including currently as of 2025)
- Employment and educational statuses (part-time, full-time employment; not in labor force; higher educationùthese provide social context to the health record)
"""

identified_words = improved_find_nouns_and_pronouns(text_to_analyze)

print("text_ analyze")
for word, tag in identified_words:
    print(f"- '{word}' -> {tag}")
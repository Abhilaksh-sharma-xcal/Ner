import nltk
from nltk.corpus import brown
from nltk.tokenize import word_tokenize
from nltk.tag import map_tag

text = """The search was performed for the patient with ID 022ad6b0-4df4-f85f-efed-fc245f20ff74, focusing specifically on allergy records.
 
 The Data-Navigator-Agent reported: ""There are no recorded allergies for the patient with patient_id: 022ad6b0-4df4-f85f-efed-fc245f20ff74.""
 
 This means that, in the current medical record for this patient, there are no documented allergies to medications, foods, or other substances.
 </think>
 
 Final response:
 
 There are no recorded allergies in the medical chart for this patient.
 
 [{""text"":""no recorded allergies"",""label"":""NEGATION"",""start"":10,""end"":30,""category"":""MEDICAL"",""terminology"":""SNOMEDCT"",""code"":""137650007""}]"""

nltk.download('universal_tagset')
nltk.download('brown')

tagged_words = brown.tagged_words(categories='news')
sample = tagged_words[:10]


mapped = [(word, map_tag('brown', 'universal', tag)) for word, tag in sample]
print(mapped)

default_tagger = nltk.DefaultTagger('NN')


patterns = [
    (r'.*ing$', 'VBG'),               # Gerunds
    (r'.*\d.*', 'CD'),                # Cardinal numbers
    (r'.*:', 'ID'),                   # Custom identifier tag
    (r'.*', 'NN')                     # Default to noun for this tagger
]
regexp_tagger = nltk.RegexpTagger(patterns, backoff=default_tagger)


train_sents = brown.tagged_sents(categories='news')[:5000]
lookup_tagger = nltk.UnigramTagger(train_sents, backoff=regexp_tagger)



words = word_tokenize(text)
tagged_words = lookup_tagger.tag(words)


terms = [{'text': word, 'pos': tag} for word, tag in tagged_words]
print(terms)


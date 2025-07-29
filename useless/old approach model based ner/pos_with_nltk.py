import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
def extract_terms_nltk(text):
    # stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    tagged = pos_tag(words)

    terms = []
    for word, tag in tagged:

        terms.append({
                'text': word,
                'pos': tag
        })
    return terms
var = """Show me allergies for the patient

 
 Search using this additional information: patient_id: 022ad6b0-4df4-f85f-efed-fc245f20ff74
 
  Return the final response as normal text"""
  
  
print(extract_terms_nltk("""Show me allergies for the patient

 
 Search using this additional information: patient_id: 022ad6b0-4df4-f85f-efed-fc245f20ff74
 
  Return the final response as normal text"""))

import numpy as np
import pandas as pd
import nltk
import spacy
import os

data = pd.read_json(r"D:\xcaliber\study\l1_ner\Corona2.json")
print(data.columns)
# print(df)
x = list(data['examples'][0].keys())
y = data['examples'][0]['content']
# print(x)
# print(y)


training_data = [{'text': example['content'],
                  'entities': [(annotation['start'], annotation['end'], annotation['tag_name'].upper())
                               for annotation in example['annotations']]}
                 for example in data['examples']]

print(training_data)
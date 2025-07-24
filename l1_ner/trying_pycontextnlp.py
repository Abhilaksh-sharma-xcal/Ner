import os
import pyConTextNLP.pyConText as pyConText
import pyConTextNLP.itemData as itemData
from pathlib import Path  
import yaml

sentence = "The patient has a history of diabetes but no evidence of cancer."

# --- SOLUTION: Convert the file path to a proper file URI ---

# 1. Define the path to your rules file
rules_file_path = r"D:\xcaliber\study\l1_ner\rules.yml"

# 2. Convert the standard path to a file URI that urlopen can understand
#    The pathlib library handles this conversion cleanly and correctly.
rules_uri = Path(rules_file_path).as_uri()

# The rules_uri will look like: 'file:///D:/xcaliber/study/l1_ner/rules.yml'
print(f"Loading rules from URI: {rules_uri}") # For debugging

# 3. Load the rules using the corrected URI
rules = itemData.get_items(rules_uri)

# --- END OF FIX ---

# 4. Create a ConTextMarkup object to store the results
markup = pyConText.ConTextMarkup()
markup.setRawText(sentence)

# 5. Apply the rules to the sentence
markup.markItems(rules, mode="yml")

# 6. Build and process the context graph
context = pyConText.ConTextGraph(markup)
context.prune_graph()
context.drop_inactive_modifiers()

# 7. Print the results
print(f"\nSentence: \"{sentence}\"\n")
print("Analysis Results:")
for node in context.nodes():
    if node.getCategory() == 'DISEASE':
        print(f"- Target: '{node.getLiteral()}'")
        modifiers = node.getModifierNodes()
        if modifiers:
            for modifier in modifiers:
                print(f"  - Context: '{modifier.getLiteral()}' ({modifier.getCategory()})")
        else:
            print("  - Context: Affirmed (no modifiers found)")
        print("-" * 20)


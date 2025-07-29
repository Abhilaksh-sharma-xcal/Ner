import json 
import pandas as pd

key_to_removed = "patient_annotated"
inp_file = r"D:\xcaliber\study\data\total_annotation.json"
out_file = r"x.json"




with open(r"D:\xcaliber\study\data\total_annotation.json") as inp:
    x = json.load(inp)

print(x)

out = []
for i in x:
    obj = {}
    for key in i:
        if key==key_to_removed:
            continue
        obj[key] = i[key]
        
    out.append(obj)

with open(out_file,"w") as file:
    json.dump(out,file, indent=2)
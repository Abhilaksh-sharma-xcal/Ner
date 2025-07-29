import pandas as pd


inp_file = r"D:\xcaliber\study\another_try_to_ner\files\another3.json"
out_file = "another3c.csv"


df = pd.read_json(inp_file)
print(df)
rs = df.to_csv(out_file,index=False)


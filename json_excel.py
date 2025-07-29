import pandas as pd


inp_file = "x1.json"
out_file = "try2.csv"


df = pd.read_json(inp_file)
print(df)
rs = df.to_csv(out_file,index=False)



# with open(out_file,"w") as file:
#     file.write(rs)
print(rs)
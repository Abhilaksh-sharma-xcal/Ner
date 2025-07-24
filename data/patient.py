import pandas as pd


df = pd.read_csv(r"D:\xcaliber\study\data\data_agent_logs - structured_logs_1.csv")
x = df.to_json("output.json", orient='records', lines= True)
print(df)
print(x)
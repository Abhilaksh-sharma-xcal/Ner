from datasets import load_dataset

ds = load_dataset("forwins/Drug-Review-Dataset", cache_dir=r"D:\xcaliber\study\try_3\new_files")


ds['train'].to_csv("train_data.csv")

# 2. Save the 'test' split to a JSON Lines file
ds['test'].to_csv("test_data.jsonl")

# 3. Save the 'train' split to a Parquet file
ds['train'].to_csv("train_data.csv")
# ds.sav
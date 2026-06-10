import pandas as pd
import glob
import os

print("Searching for Excel files...")

folder = "input_files"

files = glob.glob(os.path.join(folder, "*.xlsx"))

if not files:
    print("No Excel files found in input_files folder.")
    exit()

all_data = []

for file in files:
    print("Reading:", file)

    df = pd.read_excel(file)
    df["Source File"] = os.path.basename(file)

    all_data.append(df)

merged_df = pd.concat(all_data, ignore_index=True)

print("Rows before removing duplicates:", len(merged_df))

if "Customer ID" in merged_df.columns:
    merged_df = merged_df.drop_duplicates(subset=["Customer ID"])

print("Rows after removing duplicates:", len(merged_df))

merged_df.to_excel("merged_output.xlsx", index=False)

print("Done.")
print("Created file: merged_output.xlsx")
import polars as pl
import os
in_path = "/home/mstasky/.cache/kagglehub/datasets/kanakbaghel/hospital-management-dataset/versions/1/"
out_path = "data/"
# Load CSV file into a Polars DataFrame
#df = pl.read_csv(in_path + "appointments.csv")
# Check the structure
#print(df.head())
for filename in os.listdir(in_path):
    if filename.lower().endswith(".csv"):
        # Remove extension ".csv"
        name_without_ext = os.path.splitext(filename)[0]
        # read the file
        df = pl.read_csv(in_path + filename)
        # write it to parquent extension
        df.write_parquet(out_path + name_without_ext +".parquet")

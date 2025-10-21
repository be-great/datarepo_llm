from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, regexp_replace
from pathlib import Path

# --- 1️ Start Spark ---
spark = SparkSession.builder.appName("hospital-processing-auto").getOrCreate()

# --- 2️ Read all Parquet files in data/ ---
base = Path("data/")
parquet_files = list(base.glob("*.parquet"))
print(" Found files:", [f.name for f in parquet_files])

# Load each Parquet file into a dictionary of DataFrames
dfs = {f.stem: spark.read.parquet(str(f)) for f in parquet_files}

# --- 3️ Clean text columns & remove duplicates ---
for name, df in dfs.items():
    print(f"\n Cleaning table: {name}")
    # For every string column: lowercase + remove extra spaces
    for c, dtype in df.dtypes:
        if dtype == "string":
            df = df.withColumn(c, lower(regexp_replace(col(c), r"\s+", " ")))
    # Drop duplicates based on the first column if available
    if df.columns:
        df = df.dropDuplicates([df.columns[0]])
    dfs[name] = df
    print(f"✅ Cleaned {name}: {df.count()} rows")

# --- 4️ Join common tables (example: patients + appointments) ---
if "patients" in dfs and "appointments" in dfs:
    joined = dfs["appointments"].join(dfs["patients"], on="patient_id", how="inner")
    print(f"\n🔗 Joined patients + appointments → {joined.count()} rows")
else:
    # If no patient or appointment tables, merge all by union
    joined = None
    for i, (name, df) in enumerate(dfs.items()):
        if i == 0:
            joined = df
        else:
            joined = joined.unionByName(df, allowMissingColumns=True)
    print(f"\n🔗 Merged all tables vertically → {joined.count()} rows")

# --- 5️ Remove extra whitespace again globally ---
for c, dtype in joined.dtypes:
    if dtype == "string":
        joined = joined.withColumn(c, regexp_replace(col(c), r"\s+", " "))

# --- 6️ Save curated output ---
out_path = "data/hospital_curated.parquet"
joined.write.mode("overwrite").parquet(out_path)
print(f"\n✅ Curated dataset saved at: {out_path}")

# --- 7️ Stop Spark ---
spark.stop()
print(" Spark session stopped.")

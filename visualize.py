# hospital_api.py
# ----------------------------------------------------
# Serve a REST API that exposes DataRepo info for
# hospital_curated.parquet
# ----------------------------------------------------

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datarepo.core import ParquetTable, Catalog, ModuleDatabase
import polars as pl
import types
from pathlib import Path

# --- 1️- Register hospital_curated.parquet in DataRepo ---
data_path = Path("data/hospital_curated.parquet/part-00000-bdcc208c-401d-45d1-9ff2-1160cef2c641-c000.snappy.parquet").resolve()

hospital_table = ParquetTable(
    name="hospital_curated",
    uri=str(data_path),
    partitioning=[]
)
mod = types.SimpleNamespace(hospital_curated=hospital_table)
db = ModuleDatabase(mod)
catalog = Catalog({"hospital": db})

# --- 2️- Load dataset via Polars for stats/preview ---
df = pl.read_parquet(str(data_path))

# --- 3️- Create FastAPI app ---
app = FastAPI(title="Hospital DataRepo API")

@app.get("/")
def root():
    return {
        "message": "🏥 Hospital DataRepo API is running",
        "endpoints": ["/info", "/columns", "/preview"]
    }

@app.get("/info")
def get_info():
    """Return basic dataset metadata"""
    tbl = catalog.db("hospital").table("hospital_curated")
    info = {
        "dataset_name": tbl.name,
        "uri": tbl.uri,
        "rows": df.height,
        "columns": df.width,
        "path": str(data_path),
    }
    return JSONResponse(info)

@app.get("/columns")
def get_columns():
    """Return list of column names and data types"""
    schema = [{"column": c, "dtype": str(df[c].dtype)} for c in df.columns]
    return JSONResponse(schema)

@app.get("/preview")
def get_preview(limit: int = 10):
    """Return first few rows of dataset"""
    preview = df.head(limit).to_dicts()
    return JSONResponse(preview)

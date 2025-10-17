
# hospital_datarepo.py
# ------------------------------------------------------
# 1️⃣ Load hospital CSV datasets with DataRepo @table()
# 2️⃣ Create a catalog (metadata manager)
# 3️⃣ Optionally export a static web catalog
# ------------------------------------------------------

from datarepo.core import table, Catalog, ModuleDatabase
import polars as pl
import types
from pathlib import Path

# --- Paths ----------------------------------------------------
# Adjust if your dataset is in another location
base = Path("/home/mstasky/.cache/kagglehub/datasets/kanakbaghel/hospital-management-dataset/versions/1").resolve()
# --- 1️⃣ Define tables -----------------------------------------
@table()
def patients():
    """Load patients.csv as a DataRepo table"""
    return pl.read_csv(base / "patients.csv").lazy()

@table()
def doctors():
    """Load doctors.csv as a DataRepo table"""
    return pl.read_csv(base / "doctors.csv").lazy()

@table()
def appointments():
    """Load appointments.csv as a DataRepo table"""
    return pl.read_csv(base / "appointments.csv").lazy()

@table()
def treatments():
    """Load treatments.csv as a DataRepo table"""
    return pl.read_csv(base / "treatments.csv").lazy()

@table()
def billing():
    """Load billing.csv as a DataRepo table"""
    return pl.read_csv(base / "billing.csv").lazy()

# --- 2️⃣ Register tables in one ModuleDatabase -----------------
mod = types.SimpleNamespace(
    patients=patients,
    doctors=doctors,
    appointments=appointments,
    treatments=treatments,
    billing=billing,
)

db = ModuleDatabase(mod)
catalog = Catalog({"hospital": db})

# --- 3️⃣ Example: Preview a table ------------------------------
if __name__ == "__main__":
    tbl = catalog.db("hospital").table("patients")
    df = tbl.collect()
    print("✅ Patients table loaded successfully.")
    print("Rows:", len(df))
    print(df.head())
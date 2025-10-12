from datarepo.core import ParquetTable, Catalog, ModuleDatabase
from datarepo.export.web import export_and_generate_site
import types
from pathlib import Path

# Make sure the path is absolute
parquet_path = str(Path("data/reuters_parquet/reuters.parquet").resolve())

# ✅ FIXED: pass partitioning=[] and absolute URI
reuters_table = ParquetTable(
    name="reuters_finance",
    uri=parquet_path,
    partitioning=[],
)

# Register in a simple module and catalog
mod = types.SimpleNamespace(reuters_finance=reuters_table)
db  = ModuleDatabase(mod)
catalog = Catalog({"business": db})
# Generate static HTML files
export_and_generate_site(
    catalogs=[("business", catalog)],
    output_dir="site_out"   # directory for generated web files
)
# ✅ Verify data loading
if __name__ == "__main__":
    # tbl = catalog.db("business").table("reuters_finance")
    # df  = tbl.collect()
    # print("✅ Loaded rows:", len(df))
    # print(df.head())
    print("Open site_out/index.html")

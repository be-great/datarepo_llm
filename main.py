from datarepo.core import ParquetTable, Catalog, ModuleDatabase
from datarepo.export.web import export_and_generate_site
from pathlib import Path
import types

llm_table = ParquetTable(
    name="llm7_prompts",
    uri=str(Path("/home/mstasky/.cache/kagglehub/datasets/carlmcbrideellis/llm-7-prompt-training-dataset/versions/4/part-0003.parquet").resolve()),
    partitioning=[],
)

mod = types.SimpleNamespace(llm7_prompts=llm_table)
db = ModuleDatabase(mod)
catalog = Catalog({"llm": db})

export_and_generate_site(
    catalogs=[("llm", catalog)],
    output_dir="site_out"
)

print("✅ Site generated at site_out/")
print("🌐 Run: cd site_out && python -m http.server 8000")
print("Then open http://localhost:8000/")
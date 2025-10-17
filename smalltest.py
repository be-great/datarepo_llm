from datarepo.core import Catalog, ModuleDatabase
import my_table as tables
from datarepo.export.web import export_and_generate_site
from pathlib import Path
demo = Catalog({"demo": ModuleDatabase(tables)})

if __name__ == '__main__':
    supplier = demo.db("demo").supplier()
    part = demo.db("demo").part()
    out = Path("site_out")
    out.mkdir(exist_ok=True)
    export_and_generate_site(catalogs=[("demo", demo)], output_dir=str(out))
    print("Generated")
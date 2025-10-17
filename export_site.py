# export_site.py
from datarepo.export.web import export_and_generate_site
from hospital_catalog import catalog

export_and_generate_site(
    catalogs=[("hospital", catalog)],
    output_dir="site_out"
)

print("✅ Catalog website generated in site_out/")
print("Open site_out/index.html or serve via: python -m http.server -d site_out 5000")
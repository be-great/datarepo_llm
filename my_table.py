from datarepo.core import table
import polars as pl
import pandas as pd

def supplier_():
    data = {
        "keys":[1, 2 , 3, 4],
        "name":["supp1", "supp2", "supp3", "supp4"],
        "country":["sudan", "egypt", "turkish", "liba"],
    }
    return pd.DataFrame(data)
def part_():
    data = {
        "keys":[5, 6 , 7, 8],
        "name":["supp5", "supp6", "supp7", "supp8"],
        "country":["sudan1", "egypt1", "turkish1", "liba1"],
    }
    return pd.DataFrame(data)

@table(

    data_input = "supplier supplier",
    latency_info = "Static data",
)
def supplier():
    # convert to polars lazyframe for datarepo
    lf = pl.from_pandas(supplier_()).lazy()
    # force schema to include keys
    return lf.select(["keys", "name", "country"]).collect()
@table(

    data_input = "part supplier",
    latency_info = "part static data",
)
def part():
    # convert to polars lazyframe for datarepo
    lf = pl.from_pandas(part_()).lazy()
    return lf.select(["keys", "name", "country"]).collect()

# datarepo_llm


## install hospital managment datasets

```python
source ven/bin/activate
python3 download_dataset.py
```

## URL for the dataset
```bash
/home/username/.cache/kagglehub/datasets/kanakbaghel/hospital-management-dataset/versions/1
```

## Convert csv file to datarepo supported data type parquet
```bash
python3 csv_to_datarepo.py
```
## Create the hospital catalog
```bash
python3 hospital_catalog.py


```
## Initialization

```bash
./init.sh

```

## Navigate the datarepo

*you can navigate the datarepo using broswer by using the port 5000*
```bash
cd site_out
python3 -m http.server 5000
```

# Using pig 
## Pig modes 
### 🐷 Apache Pig Execution Modes

| **Pig Execution Mode** | **Command** | **Execution Engine** |
|-------------------------|--------------|-----------------------|
| **Local Mode** | `pig -x local` | Runs on your computer (single JVM) |
| **MapReduce Mode** | `pig -x mapreduce` | Runs on Hadoop cluster (via MapReduce engine) |
| **Tez Mode** *(optional)* | `pig -x tez` | Runs using Apache Tez DAG engine (faster than MapReduce) |
| **Spark Mode** *(experimental)* | `pig -x spark` | Runs using Apache Spark engine |


## exit the safe mode of name node
```bash
sudo -u hdfs hdfs dfsadmin leave
```


## execute pig script in hadoop cluster via mapreduce
```bash
pig -x mapreduce script.pig
```

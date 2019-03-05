# Databricks notebook source
# MAGIC %md using databricks cli to install cran libs on the cluster (drivers and workders together)
# MAGIC 
# MAGIC databricks libraries install --cluster-id 0518-154619-gamey181 --cran-package zoo

# COMMAND ----------

# MAGIC %sh
# MAGIC 
# MAGIC pwd

# COMMAND ----------

# MAGIC %r
# MAGIC library(xgboost)

# COMMAND ----------

print sc.master
print sc.pythonVer

# COMMAND ----------

# MAGIC %sh
# MAGIC wget https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data /tmp/uci_data.data
# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# dependencies = [
# ]
# ///

# COMMAND ----------
# DBTITLE 1,init

from databricks.sdk.runtime import spark
from src import s02_pipeline as p

# COMMAND ----------
# DBTITLE 1,load data
myclaims = spark.table("claims")

claims_df = p.load_claims(myclaims)
ratio = p.compute_loss_ratio(claims_df)
p.save_report(ratio, "report.txt")
print(f"Loss ratio: {ratio:.2%}")

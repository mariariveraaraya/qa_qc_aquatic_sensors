# Databricks notebook source
# MAGIC %md
# MAGIC #### Instructions
# MAGIC
# MAGIC - Change Location_code and/or measurement in the next cell.
# MAGIC - Click 'Run all'

# COMMAND ----------

Location_code = 'firebund2'
measurement = 'EC'

# COMMAND ----------

import os
import plotly.express as px

# COMMAND ----------

env = os.getenv('platform_env')
results=spark.read.parquet(f'abfss://lake-raw@etdllake{env}.dfs.core.windows.net/sensor_drift/inference')
results2 = results.filter((results.Location_code== f'{Location_code}') & (results.measurement== f'{measurement}'))
results3= results2.toPandas()

# COMMAND ----------

fig = px.scatter(results3, x="datetime", y="measurement_value", color = "measurement_quality_value")
fig.show()

# COMMAND ----------

results.groupBy("Location_code", "measurement").count().show()

# COMMAND ----------

results2.sort("datetime").display()

from pyspark.sql import functions as F

# Aggregations
df = df.groupBy('column').agg(F.count('*').alias('count'))
df = df.groupBy('column').agg(F.sum('amount').alias('totalAmount'))

# Basic Aggregations
df = df.agg(F.max('column').alias('max'))
df = df.agg(F.min('column').alias('min'))

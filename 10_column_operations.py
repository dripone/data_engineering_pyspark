# Add or rename a column
df = df.withColumn('new_column', F.lit('value'))
df = df.withColumnRenamed('old_name', 'new_name')

# Mathematical operations
df = df.withColumn('rounded', F.round('column', 2))
df = df.withColumn('absolute', F.abs('column'))

# Replace values in a column
df = df.replace(float("nan"), None)

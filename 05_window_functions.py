from pyspark.sql.window import Window

# Define a window
windowSpec = Window.partitionBy('column').orderBy('column2')

# Row number within window
df = df.withColumn('row_number', F.row_number().over(windowSpec))

# Running total within window
df = df.withColumn('running_total', F.sum('amount').over(windowSpec))

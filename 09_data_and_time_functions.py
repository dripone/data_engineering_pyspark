# Add a column with the current date and time
df = df.withColumn('current_date', F.current_date())
df = df.withColumn('current_timestamp', F.current_timestamp())

# Convert a string to a date 
df = df.withColumn('date_col', F.to_date('string_col', 'yyyy-MM-dd'))

# Convert a string to a timestamp
df = df.withColumn('ts_col', F.to_timestamp('string_col','yyyy-MM-dd HH:mm:ss'))

# Get number of days between two dates
df = df.withColumn('date_diff', F.datediff('end_date', 'start_date'))

# Get number of months between two dates
df = df.withColumn('months_between', F.months_between('date1', 'date2'))

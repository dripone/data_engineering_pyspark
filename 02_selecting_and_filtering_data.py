# Select columns
df = df.select('column1', 'column2')

# Filter rows
df = df.filter(df.column > 10)
df = df.filter(df.column.isNull()) 
df = df.filter(df.column.isNotNull())

# Drop duplicates
df = df.dropDuplicates()

# Drop a column
df = df.drop('column_name')

# Sort by a column
df = df.orderBy(df.column.asc())
df = df.orderBy(df.column.desc())

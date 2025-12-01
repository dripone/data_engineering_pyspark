# Create a SparkSession
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('your_app_name').getOrCreate()

# Load Data
df = spark.read.csv('/path/to/input.csv', header=True)  # CSV
df = spark.read.json('/path/to/input.json') 			# JSON
df = spark.read.parquet('/path/to/input.parquet')		# Parquet

# Show data
df.show(5)    # Show the first 5 rows
df.collect()  # Collect all rows (use with caution)

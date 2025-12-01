# Cache DataFrame in memory
df.cache()

# Remove DataFrame from memory
df.unpersist()

# Stop SparkSession
spark.stop()

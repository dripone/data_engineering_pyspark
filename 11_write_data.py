# Write DataFrame to different formats
df.write.csv('/path/to/output.csv', header=True) # CSV
df.write.json('/path/to/output.json')			 # JSON
df.write.parquet('/path/to/output.parquet')		 # Parquet

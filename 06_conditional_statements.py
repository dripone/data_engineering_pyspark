df = df.withColumn('status', F.when(df['column'] > 75, 'High')
                             .when(df['column'] > 50, 'Medium')
                             .otherwise('Low'))

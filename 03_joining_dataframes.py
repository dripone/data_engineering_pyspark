# Inner join
df = df1.join(df2, df1.id == df2.id, 'inner')

# Left join
df = df1.join(df2, df1.id == df2.id, 'left')

# Full outer join
df = df1.join(df2, df1.id == df2.id, 'outer')

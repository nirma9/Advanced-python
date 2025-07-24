#pandas components
import pandas as pd
# s = pd.Series([10,20,30,40])
# print(s)


#dataframe
data = {"Name":['riya','Ankit'],'Marks':[92,85]}
df = pd.DataFrame(data)
print(df)

#imp
# df = pd.read_csv("data.txt")

# print(df.head())
# print(df.tail())

# df.dropna()
# df.fillna()


high_scores = df[df['Marks']>90]
print(high_scores)

#grouping
print(df.groupby('Name')['Marks'].mean())

df1 = pd.DataFrame({'ID':[1,2],'Name':['A','B']})
df2 = pd.DataFrame({'ID':[1,2],'Markks':[90,95]})
merged = pd.merge(df1,df2, on = "ID")
print(merged)



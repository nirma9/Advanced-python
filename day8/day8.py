import pandas as pd
# data = {'City':['mumbai','delhi','mumbai','delhi'],'Year':[2020,2020,2021,2021],'Sales':[100,150,200,250]}
# df = pd.DataFrame(data)
# print(df)

# pivot_table = pd.pivot_table(df,values='Sales',index='City',columns='Year',aggfunc='sum')
# print(pivot_table)


df = pd.DataFrame({'name':['amit','riya'],'maths':[90,95],'science':[85,80]})


melted = pd.melt(df,id_vars=['name'],var_name='subject',value_name='Marks')
print(melted)

pivoted = melted.pivot(index = 'name',columns='subject',values='Marks')
print(pivoted)

#sales dashboard
data = {'city':['delhi','mumabi','delhi','mumabi','delhi'],'Month':["jan",'jan','feb','feb','mar'],
        'sales':[10000,15000,12000,17000,13000],'orders':[100,150,110,160,115]}

df = pd.DataFrame(data)
print(df)

#total sales per city
city_sales = df.groupby('city')['sales'].sum()
print(city_sales)

#average order vallue
df['Avgordervalue']= df['sales']/df['orders']
print(df[['city','Month','Avgordervalue']])

#city wise monthly pivot table

pivot = pd.pivot_table(df,values='sales',index='city',columns='Month',aggfunc='sum')
print(pivot)
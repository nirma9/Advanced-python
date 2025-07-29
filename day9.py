import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [10,20,30,40,50]
# plt.plot(x,y)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Simple line plot..")
# plt.grid(True)
# plt.show()



#bar chart
# x = ["Python","java","c++"]
# y = [90,60,70]
# plt.bar(x,y)
# plt.title("Language popularity")
# plt.xlabel("Languages")
# plt.ylabel("Popularity")
# plt.show()


#scatter plot
# x = [1,2,3,4]
# y = [1,3,2,4]
# plt.scatter(x,y)
# plt.title("Scatter Example")
# plt.xlabel("X-values")
# plt.ylabel("Y-values")
# plt.grid(True)
# plt.show()

import pandas as pd
data = {"year":[2019,2020,2021,2022],'sales':[120,150,170,200]}
df = pd.DataFrame(data)

plt.plot(df['year'],
df['sales'],marker = 'o')

plt.title("comapny sales over years")
plt.xlabel("Year")
plt.ylabel("sales")
plt.grid(True)
plt.show()
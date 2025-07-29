#ek screen pe multiple graphs   subplots
import matplotlib.pyplot as plt

x = [1,2,3,4]
y1 = [10,20,30,40]
y2 = [40,30,20,10]
# plt.subplot(1,2,1)
# plt.plot(x,y1)
# plt.title("First Graph")
# plt.subplot(1,2,2)
# plt.plot(x,y2,color = 'red')
# plt.title("Second paragraph")
# plt.tight_layout()
# plt.show()

#custom figure size
# plt.figure(figsize=(6,4),dpi = 100)
# plt.plot([1,2,3],[4,5,6])
# plt.title("custom sized graph")
# plt.show()


plt.plot(x,y1,label = 'product A',color = 'blue',linestyle= '--',marker = 'o')
plt.plot(x,y2,label = 'product B',color = 'green',linestyle = "-",marker = "o")
plt.title("comparision")
plt.xlabel("Quarter")
plt.ylabel("Revenue")
plt.legend()
plt.grid(True)
plt.show()
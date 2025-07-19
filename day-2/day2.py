# nums = [1,2,3,4]
# sq = {n: n*n for n in nums}
# print(sq)

# #dict from two list
# keys = ["a",'b','c']
# values = [10,20,30]
# res = {k:v for k,v in zip(keys,values)}
# print(res)

#with(if)
# nums = [1,2,3,4,5,6]
# evens = {n: n*n for n in nums if n % 2==0}
# print(evens)

#if- else:
# nums = [1,2,3,4,5]
# result = {n: 'Even' if n % 2 == 0 else 'ODD' for n in nums}
# print(result)

# cel = {"Delhi":30,'shimla':20,"mumbai":35}
# fah = {city :(temp * 9/5) + 32 for city , temp in cel.items()}
# print(fah)

#nested
table = {x: {y:x*y for y in range(1,4)} for x in range(1,4)}
print(table)
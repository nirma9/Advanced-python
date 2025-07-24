colors = ['red','blue','green']
it = iter(colors)
print(next(it))
print(next(it))
print(next(it))
# print(next(it))



#generator

# def num_greet():
#                yield 1
#                yield 2
#                yield 3
# g = num_greet()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))



# def read_file(filename):
#                with open(filename,'r') as file:
#                        for line in file:
#                                yield line.strip()
# for line in read_file("note.rtf"):
#         print(line)


# with open(r"data.txt",'r')as file:
#                content = file.read()
#                print(content)

#infinite fibannocai
def fib():
        a,b = 0,1
        while True:
               yield a
               a,b = b, a+b
fibonnacai = fib()
for _ in range(6):
        print(next(fibonnacai))


        #generator exp
        sq = (x *x for x in range(5))
        for i in sq:
                print(i)

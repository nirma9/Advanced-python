# def my_decorator(func):
#     def wrapper():
#         print("Before function runs")
#         func()
#         print("After function runs")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()


# #multiple decorators
# def bold_dec(func):
#                def wrapper():
#                        print("<b>", end = " ")
#                        func()
#                        print("<b>", end = "  ")
#                return wrapper
# def italic_dec(func):
#         def wrapper():
#                 print("<i>", end = " ")
#                 func()
#                 print("<i>", end = " ")
#         return wrapper
# @bold_dec
# @italic_dec
# def greet():
#         print("Hello", end = " ")

# greet()


#real world python 

#logging function calss automatically

def log_func(func):
               def wrapper(*args,**kwargs):
                       print(f"Function {func.__name__} called")
                       return func(*args,**kwargs)
               return wrapper

@log_func               
def add(a,b):
        return a+b
print(add(2,3))



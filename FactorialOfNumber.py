# 5! =  1*2*3*4*5

### Approch 1   loop
# factorial=1
# num=10
#
# if num<0:
#     print("factorial does not exist for negative numbers")
# elif num==0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print("the factorial of",num, "is",factorial)


### Approch 2  recursion

# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)   # 5 * 4 * 3 * 2 * 1
#
# num=5
# print("Factorial of",num,"is",factorial(num))
#

### or Ternary operator

# def factorial(n):
#     return 1 if (n==0 or n==1) else n* factorial(n-1)
# num=5
# print("Factorial of",num,"is",factorial(num))

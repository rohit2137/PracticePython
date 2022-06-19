## 0 1 1 2 3 5 8 13 21 34

### Approch 1  loop

# n1,n2=0,1
# print(n1)
# print(n2)
#
# for i in range(2,10):
#     sum=n1+n2
#     n1=n2
#     n2=sum
#     print(sum)

###  Approach 2   recursive

def fibonaci(n):

    if n<=0:
        print("incorrect input")
    elif n==1 or n==2:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)

print(fibonaci(9))    # 34
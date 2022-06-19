### Approach 1
# mylist=[1,2,3,5,6,8,7,0]
# ele=0
#
# if ele in mylist:
#     print("Element is present")
# else:
#     print("Element is not present")


### Approach 2
mylist=[1,2,3,5,6,8,7]
ele=0
flage=0
for i in mylist:
    if i==ele:
        print("element is present")
        flage=1
if flage==0:
    print("element is not present")


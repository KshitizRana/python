# Accept two integers a and b as input and print the absolute difference of both the numbers. For example, if a=9,b=8, then the absolute difference is 9-8=1.So, your output should be 1. You should be able to solve this problem using the concepts covered in this week.

a=int(input("Enter first int: "))
b=int(input("Enter second int: "))
if ((a-b)>=0):
    print((a-b))
else :
    print(-1*(a-b))
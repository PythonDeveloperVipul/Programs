def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    elif n<0:
        return "Negative Number Enter"
    return n*factorial(n-1)
    
n=int(input('Enter Number:'))
ans=factorial(n)
print(ans)

# import math
# print(math.factorial(5))

# Python 3 program to find
# factorial of given number

# def factorial(n):

# 	# single line to find factorial
# 	return 1 if (n==1 or n==0) else n * factorial(n - 1)


# # Driver Code
# num = int(input('Enter Number : '))
# print ("Factorial of",num,"is",
# 	factorial(num))

# This code is contributed
# by Smitha Dinesh Semwal.

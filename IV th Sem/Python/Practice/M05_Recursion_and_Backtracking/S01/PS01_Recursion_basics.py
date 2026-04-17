#Recursion : 
# Sum of n natural numbers:
#Traditional Approach
def sum_of_N(n):
    s = 0
    for i in range(1,n+1):
        s += i 
    return s
print(sum_of_N(5))#15
print(sum_of_N(10)) #55
# Recursive Apporach
def sum_of_N1(n):
    if n == 0:
        return 0
    return n + sum_of_N1(n-1)
print(sum_of_N1(6))
print(sum_of_N1(12))
# Factorial of a number
# Traditional Apporach
def Factorial1(n):
    fact = 1
    if n < 0:
        return "No Factorial - ves"
    else:
        for i in range(1,n+1):
            fact *= i
print(Factorial1(4))
#Recursive Apporach
def Factorial(n):
    if n < 0:
        return "no factorial -ves"
    elif n == 0 or n == 1:
        return 1 
    else:
        return n * Factorial(n-1)
print(Factorial(5))
print(Factorial(3))
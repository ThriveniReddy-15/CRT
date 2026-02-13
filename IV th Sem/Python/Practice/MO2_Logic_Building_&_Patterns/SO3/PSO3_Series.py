'''
Read  a and b and print the series of arithmetic progression
'''
a = int(input())
b = int(input())
d = 0
for i in range(1,10):
    d = a +(i*b)
    print(d,end=" ")


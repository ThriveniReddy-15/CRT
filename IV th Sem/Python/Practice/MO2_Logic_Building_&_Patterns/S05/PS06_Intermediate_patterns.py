#li = [1,2,3,4,5]
#output= [1,4,9,16,25]
#li = list(map(int,input().split()))
#res = []
#for i in li:
#    res.append(i ** 2)
#print(res)
# li = ['a','b','c']
#a,b,c
''' Intermediate Patterns
1.Pyramid
n = 4
Output:
    *
   * * 
  * * *
* *  *  *
'''
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
# * * * *
# * * *
#  * *
#   *
n = int(input())
for i in range(1,n+1):
    print()
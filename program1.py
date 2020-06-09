# Program to count occurrences of an element in a tuple:-

def countoccur(A, x):
   c = 0
   for i in A:
      if (i == x):
         c = c + 1
   return c


A=list()
n = int(input("Enter the size of tuple: "))
print("Enter the Element of tuple : ")
for i in range(int(n)):
   k = int(input(""))
   A.append(k)
n1 = int(input("Enter an element to count number of occurrences : "))
print("Number of Occurrences of ",n1,"is",countoccur(A, n1))
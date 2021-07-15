#Program to display fibonacci series up to a limit
n=int(input("Enter the limit:"))
x=0
y=1
z=1
print("Fibonacci Series")
print(x,y,end=' ')
while z<=n:
 print(z,end=' ')
 x=y
 y=z
 z=x+y

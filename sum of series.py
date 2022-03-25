#Find the sum of series; 2+22+222+...+ n terms.
n=int(input("Enter the number:"))
s=0
r=0
for x in range(0,n):
    r=r*10+2
    s+=r
print("The sum of series is",s)
input()

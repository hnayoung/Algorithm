n=int(input())
i=max(0,n-54)
while i+sum(map(int,str(i)))-n and i<n:i+=1
print(i%n)
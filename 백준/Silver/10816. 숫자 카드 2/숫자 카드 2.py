import sys
input =  sys.stdin.readline 

n_dict = {}
N = int(input().strip()) 
n_numbers = list(map(int, input().split()))
                
for num in n_numbers:
    if num in n_dict:
        n_dict[num]+=1
    else:
        n_dict[num]=1
                
M = int(input().strip())
m_numbers = list(map(int, input().split()))
result = []

for num in m_numbers:
    result.append(n_dict.get(num, 0))
                 
print(*result)
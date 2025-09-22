import sys
input = sys.stdin.readline

N = int(input().strip())
map_list = set(map(int, input().split()))  
M = int(input().strip())
map_list2 = list(map(int, input().split()))  

for x in map_list2:
    print(1 if x in map_list else 0)

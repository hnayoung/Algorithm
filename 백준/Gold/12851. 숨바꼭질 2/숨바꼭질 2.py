import sys 
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

MAX = 100001
dist = [-1]*MAX
count = [0]*MAX

q = deque([n])
dist[n] = 0
count[n] = 1

while q:
    cur = q.popleft()
    for nxt in (cur-1, cur+1, cur*2):
        if 0 <= nxt < MAX:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                count[nxt] = count[cur]
                q.append(nxt)
            elif dist[nxt] == dist[cur] + 1:
                count[nxt] += count[cur]
            
x = dist[k]
su = count[k]

print(x)
print(su)
from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split()) 
g = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
    
for i in range(1,N+1):
    g[i].sort()
    
def dfs(g,v,visited):
	visited[v] = True
	print(v, end =' ')	
	for i in g[v]:
		if not visited[i]:
			dfs(g, i, visited)
	

def bfs(g,v,visited):
	queue = deque([v])
	visited[v] = True
	
	while queue:
		v = queue.popleft()
		print(v, end=' ')
		for i in g[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True


visited = [False] * (N+1)
dfs(g,V,visited)
print()

visited = [False] * (N+1)
bfs(g,V,visited)
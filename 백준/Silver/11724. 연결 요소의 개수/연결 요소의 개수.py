import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 간선 입력
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

count = 0
for i in range(1, N+1):
    if not visited[i]:  # 방문 안 했으면 새 컴포넌트 발견
        dfs(i)
        count += 1

print(count)
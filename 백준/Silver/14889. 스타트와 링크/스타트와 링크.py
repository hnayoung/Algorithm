N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * N
ans = 1e9

def calc():
    start, link = 0, 0
    for i in range(N):
        for j in range(i+1, N):
            if visited[i] and visited[j]:
                start += S[i][j] + S[j][i]
            elif not visited[i] and not visited[j]:
                link += S[i][j] + S[j][i]
    return abs(start - link)

def dfs(idx, cnt):
    global ans
    if cnt == N // 2:
        ans = min(ans, calc())
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1
            dfs(i+1, cnt+1)
            visited[i] = 0

dfs(0, 0)
print(ans)
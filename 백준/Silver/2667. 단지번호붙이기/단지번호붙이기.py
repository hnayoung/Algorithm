import sys

sys.setrecursionlimit(3000)

def dfs(x, y, n, graph):
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0
    
    if graph[x][y] == 0:
        return 0
    
    graph[x][y] = 0
    count = 1
    
    count += dfs(x - 1, y, n, graph)
    count += dfs(x + 1, y, n, graph)
    count += dfs(x, y - 1, n, graph)
    count += dfs(x, y + 1, n, graph)
    
    return count

def solve():
    n = int(sys.stdin.readline())
    
    graph = []
    for _ in range(n):
        line = list(map(int, sys.stdin.readline().strip()))
        graph.append(line)

    complex_sizes = []
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                size = dfs(i, j, n, graph)
                if size > 0:
                    complex_sizes.append(size)

    print(len(complex_sizes))
    
    complex_sizes.sort()
    for size in complex_sizes:
        print(size)

solve()
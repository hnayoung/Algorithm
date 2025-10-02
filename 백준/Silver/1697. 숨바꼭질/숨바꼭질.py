import sys
from collections import deque

def solve():
    try:
        n, k = map(int, sys.stdin.readline().split())
    except:
        return

    if n == k:
        print(0)
        return

    MAX_POS = 100001
    dist = [-1] * MAX_POS 
    
    queue = deque()
    queue.append(n)
    dist[n] = 0

    while queue:
        x = queue.popleft()

        next_positions = [x - 1, x + 1, x * 2]

        for next_x in next_positions:
            if 0 <= next_x < MAX_POS:
                if dist[next_x] == -1:
                    dist[next_x] = dist[x] + 1
                    queue.append(next_x)

                    if next_x == k:
                        print(dist[k])
                        return

solve()
# 숫자 정사각형 (BOJ 1051)

N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]

max_side = 1  # 최소 1x1 정사각형은 항상 가능

limit = min(N, M)
for k in range(2, limit + 1):       # k = 정사각형 한 변의 길이
    for i in range(N - k + 1):
        for j in range(M - k + 1):
            a = grid[i][j]
            if (grid[i][j + k - 1] == a and      # 우상단
                grid[i + k - 1][j] == a and      # 좌하단
                grid[i + k - 1][j + k - 1] == a  # 우하단
               ):
                max_side = k

print(max_side * max_side)

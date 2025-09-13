# 입력
N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

ans = 64  

for i in range(N - 7):
    for j in range(M - 7):
        repaint_w = 0  
        for r in range(8):
            for c in range(8):
                expected = 'W' if (r + c) % 2 == 0 else 'B'
                if board[i + r][j + c] != expected:
                    repaint_w += 1
        repaint_b = 64 - repaint_w

        if repaint_w < ans:
            ans = repaint_w
        if repaint_b < ans:
            ans = repaint_b

print(ans)

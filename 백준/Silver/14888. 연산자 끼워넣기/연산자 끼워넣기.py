N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, /

mx = -1000000000
mn = 1000000000

def dfs(idx, val, p, m, mul, div):
    global mx, mn
    if idx == N:
        if val > mx:
            mx = val
        if val < mn:
            mn = val
        return
    if p:
        dfs(idx+1, val + A[idx], p-1, m, mul, div)
    if m:
        dfs(idx+1, val - A[idx], p, m-1, mul, div)
    if mul:
        dfs(idx+1, val * A[idx], p, m, mul-1, div)
    if div:
        if val < 0:
            dfs(idx+1, -(-val // A[idx]), p, m, mul, div-1)
        else:
            dfs(idx+1, val // A[idx], p, m, mul, div-1)

dfs(1, A[0], op[0], op[1], op[2], op[3])
print(mx)
print(mn)
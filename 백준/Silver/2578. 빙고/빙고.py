# 1) 5x5 보드 입력 (각 줄에 5개 숫자)
a = [list(map(int, input().split())) for _ in range(5)]

# 2) 사회자가 부를 5x5 숫자 입력 (각 줄에 5개 숫자)
b = [list(map(int, input().split())) for _ in range(5)]

# 3) 숫자를 하나씩 부르면서 보드에 표시(0으로 마킹) → 빙고 줄 수 확인
for k in range(5):          # k: 부른 숫자들의 '행' 인덱스
    for l in range(5):      # l: 부른 숫자들의 '열' 인덱스
        called = b[k][l]

        # (A) 보드에서 같은 숫자를 찾으면 0으로 바꿔 '지운다'
        for i in range(5):
            for j in range(5):
                if a[i][j] == called:
                    a[i][j] = 0

        # (B) 현재 빙고 줄(가로/세로/대각선) 개수 세기
        line = 0
        # 가로
        for i in range(5):
            if all(x == 0 for x in a[i]):
                line += 1
        # 세로
        for j in range(5):
            if all(a[i][j] == 0 for i in range(5)):
                line += 1
        # 대각선 2개
        if all(a[i][i] == 0 for i in range(5)):
            line += 1
        if all(a[i][4 - i] == 0 for i in range(5)):
            line += 1

        # (C) 빙고 3줄 이상이면, 문제 요구대로 지금까지 부른 횟수 출력
        if line >= 3:
            print((l + 1) + 5 * k)  # 당신이 의도한 출력식 유지
            exit()

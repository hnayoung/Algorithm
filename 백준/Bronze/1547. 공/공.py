# 첫째 줄에서 컵의 위치를 바꾼 횟수 M을 입력받습니다.
try:
    M = int(input())
except ValueError:
    print(-1)
    exit()

# 공의 초기 위치는 1번 컵입니다.
ball_position = 1

# M번의 교환을 반복합니다.
for _ in range(M):
    try:
        # 각 줄에서 교환할 두 컵의 번호 X와 Y를 입력받습니다.
        X, Y = map(int, input().split())
    except ValueError:
        print(-1)
        exit()

    # 현재 공이 X번 컵에 있다면 Y번 컵으로 위치를 바꿉니다.
    if ball_position == X:
        ball_position = Y
    # 현재 공이 Y번 컵에 있다면 X번 컵으로 위치를 바꿉니다.
    elif ball_position == Y:
        ball_position = X
    # 공이 X나 Y가 아닌 다른 컵에 있으면 위치는 바뀌지 않습니다.

# 모든 교환이 끝난 후 공이 들어있는 최종 컵 번호를 출력합니다.
print(ball_position)

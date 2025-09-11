a, b = map(int, input().split())

# 족보 랭크 계산 함수
def rank_hand(x, y):
    if x == y:                  # 같은 숫자 → 땡
        return (2, x)           # (2, 숫자) → 땡이 끗보다 우선
    else:                       # 끗
        return (1, (x + y) % 10)

my_rank = rank_hand(a, b)

# 덱 준비: 1~10 각 2장
deck = [i for i in range(1, 11)] * 2
deck.remove(a)
deck.remove(b)

wins = 0
total = 0
n = len(deck)  # 18장

# 남은 카드에서 상대가 뽑을 수 있는 모든 경우 탐색
for i in range(n):
    for j in range(i + 1, n):
        opp_rank = rank_hand(deck[i], deck[j])
        total += 1
        if my_rank > opp_rank:      # 내가 더 강하면 승
            wins += 1

# 승률 계산
prob = wins / total
print(f"{prob:.3f}")

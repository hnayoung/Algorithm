import sys

input_data = sys.stdin.read().split()

if not input_data:
    sys.exit()

n = int(input_data[0])
target_sequence = [int(x) for x in input_data[1:]]

stack = []
results = []
current_num = 1
target_index = 0

while target_index < n:
    target = target_sequence[target_index]

    if not stack or stack[-1] < target:
        if current_num > n:
            print("NO")
            sys.exit()

        stack.append(current_num)
        results.append('+')
        current_num += 1

    elif stack[-1] == target:
        stack.pop()
        results.append('-')
        target_index += 1

    else:
        print("NO")
        sys.exit()

sys.stdout.write('\n'.join(results) + '\n')
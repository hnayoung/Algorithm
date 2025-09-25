import sys
input = sys.stdin.readline

def solve_parentheses():
    try:
        T = int(input())
    except:
        return

    for _ in range(T):
        ps = input().strip()
        
        stack = []
        is_vps = True 
        
        for char in ps:
            if char == '(':
                stack.append(char)
            
            elif char == ')':
                if not stack:
                    is_vps = False
                    break 
                else:
                    stack.pop()
        if stack:
            is_vps = False
            
        if is_vps:
            print("YES")
        else:
            print("NO")


solve_parentheses()
T = int(input())
for _ in range(T):
    k = int(input())

    tri = []
    n = 1
    while True:
        t = n*(n+1)//2
        if t > k:
            break
        tri.append(t)
        n+=1
    
    found = 0
    for t1 in tri:
        if found: break
        for t2 in tri:
            if found: break
            for t3 in tri:
                if t1 + t2 + t3 == k:
                    found = 1
                    break
                
    print(found)
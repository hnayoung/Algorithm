b=sum(a:={*map(int,open(0))})-100
print(*sorted(a-[{c,b-c}for c in a if b-c in a][0]))
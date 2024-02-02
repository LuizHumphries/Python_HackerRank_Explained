from collections import defaultdict

n, m = map(int, input().split())
positions = defaultdict(list)

for i in range(n):
    word = input()
    positions[word].append(i+1)

for j in range(m):
    word = input()
    if word in positions:
        print(" ".join(map(str, positions[word])))
    else:
        print(-1)
    
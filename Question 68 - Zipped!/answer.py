x, n = map(int, input().split())
answer = [list(map(float, input().split())) for _ in range(n)]
for x in zip(*answer):
    print(sum(x)/n)
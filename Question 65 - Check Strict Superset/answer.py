a = set(map(int, input().split()))
n = int(input())
answer = True
for _ in range(n):
    if not a.issuperset(set(map(int, input().split()))):
        answer = False
        
print(answer)
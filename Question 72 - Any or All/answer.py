_, arr = input(), list(map(int, input().split()))
print(all([any(str(x)==str(x)[::-1] for x in arr), all(i > 0 for i in arr)]))
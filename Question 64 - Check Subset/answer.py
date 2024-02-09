n = int(input())
for i in range(n):
    _, a = input(), set(map(int, input().split()))
    _, b = input(), set(map(int, input().split()))
    if len(a.intersection(b)) == len(a):
        print(True)
    else:
        print(False)
    
    
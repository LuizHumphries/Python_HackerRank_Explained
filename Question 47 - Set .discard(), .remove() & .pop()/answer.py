n = int(input())
s = set(map(int, input().split()))
n_calls = int(input())


for _ in range(n_calls):
    comand = input().split()
    if comand[0] == "pop":
        s.pop()
    elif comand[0] == "discard":
        s.discard(int(comand[1]))
    else:
        try:
            s.remove(int(comand[1]))
        except KeyError:
            continue

print(sum(s))
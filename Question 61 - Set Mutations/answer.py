n_a = int(input())
a = set(map(int, input().split()))
n = int(input())
comands = [[input().split(), set(map(int, input().split()))] for _ in range(n)]
for comand, b_set in comands:
    if comand[0] == "update":
        a.update(b_set)
    elif comand[0] == "intersection_update":
        a.intersection_update(b_set)
    elif comand[0] == "difference_update":
        a.difference_update(b_set)
    elif comand[0] == "symmetric_difference_update":
        a.symmetric_difference_update(b_set)
    else:
        continue

print(sum(a))
import re
n = int(input())
for _ in range(n):
    r = input()
    try:
        print(all([float(r), ["." == x for x in r], re.search(r".\d", r)]))
    except:
        print(False)
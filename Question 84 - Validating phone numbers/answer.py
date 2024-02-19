import re
n = int(input())
for _ in range(n):
    s = input()
    if bool(re.match(r"[987*]", s)) and bool(re.match(r"^\d{10}$", s)):
        print("YES")
    else:
        print("NO")
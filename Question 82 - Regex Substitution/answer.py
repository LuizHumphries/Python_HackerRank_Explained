import re
n = int(input())
text = "\n".join((input() for _ in range(n)))
print(re.sub(r"(?<=\s)(&&)(?=\s)", "and", re.sub(r"(?<=\s)(\|\|)(?=\s)", "or", text)))
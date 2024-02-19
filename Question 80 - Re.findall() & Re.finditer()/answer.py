import re
s = input()
matches = re.findall(r"(?<=[b-df-hj-np-tz])[aeiou]{2,}(?=[b-df-hj-np-tz])", s, flags=re.IGNORECASE)
if matches:
    print("\n".join(matches))
else:
    print(-1)
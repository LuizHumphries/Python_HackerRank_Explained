import re
repeated_index = re.search(r'([a-zA-Z0-9])\1', input())
if repeated_index:
    print(repeated_index.group(1))
else:
    print(-1)
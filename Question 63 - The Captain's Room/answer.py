from collections import Counter
_, rooms = input(), input().split()
print(Counter(rooms).most_common()[-1][0])
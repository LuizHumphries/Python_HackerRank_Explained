from itertools import combinations
_, items, k = input(), input().split(), int(input())
letters = list(combinations([i + 1 for i in range(len(items))], k))
a_index = [count + 1 for count, value in enumerate(items) if value == "a"]
chance = len([x for x in letters if any(item in x for item in a_index)])
print("{:.3f}".format(chance/len(letters)))
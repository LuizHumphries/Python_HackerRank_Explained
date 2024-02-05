from itertools import combinations_with_replacement

word, size = input().split()
combination = list(combinations_with_replacement(sorted(word), int(size)))
combination = ["".join(item) for item in combination]
print("\n".join(combination))
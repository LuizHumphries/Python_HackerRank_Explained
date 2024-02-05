from itertools import combinations

word, size = input().split()

combinations = [list(combinations(sorted(word), i + 1)) for i in range(int(size))]
combinations = ["".join(item) for sublist in combinations for item in sublist]
print("\n".join(combinations))

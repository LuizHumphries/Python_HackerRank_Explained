from itertools import permutations
word, width = input().split()
print("\n".join(sorted(map("".join, permutations(word, int(width))))))

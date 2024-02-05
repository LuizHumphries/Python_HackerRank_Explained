from collections import Counter
n = int(input())
words = [input() for _ in range(n)]
counted_words = Counter(words)
print(len(set(words)))
print(" ".join(map(str, counted_words.values())))
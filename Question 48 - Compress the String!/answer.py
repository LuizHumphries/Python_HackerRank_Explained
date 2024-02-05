from itertools import groupby

numbers = [int(x) for x in input()]
for key, value in groupby(numbers):
    print(f"({len(list(value))}, {key})", end=" ")

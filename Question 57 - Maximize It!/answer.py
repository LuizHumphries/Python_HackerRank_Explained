from itertools import product

k, m = map(int, input().split())
values = product(*[list(map(int, input().split()))[1:] for _ in range(k)])
result = max([sum(x ** 2 for x in item) % m for item in values])
print(result)
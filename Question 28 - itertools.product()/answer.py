from itertools import product

A, B = map(int, input().split()), map(int, input().split())
print(" ".join(map(str, product(A,B))))
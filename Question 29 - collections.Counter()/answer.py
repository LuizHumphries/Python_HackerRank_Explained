from collections import Counter

bill = 0

N = int(input())
sizes = Counter(map(int, input().split()))
customers = int(input())
orders = [map(int, input().split()) for _ in range(customers)]

for size, price in orders:
    if sizes.get(size):
        sizes[size] -= 1
        bill += price          

print(bill)
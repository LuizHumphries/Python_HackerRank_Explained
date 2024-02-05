from collections import OrderedDict
n = int(input())
order = OrderedDict()
for _ in range(n):
    item, space, price = input().rpartition(" ")
    order[item] = order.get(item, 0) + int(price)

for item, price in order.items():
    print(item, price)
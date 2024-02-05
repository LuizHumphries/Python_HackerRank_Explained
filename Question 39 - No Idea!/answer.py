n, m = map(int, input().split())
n_array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = sum([(i in A) - (i in B) for i in n_array])
print(happiness)
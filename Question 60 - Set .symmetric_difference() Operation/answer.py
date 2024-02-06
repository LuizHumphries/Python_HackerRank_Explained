_, english = input(), set(map(int, input().split()))
_, french = input(), set(map(int, input().split()))
print(len(english.symmetric_difference(french)))
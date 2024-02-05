import math
ab_length, bc_length = int(input()), int(input())
angle = math.degrees(math.atan(ab_length/bc_length))
print(f"{math.floor(angle)}\xb0") if angle - math.floor(angle) < 0.5 else print(f"{math.ceil(angle)}\xb0")
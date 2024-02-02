n = int(input())
for _ in range(n):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except ValueError as val_error:
        print(f"Error Code: {val_error}")
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
def sort_string(s):
    lower_case = sorted([c for c in s if c.islower()])
    upper_case = sorted([c for c in s if c.isupper()])
    odd_digits = sorted([c for c in s if c.isdigit() and int(c) % 2 != 0])
    even_digits = sorted([c for c in s if c.isdigit() and int(c) % 2 == 0])
    return ''.join(lower_case + upper_case + odd_digits + even_digits)
    
    
s = input()
print(sort_string(s))
#PYPY 3
import re
n = int(input())
for i in range(n):
    try:
        regex = input()
        re.compile(regex)        
        print("True")
    except Exception as e:
        print("False")
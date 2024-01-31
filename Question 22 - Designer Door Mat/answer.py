# Enter your code here. Read input from STDIN. Print output to STDOUT
high, width = map(int, input().split())
word = "WELCOME"
pattern = ".|."
filler = "-"

for row in range(high//2):
    print((pattern*(row*2+1)).center(width, filler))
    
print(word.center(width, filler))

for row in reversed(range(high//2)):
    print((pattern*(row*2+1)).center(width, filler))

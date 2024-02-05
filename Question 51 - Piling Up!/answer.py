n = int(input())

for _ in range(n):
    _ = input()
    blocks = list(map(int, input().split()))
    left, right = None, None
    answer = "Yes"
    while len(blocks) > 1:
        if blocks[0] >= blocks[-1]:
            larger_num = blocks[0]
            blocks.pop(0)
        else:
            larger_num = blocks[-1]
            blocks.pop(-1)
        if larger_num < blocks[0] or larger_num < blocks[-1]:
            answer = "No"
            break
    
    print(answer)
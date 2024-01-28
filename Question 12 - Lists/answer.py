if __name__ == '__main__':
    N = int(input())
    comands = [input().split() for _ in range(N)]
    arr = []
    for comand in comands:
        if comand[0] == "print":
            print(arr)
        elif comand[0] == "insert":
            arr.insert(int(comand[1]), int(comand[2]))
        elif comand[0] == "remove":
            arr.remove(int(comand[1]))
        elif comand[0] == "sort":
            arr.sort()
        elif comand[0] == "pop":
            arr.pop()
        elif comand[0] == "reverse":
            arr.reverse()
        elif comand[0] == "append":
            arr.append(int(comand[1]))
        else:
            continue
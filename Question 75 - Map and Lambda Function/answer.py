cube = lambda x: x ** 3

def fibonacci(n):
    def result(i):
        if i in [0,1]:
            return i
        return result(i-1) + result(i - 2)
    return [result(x) for x in range(n)]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
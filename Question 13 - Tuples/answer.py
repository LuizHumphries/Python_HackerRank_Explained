if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))    
    print(hash(t))
#RUN THIS IN PYPY 3 - PYTHON 3 OPTION IS BUGGED
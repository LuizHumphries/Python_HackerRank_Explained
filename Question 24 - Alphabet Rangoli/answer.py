import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    rangoli = []

    for i in range(size):
        line = "-".join(alphabet[i:size])
        rangoli.append((line[::-1]+line[1:]).center(4*size-3, "-"))
        
    print('\n'.join(rangoli[:0:-1]+rangoli))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
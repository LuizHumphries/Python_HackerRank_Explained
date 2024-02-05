from collections import Counter
if __name__ == '__main__':
    s = input()
    
    for letter, count in Counter(sorted(s)).most_common(3):
        print(f"{letter} {count}")
def merge_the_tools(string, k):
    substrings = [string[i:i+k] for i in range(0,len(string),k)]
    substring_non_repeat = ["".join(set(substring)) for substring in substrings]
    print("\n".join(substring_non_repeat))
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
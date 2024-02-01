def minion_game(string):
    s=len(string)
    vowel_score = sum(s - i for i in range(s) if string[i] in "AEIOU")
    consonant_score = sum(s - i for i in range(s) if string[i] not in "AEIOU")
    
    for winner, score in (("Stuart", consonant_score), ("Kevin", vowel_score)):
        if score > consonant_score + vowel_score - score:
            print(f"{winner} {score}")
            break
    else:
        print("Draw")
     
    
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
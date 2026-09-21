def solution(s):
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    length = len(alphabet)
    total = 0
    letter_count = 1 

    for s_letter in s:
        for letter in alphabet:
            if s_letter == letter:
                letter_val = length - alphabet.index(letter)
                total += letter_val * letter_count
                letter_count += 1
    print(total)
solution("azaz")
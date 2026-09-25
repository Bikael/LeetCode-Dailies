def countSubstrings( s: str) -> int:
        all_sub_palindromes = 0
        left = 0
        right = 0

        while left != len(s) and right != len(s):
            palindrome_sub_count = getPalindromeSubstrings(s,left,right)
            if left == right:
                right += 1
            else:
                left += 1

            all_sub_palindromes += palindrome_sub_count
        print(all_sub_palindromes)
        return all_sub_palindromes
    
def getPalindromeSubstrings( s: str, left : int, right : int) -> int:
    offset = 0
    sub_string_count = 0
    while ((left - offset) >= 0 and (right + offset) < len(s)):
        if s[left - offset] == s[right + offset]:
            offset += 1
            sub_string_count += 1
        else:
            return sub_string_count
    return sub_string_count

print(countSubstrings("aaa"))
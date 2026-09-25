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
        return all_sub_palindromes
    
def getPalindromeSubstrings( s: str, left : int, right : int) -> list[str]:
    sub_string_count = 0
    while (left >= 0 and right < len(s) and s[left] == s[right]):
        sub_string_count += 1
        left -= 1
        right += 1
    return sub_string_count

print(countSubstrings("aaa"))
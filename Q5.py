def getPalindromeSubstring(s: str, left : int, right : int) -> str:
    offset = 0
    while ((left - offset) >= 0 and (right + offset) < len(s)):
        # print(f"right offset {right + offset}")
        # print(f"left offset {left - offset}")
        if s[left - offset] == s[right + offset]:
            offset += 1
        else:
            return s[left - offset + 1 : right + offset]

    return s[left - offset + 1 : right + offset]

# print(getPalindromeSubstring("dabba", 2 , 3))

def longestPalindrome( s: str) -> str:

    longestPalindrome = ""
    left = 0
    right = 0

    while left != len(s) and right != len(s):
        if left == right:
            right += 1
        else:
            left += 1

        palindrome_sub = getPalindromeSubstring(s,left,right)
        if len(palindrome_sub) > len(longestPalindrome):
            longestPalindrome = palindrome_sub
    return "Boom longest palindrome: " + longestPalindrome

word = input("Enter your string: ")
print(longestPalindrome(word))

class Solution:
    def isPalindrome(self, s: str) -> bool:

        result = ""

        for char in s:
            if char.isalnum():
                result += char.lower()
        
        reverse = result[::-1]

        return result == reverse
        
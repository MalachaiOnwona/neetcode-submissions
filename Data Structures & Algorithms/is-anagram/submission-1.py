class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_count = {}
        t_count = {}

        if len(s) != len(t):
            return False

        for char in s:
            s_count[char] = s_count.get(char, 0) + 1
        
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        
        if s_count != t_count:
            return False
        else:
            return True
        
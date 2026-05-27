class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Return False for unequal lengths
        if len(s) != len(t):
            return False

        #Initialize Count Hashmaps    
        s_count, t_count = {}, {}

        for letter in s:
            # .get(i,0) sets default value of 0
            # for when letter does not exist in 
            # hashmap yet
            s_count[letter] = s_count.get(letter,0) + 1
        
        for letter in t:
            t_count[letter] = t_count.get(letter,0) + 1
        
        if s_count != t_count:
            return False
        return True



        
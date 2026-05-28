class Solution:

    def encode(self, strs: List[str]) -> str:
        # Standard Approach: Length-Prexfix Encoding
        # Ex: ["hello", "world"] -> "5#hello5#world"
        encoded = ""

        for string in strs:
            encoded += str(len(string)) + "#" + string
        
        return encoded 


    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1

            length = int(s[i:j])
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1+ length

        return result



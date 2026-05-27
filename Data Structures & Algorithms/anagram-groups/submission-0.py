class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {} # general hashmap
        result = [[]] # resulting list

        for string in strs:
            countmap = {} # track count of letters in each string in strs
            for letter in string:
                if letter in countmap:
                    countmap[letter]  += 1
                else:
                    countmap[letter] = 1

            # use a sorted tuple to convert the countmaps
            # to immutable, hashable values so that they
            # can be compared for equality with other 
            # countmaps
            key = tuple(sorted(countmap.items()))

            if key not in hashmap:
                hashmap[key] = []
            
            # set the countmap to be the key of 
            # the general hashmap
            hashmap[key].append(string)
            
        return list(hashmap.values())

        
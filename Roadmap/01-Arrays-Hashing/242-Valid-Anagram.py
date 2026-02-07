class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # create a frequency hash map for both s and t
        # count the occurrences of each character and compare the two maps
        # if the maps are identical, return true; otherwise, return false 
        map_s, map_t = {}, {}  
        for i in range(len(s)):
            if s[i] not in map_s:
                map_s[s[i]] = 0
            if t[i] not in map_t:
                map_t[t[i]] = 0
                
            map_s[s[i]] += 1
            map_t[t[i]] += 1

        return map_s == map_t
    
    # time complexity: O(n)
    # space complexity: O(n)
    
    def isAnagram2(self, s: str, t: str) -> bool:
        # first of all inputs are rejected if lengths don't match
        if len(s) != len(t):
            return False
        # time complexity of the sorting algorithm in python: O(nlogn)
        return sorted(s) == sorted(t)

    # time complexity: O(nlogn + mlogm) because of the sorting algorithm
    # space complexity: O(1) or O(n) (depends on the sorting algorithm)

    # unless we know that n dominates m, we must keep both terms
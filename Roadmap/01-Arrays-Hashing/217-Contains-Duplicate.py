class Solution:
    # solution 1
    def hasDuplicate(self, nums: List[int]) -> bool:
        # convert the list to a set and compare the sizes to detect duplicates
        return len(set(nums)) < len(nums)

    # time complexity: O(n) due to building the set
    # space complexity: O(n) for the additional set
    # len() operation is O(1)



    # solution 2
    def hasDuplicate2(self, nums: List[int]) -> bool:
        # keep a hash set of seen elements and check for duplicates while iterating
        seen = set()
        for e in nums:
            if e in seen:
                return True
            seen.add(e)

        return False

    # time complexity is O(n) since this code checks every element in nums once
    # space complexity is O(n)
    # insert/lookup of a set: O(1) on average (O(n) in worst case due to collisions)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        f = {}
        for item in nums:
            if item in f: return True
            f[item] = 1
        return False



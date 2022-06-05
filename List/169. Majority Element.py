from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        value, nums = Counter(nums).most_common(1)[0]
        return value
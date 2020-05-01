"""

Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""

# Solution1 :
def maxsub(s):

    maxhere = maxsum = 0
    for i, _ in enumerate(s):
        if maxhere <= 0:
            maxhere = s[i]

        else:
            maxhere += s[i]
            maxsum = max(maxhere, maxsum)
    return maxsum

print(maxsub([-2,1,-3,4,-1,2,1,-5,4]))
# error : [-2, 1]

# Solution2:
def ms(nums):
    if not nums:
        return 0
    current = nums[0]
    m = current
    for i in range(1, len(nums)):
        if current < 0:
            current = 0
        current += nums[i]
        m = max(current, m)

    return m

print(ms([-2,1,-3,4,-1,2,1,-5,4]))

# Solution 3:
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    dp = [nums[0] for i in range(len(nums))]
    max_result = nums[0]
    for i in range(1, len(nums)):
        if dp[i - 1] < 0:
            dp[i] = nums[i]
        else:
            dp[i] = dp[i - 1] + nums[i]
        if max_result < dp[i]:
            max_result = dp[i]
    return max_result

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


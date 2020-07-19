"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
"""

from collections import Counter
def topKFrequent(nums,k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    #nums = set(nums)
    result = Counter(nums)
    k_freq = result.most_common(k)
    k_freq = [k[0] for k in k_freq]
    return k_freq

print(topKFrequent([1,1,1,2,2,3],2))

def topKFrequent2(nums,k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    #nums = set(nums)
    result = Counter(nums)
    sorted_nums = sorted(result.items(), key=lambda x: x[1], reverse=True)
    #print(sorted_nums[:k])
    k_freq2 = [num[0] for num in sorted_nums[:k]]
    return k_freq2
print(topKFrequent2([1,1,1,2,2,3],2))

#demo
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    d = {}
    output = []

    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    dmap = sorted(d, key=d.get)
    f_dmap = dmap[::-1]

    for i in range(k):
        output.append(f_dmap[i])

    return output
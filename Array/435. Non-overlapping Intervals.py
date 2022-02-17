"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.



Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        count = 0
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            next_start = intervals[i][0]
            next_end = intervals[i][1]
            if next_start<end:
                end = next_end
            else:
                count +=1
        return count
    def eraseOverlapIntervals2(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda y: y[1])
        erase_total = 0
        largest_so_far = float('-inf')
        for interval in intervals:
            if (interval[0] < largest_so_far):
                erase_total += 1
            else:
                largest_so_far = interval[1]
        return int(erase_total)





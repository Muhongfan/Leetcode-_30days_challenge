"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.



Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""


def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])  # 按左端点从小到大排序
    temp_pos = 0
    cnt = 0
    for i in range(1, len(intervals)):
        if intervals[temp_pos][1] > intervals[i][0]:  # 当当前区间右端点>i区间左端点
            if intervals[i][1] <= intervals[temp_pos][1]:  # 当i区间右端点<当前区间右端点，表示i区间被覆盖在当前区间中
                temp_pos = i  # 更新temp_pos，选择覆盖范围小的i区间
            cnt += 1  # 当前区间右端点>i区间左端点都要计数+1
        else:
            temp_pos = i  # 当当前区间右端点<=i区间左端点，表示不重叠，要更新temp_pos
print(eraseOverlapIntervals([[1,2],[2,3]]))
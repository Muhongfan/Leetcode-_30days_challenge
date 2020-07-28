"""
You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

You need to return the least number of units of times that the CPU will take to finish all the given tasks.



Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation:
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A


Constraints:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""
from collections import Counter

# https://www.cnblogs.com/grandyang/p/7098764.html
def leastInterval(tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    count = Counter(tasks)
    max_num = Counter(tasks).most_common()[0][1]
    # find the nums of the ones that have the same count
    num_of_max_freq = len([k for k, v in count.items() if v == max_num])
    # if the rest letters are ignored
    res = (n + 1) * (max_num - 1) + num_of_max_freq
    # if the rest letters are very long
    return max(res, len(tasks))

print(leastInterval(["A","A","A","B","B","B"], 0))
print(leastInterval(["A","A","A","B","B","B"], 2))
array = [0,1,2,2,3,4,4,4,5,6]
print(Counter(array))
# most_common找到出现次数最多的元素
print(Counter(array).most_common(1)[0][0])
#Counter({4: 3, 2: 2, 0: 1, 1: 1, 3: 1, 5: 1, 6: 1})
#4
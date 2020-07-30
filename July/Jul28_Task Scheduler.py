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

#print(leastInterval(["A","A","A","B","B","B"], 0))
#print(leastInterval(["A","A","A","B","B","B"], 2))
array = [0,1,2,2,3,4,4,4,5,6]
print(Counter(array))
# most_common - to find the most frequent ones
print(Counter(array).most_common(1)[0][0])
#Counter({4: 3, 2: 2, 0: 1, 1: 1, 3: 1, 5: 1, 6: 1})
#4

#
def leastInterval2(tasks, n):
    frequencies = [0] * 26
    for t in tasks:
        #ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，
        #它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值
        frequencies[ord(t) - ord('A')] += 1
    frequencies.sort()
    f_max = frequencies.pop()
    idle_time = (f_max - 1) * n
    while frequencies and idle_time > 0:
        idle_time -= min(f_max - 1, frequencies.pop())
    idle_time = max(0, idle_time)
    return idle_time + len(tasks)


print(leastInterval2(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))

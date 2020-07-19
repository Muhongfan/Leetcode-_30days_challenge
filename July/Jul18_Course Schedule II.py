
from collections import defaultdict

def findOrder(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    graph = defaultdict(list)
    indegrees = defaultdict(int)
    for u, v in prerequisites:
        graph[v].append(u)
        indegrees[u] += 1
    path = []
    for i in range(numCourses):
        zeroDegree = False
        for j in range(numCourses):
            if indegrees[j] == 0:
                zeroDegree = True
                break
        if not zeroDegree:
            return []
        indegrees[j] -= 1
        path.append(j)
        for node in graph[j]:
            indegrees[node] -= 1
    return path

print(findOrder(2,[[1,0]]))

#demo
def findOrder(numCourses, prerequisites):

    status = [0] * numCourses
    graph = collections.defaultdict(list)
    for c, pre in prerequisites:
        graph[pre].append(c)
    stack = []


    def dfs(course):
        if status[course] == 1:
            return False  # circle case
        if status[course] == 2:  # visited
            return True
        status[course] = 1  # visiting
        for c in graph[course]:
            if not dfs(c):
                return False
        stack.append(course)
        status[course] = 2
        return True


    for course in range(numCourses):
        if status[course] == 0:
            if not dfs(course):
                return []
    return stack[::-1]


def findOrder(numCourses, prerequisites):
    how_many_pre_req = [0] * numCourses
    other_course = [[] for _ in range(n)]
    for course, pre in prerequisites:
        other_course[pre].append(course)
        how_many_pre_req[course] += 1
    dfs = [i for i in range(numCourses) if how_many_pre_req[i] == 0]
    for course in dfs:
        for i in other_course[course]:
            how_many_pre_req[i] -= 1
            if how_many_pre_req[i] == 0:
                dfs.append(i)
    if len(dfs) == numCourses:
        return dfs
    return []

"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
from collections import defaultdict


class Solution:
    def pathSum(self, root, sum) :
        if not root:
            return 0
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)


    def dfs(self, root, sum):
        # count the number of paths starting from the node
        ans = 0
        if not root:
            return ans
        if root.val == sum:
            ans += 1
        ans += self.dfs(root.left, sum - root.val)
        ans += self.dfs(root.right, sum - root.val)
        return ans
solu = Solution()
print(solu.pathSum([10,5,-3,3,2,0,11,3,-2,0,1],8))

# demo2
def pathSum(self, root, sum):
    running_sum_counter = defaultdict(int)
    # This step is important; otherwise we will miss paths
    # from the root
    running_sum_counter[0] = 1
    return dfs(root, 0, running_sum_counter, sum)


def dfs(root, running_sum, running_sum_counter, target):
    if not root:
        return 0
    # Update running sum and counter
    # This is the trick to make it O(N) fast:
    # In each array, we need to look for continuous subarrays
    # that sum up to the target sum. To remove duplicate sums,
    # we keep a running sum at each index, so that when the array
    # is extended, to check how many subarrays would sum up to
    # the target, we just check the count of:
    # new_running_sum - target = # existing running sums
    # Think of it as this:
    # |--prevSum---|-----target-----|
    # |------newRunningSum----------|
    # target = newRunningSum - prevSum, and prevSum can be cached
    # so we compute each sum only once.
    running_sum += root.val
    num_paths = running_sum_counter[running_sum - target]
    running_sum_counter[running_sum] += 1

    # Go down
    num_paths += dfs(root.left, running_sum, running_sum_counter, target)
    num_paths += dfs(root.right, running_sum, running_sum_counter, target)

    # Before return, revert the "damage" -- we'll be back
    # to a state where the updated running_sum hasn't
    # been encountered yet
    running_sum_counter[running_sum] -= 1
    return num_paths
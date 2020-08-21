"""
We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.



Example 1:

Input: candies = 7, num_people = 4
Output: [1,2,3,1]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0,0].
On the third turn, ans[2] += 3, and the array is [1,2,3,0].
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].
Example 2:

Input: candies = 10, num_people = 3
Output: [5,2,3]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0].
On the third turn, ans[2] += 3, and the array is [1,2,3].
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].


Constraints:

1 <= candies <= 10^9
1 <= num_people <= 1000
"""


def distributeCandies(self, candies: int, num_people: int) -> List[int]:
    rst, i, t = [0] * (num_people + 1), 0, 0
    while candies > 0:
        k = i % num_people + 1
        num_dst = i + 1
        rst[k] = rst[k] + num_dst if candies >= num_dst else rst[k] + candies
        candies -= num_dst
        i += 1
    return rst[1:num_people + 1]

#@@
def distributeCandies(self, candies, num_people):
    """
    :type candies: int
    :type num_people: int
    :rtype: List[int]
    """
    loops = int(candies / ((num_people * (num_people + 1)) / 2))
    if loops > 0:
        num_p = num_people
        while loops > 0:
            num_p += num_people
            loops = int(candies / ((num_p * (num_p + 1)) / 2))

        num_p -= num_people
        loops = num_p / num_people
        candies_remaining = candies - ((num_p * (num_p + 1)) / 2)
        loop = loops - 1
        distr = [num_people * (((loops - 1) * (loops)) / 2)] * num_people
        for i in range(num_people):
            distr[i] += loops * (i + 1)
        count = 0
        while candies_remaining > 0:
            distr[count] += (loops * num_people) + (count + 1) if candies_remaining > (
                       (loops * num_people) + (count + 1)) else candies_remaining
            candies_remaining -= (loops * num_people) + (count + 1)
            count += 1
    else:
        distr = [0] * num_people
        count = 1
        while candies > 0:
            distr[count - 1] = count if candies > count else candies
            candies -= count
            count += 1

    return distr

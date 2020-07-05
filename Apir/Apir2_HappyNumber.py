"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

"""


# Solution 1:

def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    sum = n
    sequence = []
    # same = []
    num = 0
    while sum > 1:
        # get each number in the digit
        while sum > 0:
            (sum, r) = divmod(sum, 10)
            sequence.append(str(r))
        # get the sum of the square of each numbers
        for i in sequence:
            sum += pow(int(i), 2)
        # print("sum",sum)
        sequence = []
        # same.append(str(sum))
        # print(same)
        num = num + 1
        if num == 10:
            sum = 0
    return sum

# Solution 2:
def device(n):
    s = []
    while n > 0:
        (n, r) = divmod(n, 10)
        s.append(str(r))
    return s


def isHappy(n):
    same = set()
    while n not in same:
        same.add(n)
        # get each number in the digit
        sequence = device(n)
        #print(sequence)
        n = 0
        # get the n of the square of each numbers
        for i in sequence:
            n += pow(int(i), 2)
        print("n",n)
        if n ==1:
            return True
    return False

print(isHappy(4))







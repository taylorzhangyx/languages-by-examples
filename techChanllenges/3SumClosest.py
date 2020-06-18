import sys


class Solution(object):
    def threeSumClosest(self, num, target):
        """
    input: int[] num, int target
    return: int
    """
        # write your solution here
        minDiff = sys.maxsize
        num.sort()
        for i in range(len(num)):
            firstV = num[i]
            numLeft = num[i + 1 :]
            newTarget = target - firstV
            diff = self.twoSumClosest(numLeft, newTarget)
            if minDiff > diff:
                minDiff = diff
            if minDiff == 0:
                return 0
        return minDiff

    def twoSumClosest(self, nums, target):
        # nums -> min - max
        pMin = 0
        pMax = len(nums) - 1
        minDiff = sys.maxsize

        # optimize
        if len(nums) <= 1:
            return minDiff

        while minDiff != 0 and pMin < pMax:
            sums = nums[pMin] + nums[pMax]
            diff = abs(sums - target)
            if minDiff > diff:
                minDiff = diff
            if sums > target:
                pMax -= 1
            else:
                pMin += 1
        return minDiff

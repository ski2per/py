from typing import List


class Solution:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    """
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        d = {}
        for idx, num in enumerate(nums):
            pass



if __name__ == '__main__':
    sol = Solution()
    print(sol.two_sum([3, 7, 8, 10, 4, 5], 9))


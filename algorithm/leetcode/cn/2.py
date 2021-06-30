from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        tmp
        for i in range(k):
            nums = nums[-1:] + nums[:-1]
        print(id(nums))



if __name__ == '__main__':
    l = [1,2,3,4,5,6,7]
    k = 3
    sol = Solution()
    sol.rotate(l, k)
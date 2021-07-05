from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for x in nums:
            d[x] = 0
        print(d)
        return len(d.keys()) != len(nums)


if __name__ == '__main__':
    # l = [1,1,1,3,3,4,3,2,4,2]
    l = [1,2,3,1]
    sol = Solution()
    print(sol.containsDuplicate(l))
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for x in nums:
            result ^= x
            print(result)
        return result


if __name__ == '__main__':
    l = [4, 1, 2, 1, 2]
    sol = Solution()
    print(sol.singleNumber(l))

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        for j in range(1, len(prices)):
            if prices[i] < prices[j]:
                p = prices[j] - prices[i]
                profit += p
            i += 1
        return profit


if __name__ == '__main__':
    # l = [7, 1, 5, 3, 6, 4]
    l = [1,2,3,4,5]

    sol = Solution()
    print(sol.maxProfit(l))

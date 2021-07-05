from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        total = len(nums)
        if k > total:
            # [1,2], k=3
            k = k%total
            
        # Say [1,2,3,4,5,6,7]
        nums[0:total] = nums[::-1]
        # print(nums) 
        # [7,6,5,4,3,2,1]
        nums[k:total] = nums[k:total][::-1]
        # print(nums)
        # [7,6,5,1,2,3,4]
        nums[0:k] = nums[0:k][::-1]
        # print(nums)
        # [5,6,7,1,2,3,4]





if __name__ == '__main__':
    # l = [1,2,3,4,5,6,7]
    # k = 3
    l = [1,2]
    k = 5
    sol = Solution()
    sol.rotate(l, k)
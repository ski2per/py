class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        head = 0
        total = len(nums)
        
        for i in range(total):
            if nums[head] != nums[i]:
                print(nums[i])
                nums



if __name__ == "__main__":
    sol = Solution()
    sol.removeDuplicates([0,0,0,1,1,2,3,3,4])

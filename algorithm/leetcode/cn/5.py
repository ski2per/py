from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Sort two lists first
        nums1.sort()
        nums2.sort()

        len1 = len(nums1)
        len2 = len(nums2)
        print(len1, len2)
        print(nums1, nums2)

        i = 0
        j = 0
        nums = []

        try:
            print(i,j)
            while i < len1 and j < len2:
                if nums1[i] == nums2[j]:
                    nums.append(nums1[i])
                elif nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1

        except IndexError:
            return nums
        return nums


if __name__ == '__main__':
    l1 = [1, 2, 2, 1]
    l2 = [2, 2]
    sol = Solution()
    l = sol.intersect(l1, l2)
    print(l)

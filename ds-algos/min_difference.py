from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 10000000
        for i in range(0, len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            print(diff, i)
            res = min(res, diff)

        return res
    
if __name__ == "__main__":
    s = Solution()
    print(s.minimumDifference(nums = [9,4,1,6], k = 2))
    a = [1, 2, 3, 4]
    k = 2
    print(list(range(len(a) - k - 1, -1, -1)))
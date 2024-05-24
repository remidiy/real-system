from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums: List[int], t: int):
            d = {}
            for i in range(len(nums)):
                residual = t - nums[i]
                d[residual] = i
                if nums[i] in d:
                    return [i, d[nums[i]]]

        res = list()
        for i in range(len(nums)):
            compliment = twoSum(nums[i+1:], -nums[i]) 
            print(compliment)
            if compliment:
                compliment.append(nums[i])
                compliment.sort()
                res.append(compliment)

        return list(res)
    
if __name__ == "__main__":
    s = Solution()
    res = s.threeSum([-1,0,1,2,-1,-4])
    print(f"main : {res}")

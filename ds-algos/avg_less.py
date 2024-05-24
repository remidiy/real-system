from typing import List
from functools import reduce

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        res = 0
        curr_mean = reduce(lambda x,y: x + y, arr[0:k])/k
        if curr_mean >= threshold: res += 1
        for i in range(1, len(arr)):
            if i + k <= len(arr):
                prev = arr[i - 1]
                nxt = arr[i + k - 1]
                curr_mean = curr_mean + (nxt - prev)/k
                print(i-1, i + k - 1, curr_mean)
                if curr_mean >= threshold:
                    res += 1

        return res
    
if __name__ == "__main__":
    s = Solution()
    print(s.numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))
    print((13)//5)
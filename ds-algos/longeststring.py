class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []
        max_res = 0 
        l  = 0
        for r in range(len(s)):
            
            if s[r] in res:
                while l < r:
                    res.remove(s[l])
                    if s[l] == s[r]:
                        l += 1
                        break
                    l += 1
            res.append(s[r])
            max_res = max(max_res, len(res))

        return max_res
    
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkew"))

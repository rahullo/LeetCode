#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        i = 0
        j = len(height)-1
        while i < j:
            h = min(height[i], height[j])
            ans = max(ans, h*(j-i))
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return ans

        
# @lc code=end


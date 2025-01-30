#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev = 0
        temp = x
        while temp != 0:
            digit = temp % 10
            rev = 10 * rev + digit
            temp //= 10
        return rev == x


        
        
# @lc code=end

c = Solution()
print(c.isPalindrome(12321))
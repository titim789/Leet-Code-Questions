class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def climb(left):
            if left == 0:
                return 1
            
            if left == 1:
                return climb(left-1)
            
            # else if more than 1
            return climb(left-1) + climb(left-2)
    
        return climb(n)
    
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def helper(left):
            if left == 0 or left == 1:
                return 1
            if left not in memo:
                memo[left] = helper(left-1) + helper(left-2)
            
            return memo[left]
        
        return helper(n)
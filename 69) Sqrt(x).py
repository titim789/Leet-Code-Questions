class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        a = x/2

        for i in range(19):
            a = 0.5*(a + x/a)

        return int(a)
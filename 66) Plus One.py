class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        i = len(digits)-1
        while True:
            tot = digits[i] + 1
            if tot == 10:
                digits[i] = 0
                if i == 0:
                    digits.insert(0,1)
                    break
            else:
                digits[i] = tot
                break
            i -= 1

        return digits
class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        value = [1000,900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        ans = ""

        index = 0
        while num != 0:
            while num >= value[index]:
                num -= value[index]
                ans += symbol[index]
            index += 1

        return ans
        
        
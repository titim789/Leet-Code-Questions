class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = n2 = 0
        for i in num1:
            n1 = n1*10 + ord(i)-48
        for i in num2:
            n2 = n2*10 + ord(i)-48

        return str(n1*n2)
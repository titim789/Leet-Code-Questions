class Solution:
    def myAtoi(self, s: str) -> int:
        num = ""
        neg_flag = ""
        for char in s:
            if char.isdigit():
                num += char
            elif char == "-":
                if neg_flag != "":
                    break
                if num == "":
                    neg_flag = True
                    continue
                else:
                    break
            elif char == "+":
                if neg_flag != "":
                    break
                if num == "":
                    neg_flag = False
                    continue
                else:
                    break
            elif char == " ":
                if num != "" or neg_flag != "":
                    break
                continue
            else:
                break
        if num == "":
            num = "0"

        if neg_flag:
            ans = -int(num)
        else:
            ans = int(num)
        
        if ans < -2**31:
            return -2**31
        elif ans > 2**31-1:
            return 2**31-1
        else:
            return ans
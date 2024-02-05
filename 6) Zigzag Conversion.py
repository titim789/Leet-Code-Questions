class Solution:
    def convert(self, s: str, numRows: int) -> str:
        output_dict = []
        for row in range(numRows):
            output_dict.append("")
        curr_num = 0
        for char in s:
            output_dict[curr_num] += char
            if curr_num == numRows-1:
                reverse_order = True
            if curr_num == 0:
                reverse_order = False
            if numRows != 1:
                if reverse_order:
                    curr_num -= 1
                else:
                    curr_num += 1
        
        return "".join(output_dict)
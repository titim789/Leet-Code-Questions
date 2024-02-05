class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        highest_tenth = 0

        while True:
            if x//(10**highest_tenth):
                highest_tenth+=1
            else:
                break
        
        current_tenth = highest_tenth - 1
        flipped_pos = 0

        flipped_num = 0
        temp = int(x)
        while temp != 0:
            right_num = temp//(10**current_tenth)
            flipped_num += right_num*(10**(flipped_pos))
            temp -= right_num*(10**(current_tenth))
            current_tenth -= 1
            flipped_pos += 1
        
        if flipped_num == x:
            return True
        else:
            return False
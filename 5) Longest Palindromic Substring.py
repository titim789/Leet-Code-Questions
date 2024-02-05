class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def isPalindrome(s: str):
            string_length = len(s)
            for i in range(string_length//2):
                if(s[i] != s[string_length-i-1]):
                    return False
            return True

        longest_substring = ""

        if len(s) == 1 or len(set(s)) == 1:
            return s
        else:
            longest_substring = s[0]

        for i in range(len(s)):
            left = i-1
            right = i+1
            
            # Check if left is same (between 2 numbers)
            while left > -1 and right <= len(s):
                if isPalindrome(s[left:right]):
                    if len(s[left:right]) > len(longest_substring):
                        longest_substring = s[left:right]
                else:
                    break
                left -= 1
                right += 1
            
            first = i-1
            last = i+2

            # Check if left and right match (between current number)
            while first > -1 and last <= len(s):
                if isPalindrome(s[first:last]):
                    if len(s[first:last]) > len(longest_substring):
                        longest_substring = s[first:last]
                else:
                    break
                first -= 1
                last += 1

            if longest_substring == s:
                break
        return longest_substring
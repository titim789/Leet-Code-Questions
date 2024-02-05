class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_substring = ""
        current_substring = ""
        for letter in s:
            if letter not in current_substring:
                current_substring += str(letter)
            else:
                if len(longest_substring) <= len(current_substring):
                    longest_substring = current_substring
                current_substring = current_substring[current_substring.rfind(letter)+1:]+str(letter)
            
        if len(longest_substring) <= len(current_substring):
            longest_substring = current_substring 
        
        return len(longest_substring)

        
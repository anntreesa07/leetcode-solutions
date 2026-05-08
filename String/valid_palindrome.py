# 125. Valid Palindrome

#uses string manipulation to clean the input string by removing non-alphanumeric characters and converting it to lowercase. Then it checks if the cleaned string is equal to its reverse. If they are the same, then the original string is a palindrome.


class Solution(object):
    def isPalindrome(self, s):

        SLower=s.lower()

        cleaned=""

        for ch in SLower:
            if ch.isalnum():
                cleaned+=ch

        if cleaned==cleaned[::-1]:
            return True
        else:
            return False
# 14. Longest Common Prefix

#we can solve this problem by iterating through the characters of the first string and comparing them with the corresponding characters of the other strings. We can keep track of the longest common prefix found so far and return it at the end.


class Solution(object):
    def longestCommonPrefix(self, strs):
   

        prefix = ""

        for i in range(len(strs[0])):

            for word in strs:

                if i >= len(word) or word[i] != strs[0][i]:
                    return prefix

            prefix += strs[0][i]

        return prefix
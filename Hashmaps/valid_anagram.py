#242. Valid Anagram - Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#uses two hashmaps to count the frequency of characters in both strings and then compares the hashmaps. If they are the same, then the strings are anagrams of each other.



class Solution(object):
    def isAnagram(self, s, t):
        
        if len(s)!=len(t):
            return False     #if not same length, not anagram

        countS={}
        countT={}

        for ch in s:
            if ch in countS:
                countS[ch]+=1
            else:
                countS[ch]=1

        for ch in t:
            if ch in countT:
                countT[ch]+=1
            else:
                countT[ch]=1
        
        if countS==countT:    #if both dictionaries are same
            return True
        else:
            return False
        
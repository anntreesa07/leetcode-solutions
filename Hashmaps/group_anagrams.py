# 49. Group Anagrams

#here we can use a hash map to group the anagrams together. The key of the hash map will be the sorted version of the word, and the value will be a list of words that are anagrams of each other. we iterate through the list of words, sort each word and use it as a key to group the anagrams together. Finally, we return the values of the hash map as a list of lists.



class Solution(object):
    def groupAnagrams(self, strs):
        
        groups = {}

        for word in strs:

            key = ''.join(sorted(word))

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())
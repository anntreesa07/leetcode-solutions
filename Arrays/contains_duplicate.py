# Using set to track seen elements

class Solution(object):
    def containsDuplicate(self, nums):

        checked = set()

        for num in nums:
            if num in checked:
                return True

            checked.add(num)

        return False
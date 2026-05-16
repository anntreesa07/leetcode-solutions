# 704. Binary Search

#we can solve this problem by using a binary search algorithm. We will use two pointers, one at the beginning of the array and one at the end. We will calculate the middle index and compare the value at that index with the target. If it matches, we return the index. If it is less than the target, we move the left pointer to the right of the middle index. If it is greater than the target, we move the right pointer to the left of the middle index. We repeat this process until we find the target or until the left pointer exceeds the right pointer, in which case we return -1.

class Solution(object):
    def search(self, nums, target):
        

        left=0
        right=len(nums)-1

        while (left<=right):
           
            mid=(left+right)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1

        return -1
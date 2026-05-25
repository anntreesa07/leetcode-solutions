# 11. Container With Most Water

#we can solve this problem using a two-pointer approach. We will initialize two pointers, one at the beginning of the array (left) and one at the end of the array (right). We will calculate the area formed by the lines at these two pointers and keep track of the maximum area found. Then, we will move the pointer that points to the shorter line inward, as moving the taller line would not increase the area. We will repeat this process until the two pointers meet.

class Solution(object):
    def maxArea(self, height):
        
        left=0
        right=len(height)-1
        maxArea=0
        while left<right:
            area=min(height[left],height[right])*(right-left)
            if area>maxArea:
                maxArea=area
            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return maxArea
# 53. Maximum Subarray

#we can solve this problem using a greedy approach. We will keep track of the current sum of the subarray and the maximum sum found so far. We will iterate through the array, adding each element to the current sum. If the current sum exceeds the maximum sum, we update the maximum sum. If the current sum becomes negative, we reset it to zero, as a negative sum would not contribute to a maximum subarray in future iterations.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum=0
        max=nums[0]
        for i in nums:
            sum+=i
            if sum>max:
                max=sum
            if sum<0:
                sum=0
            

        return max


        
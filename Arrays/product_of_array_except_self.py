#238. Product of Array Except Self

#we can solve this problem by creating two arrays, one for the prefix product and one for the postfix product. The prefix product array will store the product of all the elements to the left of the current index, and the postfix product array will store the product of all the elements to the right of the current index. Finally, we can multiply the corresponding elements from both arrays to get the final result.

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        product=1
        prefix=[]
        for num in nums:
            prefix.append(product)
            product*=num

        product=1
        postfix = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = product
            product*=nums[i]

        answer=[]
        for i in range(len(nums)):
            answer.append(prefix[i] * postfix[i])

        return answer
        


        

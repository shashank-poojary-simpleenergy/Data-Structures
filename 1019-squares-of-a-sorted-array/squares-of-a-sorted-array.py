class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums)):
            if nums[i]<=0 or nums[i]>0:
                res.append(nums[i]**2)
        res.sort()
        for i in range(len(nums)):
            nums[i]=res[i]
        return nums
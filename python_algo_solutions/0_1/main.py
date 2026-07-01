#this algo is for the leetcode problem "two sum"
#given 2 array, find the indices of the two numbers that add up to the target
"""

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for k in range(i + 1, len(nums)):
                if nums[i] + nums[k] == target:
                    return [i, k]

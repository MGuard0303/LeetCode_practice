"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]


Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]



Constraints:

1.  2 <= nums.length <= 104
2.  -109 <= nums[i] <= 109
3.  -109 <= target <= 109
4.  Only one valid answer exists.
"""





class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ele in nums:
            diff = target - ele
            
                
            if diff in nums:
                if nums.index(diff) != nums.index(ele):
                    return [nums.index(ele), nums.index(diff)]
                
                if nums.index(diff) == nums.index(ele):
                    index = []
                    for i, v in enumerate(nums):
                        if v == ele:
                            index.append(i)
                            
                    if len(index) >= 2:
                        return [index[0], index[1]]
                    
                    elif len(index) < 2:
                        continue
                    
            
            
            
            
            elif diff not in nums:
                continue

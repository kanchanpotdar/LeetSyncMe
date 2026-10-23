class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Sort the array in-place
        nums.sort()
        
        # The majority element will always be at the middle index
        return nums[len(nums) // 2]
        
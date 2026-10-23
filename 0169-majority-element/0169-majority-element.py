class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = {}
        majority_threshold = len(nums) // 2
        
        for num in nums:
            # Increment the count for the current number
            counts[num] = counts.get(num, 0) + 1
            
            # If the count exceeds n/2, we found the majority element
            if counts[num] > majority_threshold:
                return num
        
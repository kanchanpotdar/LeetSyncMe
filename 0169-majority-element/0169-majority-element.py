class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            # If the count drops to 0, we pick a new candidate
            if count == 0:
                candidate = num
                
            # If the current number matches our candidate, increment the count
            # Otherwise, decrement the count
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        # The problem guarantees a majority element exists, so the remaining candidate is our answer
        return candidate
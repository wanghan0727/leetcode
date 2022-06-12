class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        res = 0
        tmp = 0
        window = set()
        left = 0
        right = 0
    
        for right in range(len(nums)):
            while nums[right] in window:
                tmp -= nums[left]
                window.remove(nums[left])
                left += 1
            window.add(nums[right])
            tmp += nums[right]
            
            res = max(res, tmp)
            
        return res
        
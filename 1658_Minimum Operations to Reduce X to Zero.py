class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x

        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        
        left = 0
        right = 0
        window_sum = 0
        max_length = -1
        while right < len(nums):
            window_sum += nums[right]
            right += 1
            while window_sum >= target:
                if window_sum == target:
                    max_length = max(max_length, right - left)

                window_sum -= nums[left]
                left += 1

        return -1 if max_length == -1 else len(nums) - max_length



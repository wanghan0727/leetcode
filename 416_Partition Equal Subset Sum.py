class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if len(nums) < 2:
            return False

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target+1)
        # dp[0] = True

        for n in nums:
            if n > target:
                return False

            elif n == target:
                return True

            for j in range(target, n-1, -1):
                if j == n:
                    dp[j] = True
                else:
                    dp[j] = dp[j] or dp[j-n]

            if dp[target]:
                return True

        return dp[target]
        
#method 1
class Solution:
    def fib(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]

        for i in range(n+1):
            if i == 0:
                dp[i] = 0
            elif i == 1:
                dp[i] = 1
            else:
                dp[i] = dp[i-1] +dp[i-2]

        return dp[-1]

#method 2
class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        elif n ==1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        if not s:
            return []

        self.ans = []
        self.dfs(s, [], 0, len(s))

        return self.ans

    def dfs(self, s, partitions, start, end):

        if start >= end:
            self.ans.append(list(partitions))
            return

        for idx in range(start, end):
            split_s = s[start: idx+1]

            if self.is_palindrome(split_s):
                partitions.append(split_s)
                self.dfs(s, partitions, idx+1, end)
                partitions.pop()

        return


    def is_palindrome(self, s):

        start = 0
        end = len(s) - 1
        while(start <= end and s[start] == s[end]):
            start += 1
            end -= 1

        else:
            if start <= end:
                return False
            else:
                return True
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            res = 0

        else:
            res = 0
            tmp_lst = []
            left = 0

            for right in range(len(s)):

                while s[right] in tmp_lst:
                    tmp_lst.pop(0)
                    left += 1

                tmp_lst.append(s[right])

                if right - left + 1 > res:
                    res = right - left + 1

        return res
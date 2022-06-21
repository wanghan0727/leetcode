class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        nums = len(heights)
        lst = []
        
        for i in range(1, nums):
            dif = heights[i] - heights[i-1]
            if dif > 0:
                heapq.heappush(lst, dif)
                if len(lst) > ladders:
                    bricks -= heapq.heappop(lst)
                if bricks < 0:
                    return i - 1
        
        return nums - 1
                    
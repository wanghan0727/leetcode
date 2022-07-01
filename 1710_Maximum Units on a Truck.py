class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        res = 0
        for number, unit in sorted(boxTypes, key=lambda d:d[1], reverse=True):
            if truckSize >= number:
                res += number * unit
                truckSize -= number
            
            else:
                res += truckSize * unit
                break
            
            
        return res
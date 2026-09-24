class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n = len(grid)
        total_numbers = n * n
        seen = set()
        
        a = -1  
        b = -1  
        
       
        for row in grid:
            for val in row:
                if val in seen:
                    a = val
                else:
                    seen.add(val)
        
        
        for i in range(1, total_numbers + 1):
            if i not in seen:
                b = i
                break
                
        return [a, b]
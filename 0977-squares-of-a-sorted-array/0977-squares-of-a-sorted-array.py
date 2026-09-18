class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        squared = [x * x for x in nums]
        squared.sort()
        return squared
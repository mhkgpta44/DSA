class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # expected_sum = n * (n + 1) // 2
        # actual_sum = sum(nums)
        # return expected_sum - actual_sum
        n=len(nums)
        for number in range(n+1):
                if number not in nums:
                    return number
        
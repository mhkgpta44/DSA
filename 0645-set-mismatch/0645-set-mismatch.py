class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        # miss=-1
        # dup=-1
        # for i in range(1,len(nums)+1):
        #     count=0
        #     for j in range(0,len(nums)):
        #         if nums[j]==i:
        #             count+=1
        #     if count==0:
        #         miss=i
        #     elif count==2:
        #         dup=i
        # return [dup,miss]

        freq=[0]*(len(nums)+1)
        miss=-1
        dup=-1
        for i in range(len(nums)):
            freq[nums[i]]+=1
        for i in range(1,len(freq)):
            if freq[i]==0:
                miss=i
            elif freq[i]==2:
                dup=i
        return[dup,miss]
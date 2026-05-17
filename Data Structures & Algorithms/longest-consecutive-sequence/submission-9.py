class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        nums = list(sorted(set(nums)))
        count = 1
        lar = 1
        print(nums)
        for i in range(len(nums)-1):
            temp = nums[i]+1
            print(f"----{count}----")
            print(temp)
            print(nums[i+1])
            if nums[i]+1 == nums[i+1]:
                count += 1
            else:
                if count>lar:
                    lar = count
                count = 1
        return count if count>lar else lar
            
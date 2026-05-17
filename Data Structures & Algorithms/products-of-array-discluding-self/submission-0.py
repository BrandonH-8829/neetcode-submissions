class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        for k in range(len(nums)):
            total = 1
            for i in range(len(nums)):
                if k != i:
                    total = nums[i] * total
            output[k] = total

        return output
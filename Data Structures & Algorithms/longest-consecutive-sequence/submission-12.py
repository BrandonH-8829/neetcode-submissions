class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        nums = set(nums)
        count = 1
        largest = 1
        #print(nums)
        for num in nums:
            if (num-1) not in nums:
                length = 1
                while (num + length) in nums:
                    length += 1
                if length > largest:
                    largest = length
        return largest
            
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = [0]*2
        back = len(numbers) - 1
        front = 0
        while front <= back:
            if (numbers[front] + numbers[back]) == target:
                nums[0] = front+1
                nums[1] = back+1
                return nums
            elif (numbers[front] + numbers[back]) > target:
                back -= 1
            else:
                front += 1
        return nums
1.class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        range_sum = n * (n + 1) // 2
        list_sum = sum(nums)
        return range_sum - list_sum 

2.arr = [1, 2, 3, 4, 5]
left, right = 0, len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr) 

3.class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

4.class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        j = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j 

5.class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] , nums[right] = nums[right] , nums[left]
                left += 1
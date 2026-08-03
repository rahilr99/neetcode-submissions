class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_counter = 1
        if len(nums) == 1:
            return 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[unique_counter] = nums [i]
                unique_counter +=1
        nums[unique_counter:] = [None]*(len(nums)-unique_counter)
        return unique_counter

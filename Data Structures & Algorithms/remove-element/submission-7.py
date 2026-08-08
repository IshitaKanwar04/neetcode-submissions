class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # possible solution 
        # val_count = 0
        # i = 0
        # while i < len(nums):
        #     if nums[i] == val:
        #         val_count += 1
        #         nums.pop(i)
        #         # Don't increment i - re-check this position
        #     else:
        #         i += 1
        # return len(nums)  
        

        #efficient using 2 pointers
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k 

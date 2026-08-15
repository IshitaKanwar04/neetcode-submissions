class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # only works for positives
        # i = 0
        # j = len(nums) - 1 

        # while(i<j):
        #     if nums[i] + nums[j] > target:
        #         j -= 1 
        #     elif nums[i] + nums[j] < target:
        #         i += 1
        #     else:
        #         return[i, j]

        #using hash map
        value_index_map  = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in value_index_map.keys():
                return [value_index_map[diff], i]
            else:
                value_index_map[nums[i]] = i

                
                
        
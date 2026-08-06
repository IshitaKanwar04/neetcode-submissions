class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        consecutive_count_set = {0}
        for i in nums:
            if i == 1:
                count += 1
            elif i != 1 and count > 0:
                consecutive_count_set.add(count)
                count = 0
        
        consecutive_count_set.add(count)
        return sorted(consecutive_count_set, reverse = True)[0]
            




        
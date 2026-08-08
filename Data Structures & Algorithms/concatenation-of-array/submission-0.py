class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = [0]*2*len(nums)
        # n = len(nums)
        # for i in range(n):
        #     ans[i] = ans[n+i+1] = nums[i]
        # return ans

        ans = nums
        ans.extend(nums)
        return ans
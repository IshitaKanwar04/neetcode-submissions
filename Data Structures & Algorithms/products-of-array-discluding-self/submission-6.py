class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for i in  range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
                continue
            product *= nums[i]

        if zero_count> 1 :
            return [0] * len(nums)

        output = []
        for i in range(len(nums)):
            cp = product
            if nums[i] == 0:
                output.append(product)
            elif zero_count == 1:
                output.append(0)
            else:
                output.append(cp//nums[i])
        return output


        
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            largest_sub_array_element = sorted(arr[i+1:])[-1] 
            arr[i] = largest_sub_array_element
        arr[-1] = -1
        return arr

        
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_tbl = defaultdict(int)
        for num in nums:
            count_tbl[num] += 1

        return sorted(count_tbl, key =count_tbl.get, reverse = True)[:k]

        
        
        
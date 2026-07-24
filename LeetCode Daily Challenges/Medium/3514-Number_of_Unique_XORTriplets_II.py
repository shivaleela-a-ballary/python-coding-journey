from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1

        pair_xors = set()

        # XOR of every pair of distinct elements
        for i in range(n):
            for j in range(i + 1, n):
                pair_xors.add(nums[i] ^ nums[j])

        triplets = set(nums)  # covers x ^ x ^ x = x

        # pair XOR ^ third element
        for x in pair_xors:
            for num in nums:
                triplets.add(x ^ num)

        return len(triplets)
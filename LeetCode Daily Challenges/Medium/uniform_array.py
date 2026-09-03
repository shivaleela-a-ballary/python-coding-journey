class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # If all elements are even, keep them as they are.
        if all(x % 2 == 0 for x in nums1):
            return True

        # If the minimum element is odd,
        # every even element can subtract it to become odd.
        if min(nums1) % 2 == 1:
            return True

        return False

class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)

        # Prefix sums
        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        # If Alice takes all stones, her score difference is prefix[n-1]
        dp = prefix[n - 1]

        # Try every possible point where the first player can stop merging
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)

        return dp
      

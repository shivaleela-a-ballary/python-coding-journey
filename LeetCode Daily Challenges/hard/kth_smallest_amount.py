from math import gcd


class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:

        # Remove redundant coins.
        # If a coin is a multiple of another coin, it adds no new amounts.
        coins.sort()
        useful = []

        for c in coins:
            if not any(c % d == 0 for d in useful):
                useful.append(c)

        coins = useful
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            """
            Count distinct positive amounts <= x
            that are divisible by at least one coin.
            """
            total = 0

            # Inclusion-Exclusion over all subsets
            for mask in range(1, 1 << n):
                current_lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        current_lcm = lcm(current_lcm, coins[i])

                        # No need to continue if LCM > x
                        if current_lcm > x:
                            valid = False
                            break

                if not valid:
                    continue

                multiples = x // current_lcm

                if bits % 2 == 1:
                    total += multiples
                else:
                    total -= multiples

            return total

        # The answer cannot be larger than min(coins) * k
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left

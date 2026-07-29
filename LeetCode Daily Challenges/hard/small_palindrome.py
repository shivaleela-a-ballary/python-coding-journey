from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        half = {}
        mid = ""
        half_len = 0

        for ch in sorted(freq):
            if freq[ch] % 2:
                mid = ch
            half[ch] = freq[ch] // 2
            half_len += half[ch]

        fact = [1] * (half_len + 1)
        for i in range(1, half_len + 1):
            fact[i] = fact[i - 1] * i

        ways = fact[half_len]
        for c in half.values():
            ways //= fact[c]

        if ways < k:
            return ""

        ans = []
        T = half_len

        while T:
            for ch in sorted(half):
                if half[ch] == 0:
                    continue

                cnt = half[ch]
                cand = ways * cnt // T

                if cand >= k:
                    ans.append(ch)
                    half[ch] -= 1
                    ways = cand
                    T -= 1
                    break
                else:
                    k -= cand

        left = "".join(ans)
        return left + mid + left[::-1]
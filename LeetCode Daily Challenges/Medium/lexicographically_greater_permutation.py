class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Frequency of characters in s
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        best = None

        # Prefix that matches target
        prefix = []

        for i in range(n):
            t = ord(target[i]) - ord('a')

            # Try making the first difference at position i
            # using the smallest possible character > target[i].
            for c in range(t + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1

                    candidate = ''.join(prefix) + chr(c + ord('a'))

                    # Append all remaining characters in sorted order
                    for x in range(26):
                        candidate += chr(x + ord('a')) * cnt[x]

                    if best is None or candidate < best:
                        best = candidate

                    cnt[c] += 1

            # Try to keep matching target[i]
            if cnt[t] == 0:
                break

            cnt[t] -= 1
            prefix.append(target[i])

        return best if best is not None else ""

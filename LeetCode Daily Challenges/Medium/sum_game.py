class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        diff = 0
        q_diff = 0

        for i, ch in enumerate(num):
            if ch == '?':
                q_diff += 1 if i < half else -1
            else:
                diff += int(ch) if i < half else -int(ch)

        if q_diff % 2 != 0:
            return True

        return diff != -9 * (q_diff // 2)

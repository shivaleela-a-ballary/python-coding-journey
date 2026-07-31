from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        
        # Sort frequencies in descending order
        frequencies = sorted(freq.values(), reverse=True)
        
        pushes = 0
        
        for i, f in enumerate(frequencies):
            cost = (i // 8) + 1   # every 8 letters cost increases
            pushes += f * cost
        
        return pushes
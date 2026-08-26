def shortestBeautifulSubstring(s: str, k: int) -> str:
    n = len(s)
    best = ""

    for left in range(n):
        ones = 0

        for right in range(left, n):
            if s[right] == '1':
                ones += 1

            if ones == k:
                current = s[left:right + 1]

                # First valid substring
                if best == "":
                    best = current

                # Shorter substring is better
                elif len(current) < len(best):
                    best = current

                # Same length -> lexicographically smaller
                elif len(current) == len(best) and current < best:
                    best = current

                # Since adding more characters can only make
                # the substring longer, stop this left position.
                break

    return best
  

from collections import deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        # Find S and number the litter cells
        start_r = start_c = 0
        litter_id = {}

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = len(litter_id)

        k = len(litter_id)

        # No litter to collect
        if k == 0:
            return 0

        full_mask = (1 << k) - 1

        # best[r][c][mask] = maximum energy remaining
        # when we reach (r, c) with this mask
        best = [
            [[-1] * (1 << k) for _ in range(n)]
            for _ in range(m)
        ]

        queue = deque()

        # row, col, collected_mask, remaining_energy
        queue.append((start_r, start_c, 0, energy))
        best[start_r][start_c][0] = energy

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        moves = 0

        while queue:

            # Process one BFS level
            for _ in range(len(queue)):

                r, c, mask, curr_energy = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Outside grid
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    # Obstacle
                    if classroom[nr][nc] == 'X':
                        continue

                    # Cannot move with zero energy
                    if curr_energy == 0:
                        continue

                    # One move costs 1 energy
                    new_energy = curr_energy - 1
                    new_mask = mask

                    # Collect litter
                    if classroom[nr][nc] == 'L':
                        bit = litter_id[(nr, nc)]
                        new_mask |= (1 << bit)

                    # Reset energy at R
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    # All litter collected
                    if new_mask == full_mask:
                        return moves + 1

                    # We already reached this state with
                    # more or equal energy
                    if best[nr][nc][new_mask] >= new_energy:
                        continue

                    best[nr][nc][new_mask] = new_energy

                    queue.append(
                        (nr, nc, new_mask, new_energy)
                    )

            moves += 1

        return -1

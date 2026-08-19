class Solution:
    def maximumGap(self, nums):
        n = len(nums)

        if n < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)

        if min_val == max_val:
            return 0

        # Minimum possible bucket gap
        gap = max(1, (max_val - min_val + n - 2) // (n - 1))

        bucket_count = (max_val - min_val) // gap + 1

        # Each bucket stores [minimum, maximum]
        buckets = [[float('inf'), float('-inf')]
                   for _ in range(bucket_count)]

        # Put numbers into buckets
        for num in nums:
            index = (num - min_val) // gap

            buckets[index][0] = min(buckets[index][0], num)
            buckets[index][1] = max(buckets[index][1], num)

        answer = 0
        previous_max = min_val

        # Find maximum gap between non-empty buckets
        for bucket_min, bucket_max in buckets:
            if bucket_min == float('inf'):
                continue

            answer = max(answer, bucket_min - previous_max)
            previous_max = bucket_max

        return answer

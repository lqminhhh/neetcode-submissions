class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        bucket = [[] for _ in range(len(nums) + 1)]
        
        for key, val in freq.items():
            bucket[val].append(key)
        
        output = []
        count = 0

        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                for j in range(len(bucket[i])):
                    count += 1
                    output.append(bucket[i][j])
            if count == k:
                return output
        return output
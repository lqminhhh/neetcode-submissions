class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        output = []

        for num in nums:
            freq[num] += 1

        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse = True))

        for key, val in sorted_freq.items():
            if len(output) == k:
                return output
            output.append(key)

        return output
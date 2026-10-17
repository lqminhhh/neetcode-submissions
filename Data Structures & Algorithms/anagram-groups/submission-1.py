class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # solution 2: hash table
        # time:
        # space:
        freq = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for i in range(len(s)):
                count[ord(s[i]) - ord('a')] += 1
            key_val = tuple(count)
            freq[key_val].append(s)
        return list(freq.values())

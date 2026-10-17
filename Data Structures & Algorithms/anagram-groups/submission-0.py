class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # solution 1: sorting
        # time: O(m * nlogn)
        # space: O(m * n)
        
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # solution 2: sweep line algorithm

        df = defaultdict(int)
        for start, end in intervals:
            df[start] += 1
            df[end] -= 1
        
        overlap = 0
        interval = []
        output = []
        
        for key in sorted(df):
            if not interval:
                interval = [key]
            overlap += df[key]
            if overlap == 0:
                interval.append(key)
                output.append(interval)
                overlap = 0
                interval = []
        return output
            
            
            

                
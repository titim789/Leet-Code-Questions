class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals = sorted(intervals, key=lambda x:x[0])
        for i in range(len(intervals)):
            if not ans:
                ans.append(intervals[i])
            
            elif ans[-1][1] >= intervals[i][0]:
                if ans[-1][1] >= intervals[i][1]:
                    continue
                else:
                    ans[-1][1] = intervals[i][1]
            else:
                ans.append(intervals[i])
        return ans
                
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]

        ans = []
        inserted = False

        for i in range(len(intervals)):
            if inserted:
                if ans[-1][1] < intervals[i][0]:
                    ans.append(intervals[i])
                else:
                    if ans[-1][0] <= intervals[i][0]:
                        if ans[-1][1] >= intervals[i][1]:
                            continue
                        else:
                            ans[-1][1] = intervals[i][1]
                    else:
                        if ans[-1][1] >= intervals[i][1]:
                            ans[-1][0] = intervals[i][0]
                        else:
                            ans[-1] = intervals[i]
            else:
                if newInterval[0] > intervals[i][0]:
                    if newInterval[0] > intervals[i][1]:
                        ans.append(intervals[i])
                        continue
                    else:
                        if newInterval[1] >= intervals[i][1]:
                            ans.append([intervals[i][0],newInterval[1]])
                        else:
                            ans.append(intervals[i])
                elif newInterval[0] < intervals[i][0]:
                    if newInterval[1] < intervals[i][0]:
                        ans += [newInterval, intervals[i]]
                    else:
                        if newInterval[1] >= intervals[i][1]:
                            ans.append(newInterval)
                        else:
                            ans.append([newInterval[0], intervals[i][1]])
                else:
                    ans.append([newInterval[0], max(newInterval[1], intervals[i][1])])

                inserted = True

        if not inserted:
            ans.append(newInterval)

        
        return ans
        
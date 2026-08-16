class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort based on start
        intervals.sort(key=lambda interval: interval[0])
        output = [intervals[0]]

        for start, end in intervals:
            prev_end = output[-1][1]

            # if there is an overlap
            if start <= prev_end:
                output[-1][1] = max(prev_end, end)
            else:
                output.append([start, end])
        return output
from typing import List


def merge_overlapping_intervals(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for interval in intervals:
        curr_interval = result[-1]
        if curr_interval[0] <= interval[0] <= curr_interval[1]:
            curr_interval[1] = max(interval[1], curr_interval[1])
        else:
            result.append(interval)
    return result

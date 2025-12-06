"""
Idea:
i =  0        1         2        3
  (3, 5), (10, 14), (12, 18), (16, 20) <-- list of intervals
-> 5 < 10, 5 < 12, 5 < 16 -> 
    intervals = (3, 5), (10, 14), (12, 18), (16, 20) 
    (no merges, check from next interval (10, 14))

-> 14 > 12 and 14 < 18 -> 
    new_interval = (3, 5), (10, 18), (16, 20) 
    (10, 14) U (12, 18) = (10, 18) (1 merge)
    start checking for merges from the current merged interval, i.e (10, 18)

-> 18 > 16 and 18 < 20 -> 
    new_intervals = (3, 5), (10, 20) (1 merge, check from (10, 20))

(10, 20) is the last interval in the list -> so just return the sum of current intervals

if a current interval cannot be merged with the next one, it cannot be merged with any
of the following ones because we have sorted them in ascending order, and to merge 2 intervals,
the upper limit of the first must be >= the lower limit of the second

when you merge 2 interval, delete the second one, and replace the first one with the merged interval
"""

def merge_intervals_recursively(intervals, current_ind = 0):
    if current_ind >= len(intervals) - 1: #the end of the intervals list
        sum_intervals = 0
        for lower, upper in intervals:
            sum_intervals += (upper - lower + 1)

        return sum_intervals

    else:
        current_lower, current_upper = intervals[current_ind][0], intervals[current_ind][1]
        next_lower, next_upper = intervals[current_ind+1][0], intervals[current_ind+1][1]

        if current_upper >= next_lower and current_upper <= next_upper:
            del intervals[current_ind+1]
            intervals[current_ind] = (current_lower, next_upper)
            return merge_intervals_recursively(intervals, current_ind)

        elif current_upper >= next_lower and current_upper >= next_upper:
            del intervals[current_ind+1]
            intervals[current_ind] = (current_lower, current_upper)
            return merge_intervals_recursively(intervals, current_ind)

        else:
            return merge_intervals_recursively(intervals, current_ind+1)
        

def main():
    data = ""

    with open("src/2025/day05/day05_ingredients_data.txt") as file:
        data = file.read()
        
    intervals_str, ingredients_str = data.split("\n\n")
    intervals = intervals_str.split("\n")

    for i in range(len(intervals)):
        lower_limit, upper_limit = intervals[i].split("-")
        intervals[i] = (int(lower_limit), int(upper_limit))
    
    sorted_intervals = sorted(intervals)
    sum_intervals = merge_intervals_recursively(sorted_intervals)

    print("Sum interval:", sum_intervals)

if __name__ == "__main__":
    main()
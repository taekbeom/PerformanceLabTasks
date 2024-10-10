import statistics as st
import sys

nums_file = sys.argv[1]

with open(nums_file, 'r') as file:
    nums = [int(line.strip()) for line in file]

    m = int(st.median(nums))

    steps = sum(abs(num-m) for num in nums)

print(steps)

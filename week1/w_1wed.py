def max_crossing_sum(arr, left, mid, right):
    # Include elements on left of mid
    total = 0
    left_sum = -10**18
    for i in range(mid, left - 1, -1):
        total += arr[i]
        left_sum = max(left_sum, total)
    # Include elements on right of mid
    total = 0
    right_sum = -10**18
    for i in range(mid + 1, right + 1):
        total += arr[i]
        right_sum = max(right_sum, total)
    return left_sum + right_sum

def max_subarray_sum(arr, left, right):
    # Base case: only one element
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    # Maximum subarray sum in left half
    left_max = max_subarray_sum(arr, left, mid)
    # Maximum subarray sum in right half
    right_max = max_subarray_sum(arr, mid + 1, right)
    # Maximum subarray sum crossing the midpoint
    cross_max = max_crossing_sum(arr, left, mid, right)
    return max(left_max, right_max, cross_max)

# Driver code
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_subarray_sum(arr, 0, n - 1))

#Sample Input 
#1 
#9 -2  1 -3  4  -1  2  1  -5 4 
#Expected Output 
#6
    
    
# Job Sequencing with Deadlines (Greedy)
t = int(input())  # number of test cases
for _ in range(t):
    n = int(input())  # number of jobs
    jobs = []
    max_deadline = 0
    for _ in range(n):
        d, p = map(int, input().split())
        jobs.append((d, p))
        max_deadline = max(max_deadline, d)
    # Sort jobs by profit (descending)
    jobs.sort(key=lambda x: x[1], reverse=True)
    # Track slots (0 means free)
    slots = [0] * (max_deadline + 1)
    jobs_done = 0
    total_profit = 0
    for d, p in jobs:
        # Find a free slot before or at deadline
        for j in range(d, 0, -1):
            if slots[j] == 0:
                slots[j] = 1
                jobs_done += 1
                total_profit += p
                break
    print(jobs_done, total_profit)

#Sample Input
#1
# 5
# 2 100
# 1 19
# 2 27
# 1 25
# 3 15
#Expected Output
#3 142

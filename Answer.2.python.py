def min_distance(stalls, k):
    stalls.sort()
    low, high = 1, stalls[-1] - stalls[0] + 1

    while low < high:
        mid = low + (high - low) // 2
        if is_valid(stalls, k, mid):
            low = mid + 1
        else:
            high = mid

    return low - 1

def is_valid(stalls, k, min_dist):
    count = 1
    curr_pos = stalls[0]
    for stall in stalls:
        if stall - curr_pos >= min_dist:
            count += 1
            curr_pos = stall
    return count >= k

# Test the function
stalls = [1, 2, 4, 8, 9]
k = 3
print(min_distance(stalls, k))  # Output: 3

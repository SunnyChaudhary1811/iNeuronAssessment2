def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            k, l = j + 1, n - 1
            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]
                if total == target:
                    result.append([nums[i], nums[j], nums[k], nums[l]])
                    while k < l and nums[k] == nums[k + 1]:
                        k += 1
                    while k < l and nums[l] == nums[l - 1]:
                        l -= 1
                    k += 1
                    l -= 1
                elif total < target:
                    k += 1
                else:
                    l -= 1

    return result

# Test the function
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

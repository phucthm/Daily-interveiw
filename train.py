def findKthLargest(nums, k):
    for i in range(k-1):
        nums.remove(max(nums))
    return max(nums)


def findKthLargest2(nums, k):
    nums.sort()
    return nums[-k]


print(findKthLargest2([3, 5, 2, 4, 6, 8, 8], 3))

def rob(nums) -> int:
    if len(nums) == 2:
        return max(nums[0],nums[1])
    if len(nums) == 1:
        return nums[0]
    
    
    dp = [None for i in range(len(nums)+1)]
    dp[0], dp[1], dp[2] = 0, nums[0], nums[1]
    for i in range(3, len(nums)+1):
        dp[i] = nums[i-1] + max(dp[i-2],dp[i-3])

    return max(dp[-1], dp[-2])

print(rob([1,2,3,1]))

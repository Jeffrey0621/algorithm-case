def maxsum(nums):
	if max(nums) < 0:
		return max(nums)
	if min(nums) > 0:
		return sum(nums)
	current_sum = 0
	greater_sum = 0
	for item in nums:
		if current_sum > 0:
			current_sum += item
		else:
			current_sum = item
		if current_sum > greater_sum:
			greater_sum = current_sum
		
	return greater_sum

def maxSubArray(nums):
        size = len(nums)
        if size == 0:
                return None
        if size == 1:
                return nums[0]
        dp = [i for i in range(size)]
        dp[0] = nums[0]
        for i in range(1,size):
                dp[i] = max(nums[i],dp[i-1]+nums[i])
        return max(dp)


if __name__ == "__main__":
	nums = [2, 3, -4, 10, -8, 9]
	result = maxsum(nums)
	print(result)
	print(maxSubArray(nums))

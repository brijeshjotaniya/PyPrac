def has_33(nums: list) -> bool:
	for i in range(1,len(nums)):
		if nums[i-1]==nums[i]==3:
			return True
	else:
		return False

if __name__ == '__main__':
	nums = [1,2,3,3]
	print(has_33(nums))
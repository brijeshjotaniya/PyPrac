def has_33(nums: list) -> bool:
	for i in range(len(nums)):
		if nums[i]==nums[i+1]==3:
			return True
	else:
		return False

if __name__ == '__main__':
	nums = [1,2,3,3]
	print(has_33(nums))
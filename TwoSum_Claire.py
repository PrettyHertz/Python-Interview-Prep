class Solution(object):
	def twoSum(nums, target):
		sol = []
		slv = False
		for i in range(0, len(nums)):
			com = target - nums[i]
			if com in nums:
				sol.append(i)
				slv = True
				break
		if slv == True:
			for i in range(0, len(nums)):
				if nums[i] == com:
					sol.append(i)
					break
			print(str(target - com) + "+" + str(com) + "=" + str(target) + ".")
			return sorted(sol)
		else:
			return "No solution found."
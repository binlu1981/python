class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		dict = {}
		for i in xrange(0,len(nums)):
			# x = nums[i]
			#dict[nums[i]] = i #wrong, put here will add itself value
			if target-nums[i] in dict:
				return (dict[target-nums[i]], i)
			dict[nums[i]] = i #right, put here will not add itself value

class Solution1(object):
	def twoSum(self, nums, target):
		for i in range(0,len(nums)):
			# rests=target-nums[i]
			if target-nums[i] in nums[i+1:]:
				return [i,nums.index(target-nums[i],i+1)]
	

class Solution2(object):
	def twoSum(self,nums,target):
		for i in range(len((nums))-1):
			for j in range(i+1,len((nums))):
				if nums[j] == target-nums[i]:
					return [i,j]
		


	
	
nums=[0,4,3,0]
target=0
s=Solution()
s1=Solution1()
s2=Solution2()
print s1.twoSum(nums,target)
print s.twoSum(nums,target)
print s2.twoSum(nums,target)




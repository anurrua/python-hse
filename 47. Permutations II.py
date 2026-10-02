class Solution(object):
    def permuteUnique(self, nums):
        result = set()
        def generate(nums,path):
            if not nums:
                result.add(tuple(path))
                return
            for i in range(len(nums)):
                generate(nums[:i]+nums[i+1:],path+[nums[i]])
        generate(nums,[])
        return [list(x) for x in result]
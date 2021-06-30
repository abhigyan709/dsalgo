class SolutionTwoSum:
    def twoSum(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[sum] = i
            else:
                return [h[n], i]
Class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        last = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[last]:
                last +=1
                nums[last] = nums[i]
        return last+1
        

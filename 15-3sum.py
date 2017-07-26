Class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_dict, result, result_set = {}, [], set([])
        for n in nums:
            num_dict[n]= num_dict[n]+1 if n in num_dict else 1
        unums = []
        for un in num_dict:
            unums.append(un)
        for a in unums:
            for b in unums:
                #a, b = nums[i], nums[j]
                if a == b and num_dict[a] == 1:
                    continue
                c = 0-a-b
                if c in num_dict:
                    count = num_dict[c]
                    if a == c:
                        count-=1
                    if b == c:
                        count-=1
                    if count > 0:
                        rlist = sorted([a,b,c])
                        if (rlist[0],rlist[1]) not in result_set:
                            result.append(rlist)
                            result_set.add((rlist[0], rlist[1]))
        return result
        
        
        

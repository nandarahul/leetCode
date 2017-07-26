Class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        for i in xrange(len(haystack)-len(needle)+1):
            for j in xrange(len(needle)+1):
                if j == len(needle):
                    return i
                if haystack[i+j] != needle[j]:
                    break
        return -1
   

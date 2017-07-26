Class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mystack = []
        for brack in s:
            if brack in ('(', '[','{'):
                mystack.append(brack)
            elif len(mystack) > 0 and ((brack == ')' and mystack[-1] == '(') or (brack==']' and mystack[-1]=='[')\
                 or (brack=='}' and mystack[-1]=='{')):
                    mystack.pop()
            else:
                return False
        return len(mystack) == 0

# Iterative Solution
Class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dig_dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno',
                     '7':'pqrs', '8':'tuv', '9':'wxyz', '0':' '}
        if digits == "":
            return []
        final_result = ['']
        for d in digits:
            result = final_result
            final_result = []
            for r in result:
                for char in dig_dict[d]:
                    final_result.append(r+char)
        return final_result

# Recursive Solution
class Solution(object):
    def __init__(self):
        self.dig_dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno',
                      '7':'pqrs', '8':'tuv', '9':'wxyz', '0':' '}

    def letterCombinations(self, digits):
        if digits == "":
            return []
        return self.letterCombinationsMain(digits)
   
    def letterCombinationsMain(self, digits):
        if digits == "":
            return ['']
        result = self.letterCombinationsMain(digits[1:])
        new_result = []
        for r in result:
            for ch in self.dig_dict[digits[0]]:
                new_result.append(ch+r)
        return new_result

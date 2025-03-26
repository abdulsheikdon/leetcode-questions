class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False  #to catch negative numbefs

        return str(x)== str(x)[::-1] #flips, compare, and return

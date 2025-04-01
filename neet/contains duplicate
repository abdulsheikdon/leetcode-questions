#my initial brute solution O(n^2):
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         #traverse through array
        dupCount = 0
        #for loop
        for i in range(len(nums)):
            checkEl = nums[i]
            for j in range(i + 1, len(nums)):
                if checkEl == nums[j]:
                    dupCount += 1
            

        if dupCount > 0:
            return True
        else:
            return False


#faster run time solution O(nlogn):
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = False
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==nums[i-1]:
                dup = True
        return dup
    
#fastest O(n):
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = set()
        for i in range(len(nums)):
            if nums[i] in hash:
                return True
            hash.add(nums[i])
        return False

# Recursion Problems

""" Organizational Structure:
        - Problem name, link to where I found it  with its explanation, this will be a direct copy of Leetcode or whichever resource I state as it belonging to.  
        - Sample input and output, could include constraints.
        - Diagram that represents the solution with the actual code. The first solution will be mine, sometimes I will update newer solutions and very often will copy solutions that I will break down.
        - For each solution I will submit it and see how it matches up in that platform, do this 5 times, write down how much it changes between submissions, make an average and leave it with that score. The goal is to compare how the code matches up and also start developing a sense of where the code was losing time or gaining time, or when it used more memory or didnt required more.
        - I will write down how many tests it passed based on the submission data.

This will be repeated for some number of problems, not sure how many but likely a lot.
""" 

'''416. Partition Equal Subset Sum, https://leetcode.com/problems/partition-equal-subset-sum/
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


'''
'''Insights,
        - it must be partitioned into two subsets, both subsets must be equal to the same
        - the sum must be an even number, otherwise its False
        - I must figure out now how to partition this, memoization seems to be the key possibility to use 

Diagramming + Logic,

nums = [ 1 , 5 , 11 , 5 ]

partition1 = 1 + 5 + 5 == 11
partition2 = 11

partition1 == partition2
    True 

Output: true

'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        #Attempt 5, not mine, time wise at 94.21% and memory wise at 42.82% of all submissions 
        '''
        @cache
        def subsetSum(s, i):
            if s == 0: return True
            if i >= len(nums) or s < 0: return False
            return subsetSum(s-nums[i], i+1) or subsetSum(s, i+1)
        
        
        total_sum = sum(nums)
        
        
        return total_sum & 1 == 0 and subsetSum(total_sum // 2, 0)
        '''
        
        #Attempt 4, not mine, time wise at 50.99% and memory wise at 6.88% of all submissions
        '''
        if sum(nums)%2 == 1: return False
        memo = {}

        def dfs(i, target):
            if target == 0: return True
            if target < 0 or i == len(nums): return False
            if (i, target) in memo: return memo[(i, target)]

            if dfs(i+1, target - nums[i]) or dfs(i+1, target):
                memo[(i, target)] = True
                return True
            memo[(i, target)] = False
            return memo[(i, target)]

        return dfs(0, sum(nums)//2)
        '''
        
        #Attempt 3, not mine, time wise at 5.02% and memory wise at 8.00% of all submissions
        '''
        numSum = sum(nums)
        n = len(nums)
        s1, s2 = 0, 0
        if numSum % 2 != 0: return False
        s1 = numSum/2
        s2 = numSum/2
        lookup = {}
        def f(index, target, lookup):
            
            if target == 0: return True
            
            if index == 0: return (nums[0] == target)
            
            if (index, target) in lookup: return lookup[(index, target)]
            
            notTake = f(index-1, target, lookup)
            
            take = False
            if target >= nums[index]:
                take = f(index-1, target-nums[index], lookup)
                
            lookup[(index, target)] = take or notTake
            
            return lookup[(index, target)]
        
        return f(n-1, s1, lookup)
        '''
        #Attempt 2, not mine, 138/139 test cases pass, fails at test case [1,2,3,5,17,6,14,12,6] 
        '''
        res = self.solve(nums,0,0,sum(nums),len(nums),{})
        return res
        
    def solve(self,arr,s,index,total,n,dic):
        
        if s in dic:
            return dic[s]
        
        if s == total-s:
            return True
        
        if index > n-1:
            return False
        
        dic[s] = self.solve(arr,s+arr[index],index+1,total,n,dic) or self.solve(arr,s,index+1,total,n,dic)
        
        return dic[s]
        '''
        
        #Attempt 1, mine 
        '''
        if sum(nums) % 2:
            return False
        return True
        '''

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
        - 
        
Diagramming + Logic,

nums = [ 1 , 5 , 11 , 5 ]



Output: true

nums = [ 1 , 2 , 3 , 5 ]



Output: false
'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        #Solution 5, not mine, time wise at 16.03% and memory wise at 35.19% of all submissions 

        if len(nums) < 2:
            return False
        value_sum = sum(nums)
        if value_sum % 2 == 1:
            return False
        m = len(nums)
        n = value_sum // 2

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m][n]
        
        #Solution 4, not mine, time wise at 29.40% and memory wise at 97.52% of all submissions 
        '''
        if len(nums) < 2:
            return False
        value_sum = sum(nums)
        if value_sum % 2 == 1:
            return False
        m = len(nums)
        n = value_sum // 2

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, m + 1):
            for j in range(n, 0, -1):
                if j >= nums[i - 1]:
                    dp[j] = dp[j] or dp[j - nums[i - 1]]
        return dp[n]
        '''
        
        #Solution 3, not mine, time wise at 23.41% and memory wise at 53.95% of all submissions 
        '''
        n = len(nums)
        dp = [set()] * n
        summation = sum(nums)
        target = float(summation / 2)
        dp[0].add(nums[0])
        
        for i in range(1, n):
            new_subset_sums = []
            for subsetsum in dp[i-1]:
                
                if(float(subsetsum) == target or float(subsetsum + nums[i]) == target):
                    return True
                new_subset_sums.append(subsetsum + nums[i])
            dp[i] = dp[i-1]
            for element in set(new_subset_sums):
                dp[i].add(element)

        return False
        '''
        
        #Solution 2, not mine, time wise at 43.16% and memory wise at 14.86% of all submissions 
        '''
        x = sum(nums)
        if x%2==1:
            return False
        value = x // 2
        res = False
        dp = [[0 for i in range(max(nums) + 1)] for j in range(value + 1)]
        def dfs(nums, value, cur):
            nonlocal res
            if res == True:
                return
            if cur == value:
                res = True
                return
            else:
                for i in range(len(nums)):
                    cur += nums[i]
                    if cur <= value and dp[cur][nums[i]] == 0:
                        dp[cur][nums[i]] = 1
                        dfs(nums[i+1:], value, cur)
                    cur -= nums[i]
            return
        dfs(nums, value, 0)
        return res
        '''
        
        #Solution 1, not mine, time wise at 54.50% and memory wise at 92.39% of all submissions 
        '''
        total_sum = sum(nums)
        if total_sum % 2: return False
        half_sum = total_sum // 2
        dp = [True] + [False]*half_sum
        for num in nums:
            for j in range(half_sum, num-1, -1):
                dp[j] |= dp[j-num]
        return dp[half_sum]
        '''
# Recursion Problems

""" Organizational Structure:
        - Problem name, link to where I found it  with its explanation, this will be a direct copy of Leetcode or whichever resource I state as it belonging to.  
        - Sample input and output, could include constraints.
        - Diagram that represents the solution with the actual code. The first solution will be mine, sometimes I will update newer solutions and very often will copy solutions that I will break down.
        - For each solution I will submit it and see how it matches up in that platform, do this 5 times, write down how much it changes between submissions, make an average and leave it with that score. The goal is to compare how the code matches up and also start developing a sense of where the code was losing time or gaining time, or when it used more memory or didnt required more.
        - I will write down how many tests it passed based on the submission data.

This will be repeated for some number of problems, not sure how many but likely a lot.
""" 
'''53. Maximum Subarray, https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

'''

'''Insights,
        - 
        
Diagramming + Logic,

nums = [ -2 , 1 , -3 , 4 , -1 , 2 , 1 , -5 , 4 ]


Output: 6

'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #Attempt3, not mine, time wise at 75.44% and memory wise at 16.08% of all submissions
        result = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            nums[i] = max(nums[i], nums[i] + nums[i+1])
            result = max(result, nums[i])
        return result
        
        #Attempt2, not mine, time wise at 86.95% and memory wise at 78.47% of all submissions
        '''
        max_sum_until_i = max_sum= nums[0]
        for i, num in enumerate(nums[1:],start=1):
            max_sum_until_i = max(max_sum_until_i+num, num)
            max_sum = max(max_sum,max_sum_until_i,max_sum)
        return max_sum
        '''
        
        #Attempt1, not mine, time wise at 64.92% and memory wise at 78.47% of all submissions
        '''
        max_sum = float(-inf)

        current_sum = 0

        for num in nums:
            current_sum = current_sum + num

            max_sum = max(max_sum , current_sum)

            if current_sum < 0:

                current_sum = 0

        return max_sum
        '''
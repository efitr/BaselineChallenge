# Recursion Problems

""" Organizational Structure:
        - Problem name, link to where I found it  with its explanation, this will be a direct copy of Leetcode or whichever resource I state as it belonging to.  
        - Sample input and output, could include constraints.
        - Diagram that represents the solution with the actual code. The first solution will be mine, sometimes I will update newer solutions and very often will copy solutions that I will break down.
        - For each solution I will submit it and see how it matches up in that platform, do this 5 times, write down how much it changes between submissions, make an average and leave it with that score. The goal is to compare how the code matches up and also start developing a sense of where the code was losing time or gaining time, or when it used more memory or didnt required more.
        - I will write down how many tests it passed based on the submission data.

This will be repeated for some number of problems, not sure how many but likely a lot.
""" 
'''76. Minimum Window Substring, https://leetcode.com/problems/minimum-window-substring/ 

        need = collections.Counter(t)            #hash table to store char frequency
        missing = len(t)                         #total number of chars we care
        start, end = 0, 0
        i = 0
        for j, char in enumerate(s, 1):          #index j from 1
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:                     #match all chars
                while i < j and need[s[i]] < 0:  #remove chars to find the real start
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1                  #make sure the first appearing char satisfies need[char]>0
                missing += 1                     #we missed this first char, so add missing by 1
                if end == 0 or j-i < end-start:  #update window
                    start, end = i, j
                i += 1                           #update i to start+1 for next window
        return s[start:end]

'''

'''Insights,
        - You can track whats being found, and when all the characters of the substring are found, reduce the window
        - 

Diagramming + Logic, 

Input: s = "ADOBECODEBANC", 
    
       t = "ABC"


Output: "BANC"



'''
def found_target(target_len):
    return target_len == 0

class Solution:
    def minWindow(self, search_string, target) -> str:
        
        #Attempt4, not mine, time wise at 30.54% and memory wise at 10.72% of all submissions
        target_letter_counts = collections.Counter(target)
        start = 0
        end = 0
        min_window = ""
        target_len = len(target)        

        for end in range(len(search_string)):
        # If we see a target letter, decrease the total target letter count
            if target_letter_counts[search_string[end]] > 0:
                target_len -= 1

            # Decrease the letter count for the current letter
            # If the letter is not a target letter, the count just becomes -ve
            target_letter_counts[search_string[end]] -= 1

            # If all letters in the target are found:
            while found_target(target_len):
                window_len = end - start + 1
                if not min_window or window_len < len(min_window):
                    # Note the new minimum window
                    min_window = search_string[start : end + 1]

                # Increase the letter count of the current letter
                target_letter_counts[search_string[start]] += 1

                # If all target letters have been seen and now, a target letter is seen with count > 0
                # Increase the target length to be found. This will break out of the loop
                if target_letter_counts[search_string[start]] > 0:
                    target_len += 1

                start+=1

        return min_window
        
        
        #Attempt3, not mine, time wise at 25.07% and memory wise at 36.34% of all submissions
        '''
        if not s or not t or len(s) < len(t):
            return ''
        
        t_counter = Counter(t)
        chars = len(t_counter.keys())
        
        s_counter = Counter()
        matches = 0
        
        answer = ''
        
        i = 0
        j = -1 # make j = -1 to start, so we can move it forward and put s[0] in s_counter in the extend phase 
        
        while i < len(s):
            
            # extend
            if matches < chars:
                
                # since we don't have enough matches and j is at the end of the string, we have no way to increase matches
                if j == len(s) - 1:
                    return answer
                
                j += 1
                s_counter[s[j]] += 1
                if t_counter[s[j]] > 0 and s_counter[s[j]] == t_counter[s[j]]:
                    matches += 1

            # contract
            else:
                s_counter[s[i]] -= 1
                if t_counter[s[i]] > 0 and s_counter[s[i]] == t_counter[s[i]] - 1:
                    matches -= 1
                i += 1
                
            # update answer
            if matches == chars:
                if not answer:
                    answer = s[i:j+1]
                elif (j - i + 1) < len(answer):
                    answer = s[i:j+1]
        
        return answer
        '''
    
        #Attempt2, not mine, time wise at 99.91% and memory wise at 36.34% of all submissions  
        '''
        # Defaultdict is very useful in this problem, though i don't like to import modules
        target_count_dict = collections.defaultdict(int)
        for ch in t:
            target_count_dict[ch] += 1
        remain_missing = len(t)
        start_pos, end_pos = 0, float('inf')
        current_start = 0
        
        # Enumerate function makes current_end indexes from 1
        for current_end, ch in enumerate(s, 1):
            # Whenever we encounter a character, no matter ch in target or not, we minus 1 in count dictionary
            # But, only when ch is in target, we minus the length of remain_missing
            # When the remain_missing is 0, we find a potential solution.
            if target_count_dict[ch] > 0:
                remain_missing -= 1
            target_count_dict[ch] -= 1
            
            if remain_missing == 0:
                # Remove redundant character
                # Try to find the fist position in s that makes target_count_dict value equals 0
                # Which means we can't skip this character in s when returning answer
                while target_count_dict[s[current_start]] < 0:
                    target_count_dict[s[current_start]] += 1
                    current_start += 1
                if current_end - current_start < end_pos - start_pos:
                    start_pos, end_pos = current_start, current_end
                
                # We need to add 1 to current_start, and the correspondence value in dictionary, is because
                # this is the first character of the potential answer. So, in future iteration, when we encounter this character,
                # We can remove this currently first character to try to find a shorter answer.
                target_count_dict[s[current_start]] += 1
                remain_missing += 1
                current_start += 1
        
        return s[start_pos:end_pos] if end_pos != float('inf') else ""
        '''
    
        #Attempt1, not mine, time wise at 62.84% and memory wise at 83.32% of all submissions  
        '''
        need = collections.Counter(t)            #hash table to store char frequency
        missing = len(t)                         #total number of chars we care
        start, end = 0, 0
        i = 0
        for j, char in enumerate(s, 1):          #index j from 1
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:                     #match all chars
                while i < j and need[s[i]] < 0:  #remove chars to find the real start
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1                  #make sure the first appearing char satisfies need[char]>0
                missing += 1                     #we missed this first char, so add missing by 1
                if end == 0 or j-i < end-start:  #update window
                    start, end = i, j
                i += 1                           #update i to start+1 for next window
        return s[start:end]
        '''

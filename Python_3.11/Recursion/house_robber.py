'''Insights,
        - you can't rob consecutive houses
        - you must figure out the most you could possibly rob without getting caught
        - there are no negative value houses
        - based on the lenght there must be a variable that represents how many can be robbed at max
            even, at most half the houses
            uneven, at most half moving the decimal up
        - you at most choose not to rob houses two house apart, otherwise it doesn make sense not robbing the one spot from you
            max(current+next,current+next_next )
            
        - the real challenge is ... I must store the current sum that seems like the most
            best_robbery = max(h[0]+h[2],h[0]+h[3])
            BUT, is the best robbery now, the next index best robbery
                best_robbery = max(h[1]+h[3],h[1]+h[4])
            total_stolen ...
                => my issue is how do I know if the best_robbery sum with the previous best_robbery stack up to be the best total_stolen

Diagramming + Logic,
Input: house_fortune = 
        [ 1 , 2 , 3 , 1 ]
Possibilities:
house_fortune[0] + house_fortune[2] => 4
house_fortune[0] + house_fortune[3] => 2
house_fortune[1] + house_fortune[3] => 3

Output: 4 => you rob house_fortune[0] + house_fortune[2]

Input: house_fortune = 
        [ 2 , 7 , 9 , 3 , 1 ]
Possibilities:
house_fortune[0] + house_fortune[3] => 5
house_fortune[0] + house_fortune[2] + house_fortune[4] => 12
house_fortune[1] + house_fortune[3] => 10
house_fortune[1] + house_fortune[4] => 8

Output: 4 => you rob house_fortune[0] + house_fortune[2]

'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        highest_val = 0
        
        for i in range(len(nums)):
            
        

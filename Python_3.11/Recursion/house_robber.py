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

Making example inputs to validate my edge cases and find a solution
    - the edge case that worries me is when I must sum the furthest then the closest but the closest while is the worst briefly then becomes the best option for total sum
    - closest means sum = house_fortune[x] + house_fortune[x+2]
    - furthest means sum = house_fortune[x] + house_fortune[x+3]
    - any other further option would make no sense to not add the closest, since there are no negative values and a 0 at worst case wouldnt affect negatively
    
    x2
    Eg. Closest, Closest
    [ 2 , 7 , 9 , 3 , 1 , 1 ]
      +       +       +       => 12
    
    Eg. Furthest, Furthest
    [ 7 , 2 , 9 , 11 , 1 , 1 , 2 ]
      +           +            +      => 20

    x3
    Eg. Closest, Furthest, Closest
    [ 2 , 7 , 9 , 11 , 1 , 1 , 2 , 1 , 1 , 1]
          +       +            +       +      => 21
          +       +        +       +       +  => 21
      
    Eg. Closest, Closest, Furthest
    [ 2 , 7 , 9 , 11 , 1 , 3 , 2 , 1 , 2 ]
          +       +        +           +      => 23
    
    x4
    Eg. Furthest, Closest, Furthest, Closest
    [ 2 , 1 , 1 , 3 , 2 , 3 , 1 , 4 , 2 , 1 , 1]x14
      +           +       +       +       +   => 13
    
    Eg. Furthest, Closest, Furthest, Furthest
    [ 1 , 2 , 1 , 1 , 4 , 1 , 2 , 1 , 3 , 4 , 1 , 1 , 7 ]x14
          +           +       +           +           +   => 19
          +           +       +       +       +       +   => 19
    
    
    Eg. Closest, Furthest, Closest, Closest
    [ 2 , 1 , 1 , 4 , 1 , 1 , 1 , 1 , 3 ]x14
      +           +       +           +   => 10
    
    Eg. Closest, Furthest, Closest, Furthest
    []x14
    
    
    x5
    Eg. Furthest, Closest, Furthest, Closest, Closest
    []x17


    Eg. Furthest, Closest, Furthest, Closest, Furthest
    []x17


    Eg. Furthest, Closest, Furthest, Furthest, Closest
    []x17
    
    
    Eg. Furthest, Closest, Furthest, Furthest, Furthest
    []x17
    
    
    Eg. Closest, Furthest, Closest, Closest, Closest
    []x17
    
    
    Eg. Closest, Furthest, Closest, Closest, Furthest
    []x17
    
    
    Eg. Closest, Furthest, Closest, Furthest, Closest
    []x17
    
    
    Eg. Closest, Furthest, Closest, Furthest, Furthest
    []x17
    
    
      
VARIABLES
curr_max = ()
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        return
        #highest_val = 0
        
        #for i in range(len(nums)):
            
        

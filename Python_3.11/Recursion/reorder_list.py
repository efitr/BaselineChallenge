""" Problem "Reorder List"

This problem was taken from leetcode, great webpage to do coding challenges from.
This is the link for this exact problem, https://leetcode.com/problems/reorder-list/.
"""

"""Problem Itself,
TODO: Copy the actual problem in your own words.

"""

"""Insights,
        - compare when recursion goes through the first elements in order, how it moves
        - first data point, recursion, depending on where you place the print can either read forward or backwards
        - I must understand how many must rotate, whatever is half - 1
            => when it was 4, I rotated 4/2 - 1 = 1
            => when it was 8, I rotated 8/2 - 1 = 3
            => when it was 5, I rotated 5/2 lower decimal = 2
            => when it was 9, I rotated 9/2 lower decimal = 4
        
Diagramming + Logic, 

Input: head = [  (1)=> (2)=> (3)=> (4)=> None ]
#iterate through it all, element by element and diagram how that works


def helper(node,counter):
    if node is None: return 
    print("this is the node.val = ",node.val)
    print("this is the counter = ",counter)
    helper(node.next,counter+1)
    
VARIABLES
    counter = 0 => 1 => 2 => 3

  (1)=>    (2)=>    (3)=>    (4)=>   None
1.print  2.print  3.print  4.print



def helper(node,counter):
    if node is None: return 
    helper(node.next,counter+1)
    print("this is the node.val = ",node.val)
    print("this is the counter = ",counter)
            
VARIABLES
    counter = 0 <= 1 <= 2 <= 3

  (1)=>    (2)=>    (3)=>    (4)=>   None
4.print  3.print  2.print  1.print


Output: [1,4,2,3]


Understanding case scenarios, when its 8 nodes

    (1)=>    (2)=>    (3)=>    (4)=>    (5)=>    (6)=>    (7)=>    (8)=>   None
           ^=                                                      <=

    (1)=>    (8)=>    (2)=>    (3)=>    (4)=>    (5)=>    (6)=>    (7)=>   None
                             ^=                                    <=
    
    (1)=>    (8)=>    (2)=>    (7)=>    (3)=>    (4)=>    (5)=>    (6)=>   None
                                               ^=                  <=

    (1)=>    (8)=>    (2)=>    (7)=>    (3)=>    (6)=>    (4)=>    (5)=>   None


Understanding case scenarios, when its 5 nodes

    (1)=>    (2)=>    (3)=>    (4)=>    (5)=>   None
           ^=                           <=

    (1)=>    (5)=>    (2)=>    (3)=>    (4)=>   None
                             ^=         <=
    
    (1)=>    (5)=>    (2)=>    (4)=>    (3)=>   None
                                               

Understanding case scenarios, when its 9 nodes

    (1)=>    (2)=>    (3)=>    (4)=>    (5)=>    (6)=>    (7)=>    (8)=>   (9)=>   None
           ^=                                                              <=

    (1)=>    (9)=>    (2)=>    (3)=>    (4)=>    (5)=>    (6)=>    (7)=>   (8)=>   None
                             ^=                                            <=
    
    (1)=>    (9)=>    (2)=>    (8)=>    (3)=>    (4)=>    (5)=>    (6)=>   (7)=>   None
                                               ^=                          <=

    (1)=>    (2)=>    (3)=>    (4)=>    (5)=>    (6)=>    (7)=>    (8)=>   (9)=>   None
                                                                 ^=        <=

"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def num_shifts(self, head):
        num = 0
        
        while head.next != None:
            head = head.next
            num += 1
        
        if num % 2 == 0:
            print("first if")
            return (num//2)
        else:
            print("else")
            return (num//2)-1
        
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        print(self.num_shifts(head))
        return 
        
        """
        def helper(node,counter):
            if node is None: return 

            
            helper(node.next,counter+1)
            print("this is the node.val = ",node.val)
            print("this is the counter = ",counter)
        
        helper(head,0)
        return 
        """
        

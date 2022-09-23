'''Insights,
        - compare when recursion goes through the first elements in order, how it moves
        - first data point, recursion, depending on where you place the print can either read forward or backwards
        - to know the size of the linkedlist I can use recursion forward, then once everything is on the call stack, I can get the amount of nodes that will change into something else, after that has happened, I can following a pattern add then to the linkedlist using another stack, this other stack goes last one in first, then whatever amount the pattern commands, then based on the pattern that varies whether it is even or un even,
        - I must understand how many must rotate, whatever is half - 1
            => when it was 4, I rotated 4/2 - 1 = 1
            => when it was 8, I rotated 8/2 - 1 = 3
            => when it was 5, I rotated 5/2 lower decimal = 2
            => when it was 9, I rotated 9/2 lower decimal = 4
                => the amount of nodes that will change place is
                =>even number 
                =>
        
        - When you use recursion, every node goes into the call stack, then it is about using that structure ...
            => 
        
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

Understanding case scenarios, when its 4 nodes

counter      1.       2.       3.       4 
            (1)=>    (2)=>    (3)=>    (4)=>    None
                   ^=                  <=

            (1)=>    (4)=>    (2)=>    (3)=>    None DONE

counter = 1 => 2 => 3 => 4
lenght = 4//2-1 => 1
Call stack, once it hits none, start going back to the beggining 
 None ]
 (4)=> X
 (3)=> X
 (2)=> X prev_node.next (4)=>.next= node.next
[(1)=> 

Stack,
(4)=>

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

    (1)=>    (9)=>    (2)=>    (8)=>    (3)=>    (7)=>    (4)=>    (5)=>   (6)=>   None
                                                                 ^=        <=
                                                                 
    (1)=>    (9)=>    (2)=>    (8)=>    (3)=>    (7)=>    (4)=>    (6)=>   (5)=>   None
    
Solution 1 "Using the call stack from the recursive call and another stack"
**Making the pattern for even and un-even

9 nodes example, this is what must happen

    (1)=>    (2)=>    (3)=>    (4)=>    (5)=>    (6)=>    (7)=>    (8)=>   (9)=>   None
           ^=                                                              <=

    (1)=>    (9)=>    (2)=>    (3)=>    (4)=>    (5)=>    (6)=>    (7)=>   (8)=>   None
                             ^=                                            <=
    
    (1)=>    (9)=>    (2)=>    (8)=>    (3)=>    (4)=>    (5)=>    (6)=>   (7)=>   None
                                               ^=                          <=

    (1)=>    (9)=>    (2)=>    (8)=>    (3)=>    (7)=>    (4)=>    (5)=>   (6)=>   None
                                                                 ^=        <=
                                                                 
    (1)=>    (9)=>    (2)=>    (8)=>    (3)=>    (7)=>    (4)=>    (6)=>   (5)=>   None
    
VARIABLES
    stack = []
    counter = 0    
    

    (1)=>    (2)=>    (3)=>    (4)=>    (5)=>    (6)=>    (7)=>    (8)=>   (9)=>   None
    
    
*call_stack = []



8 nodes example

    (1)=>    (2)=>    (3)=>    (4)=>    (5)=>    (6)=>    (7)=>    (8)=>   None
           ^=                                                      <=

    (1)=>    (8)=>    (2)=>    (3)=>    (4)=>    (5)=>    (6)=>    (7)=>   None
                             ^=                                    <=
    
    (1)=>    (8)=>    (2)=>    (7)=>    (3)=>    (4)=>    (5)=>    (6)=>   None
                                               ^=                  <=

    (1)=>    (8)=>    (2)=>    (7)=>    (3)=>    (6)=>    (4)=>    (5)=>   None
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        self.stack = []
        self.stack_count = 0
        # Now I must create another stack to store # num of stack based on the lenght of lenght
        
        num = 9
        num1 = 10
        '''
        if num % 2 == 0:
            print("9 is even")
        if num1 % 2 == 0:
            print("10 is even") => this one prints
        '''
        def helper(node, counter):
            if node is None: 
                return 
            
            if node.next is None:  
                print("\n")
                if counter % 2 == 0:
                    self.stack_count = counter // 2 - 1
                    print("self.stack_count = ",self.stack_count)
                    print("\n")
                else:
                    self.stack_count = counter // 2
                    print("self.stack_count = ",self.stack_count)
                    print("\n")
            print("pre recursive call")
            print("this is the counter == ", counter)
            helper(node.next, counter+1)
            print("\n")
            print("post recursive call")
            print("this is the counter == ", counter)
            
            # I must get the stack to have the last 1 value
            if self.stack_count > 0:
                #if counter 
                print("This is top value before decreasing should be 1 == ",self.stack_count)
                self.stack_count -= 1
                print("This is top value after decreasing should be 0 == ",self.stack_count)
            
        
        helper(head, 1)

        return 

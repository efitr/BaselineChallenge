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
            
        - I must figure out when I must start switching value and under what rule,
        
        
        - I must start appending to the other stack once I have the stack size until it reaches after which I start appending the nodes in the other stack into the linkedlist 
        
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
#pre recursive call
counter  1        2        3        4        5        6        7        8        
        (1)=>    (2)=>    (3)=>    (4)=>    (5)=>    (6)=>    (7)=>    (8)=>   None
                                      
self.stack_count =  8//2-1 => 3 **I append the last 3 elements using this count into the stack



#post recursive call, after having taken elements out into the stack and stack count being 0

      (1)=>      (2)=>      (3)=>      (4)=>      (5)=> 
         (8)=>None  (7)=>None  (6)=>None
#now I append 


                        ]
               (6)=>None     
               (7)=>None 
self.stack = [ (8)=>None

expected = [1,8,2,7,3,6,4,5]


Understanding case scenarios, when its 5 nodes

    (1)=>    (2)=>    (3)=>    (4)=>    (5)=>   None
           ^=                           <=

    (1)=>    (5)=>    (2)=>    (3)=>    (4)=>   None
                             ^=         <=
    
    (1)=>    (5)=>    (2)=>    (4)=>    (3)=>   None
                                               

Understanding case scenarios, when its 9 nodes
#pre recursive call
counter  1        2        3        4        5        6        7        8       9 
        (1)=>    (2)=>    (3)=>    (4)=>    (5)=>    (6)=>    (7)=>    (8)=>   (9)=>   None
                                      ^=         <=
self.stack_count =  4 **I append the last 4 elements using this count into the stack

#post recursive call, after having taken elements out into the stack and stack count being 0

      (1)=>      (2)=>      (3)=>      (4)=>      (5)=> 
         (9)=>None  (8)=>None  (7)=>None  (6)=>None
#now I append 


                    ]
               (6)=>None     
               (7)=>None     
               (8)=>None 
self.stack = [ (9)=>None
        
expected =  [1,9,2,8,3,7,4,6,5]   
    
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
        def helper(node, prev_node, counter):
            if node is None: 
                return 

            print("pre recursive call")
            print("this is the counter == ", counter)
            
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

            helper(node.next, prev_node.next, counter+1)
            print("\n")
            print("post recursive call")
            print("this is the counter == ", counter)
            
            # This 
            if self.stack_count >= 0:
                #if counter 
                if self.stack_count == 0:
                    node.next = None
                    self.stack_count -= 1
                else:
                    print("This is top value before decreasing == ",self.stack_count)
                    node.next = None
                    self.stack.append(node)
                    print(self.stack)
                    self.stack_count -= 1
                    print("This is top value after decreasing == ",self.stack_count)
    
            #When it is an even array expected = [1,8,2,7,3,6,4,5] this is the result, with 8 nodes
            ##When it is an uneven array expected =  [1,9,2,8,3,7,4,6,5] this is the result, with 9 nodes
            else:
                print("This is the current node ", node.val, "this is the previous node ", prev_node.val, "this is the node.next ",node.next)

                stack_node = self.stack.pop()
                print("this is stack_node ",stack_node)
                
                '''this looks out for even or uneven for when to add, otherwise
                
                stack_node.next = node
                prev_node.next = stack_node
                
                '''
                
        helper(head.next, head, 2)

        return 
        

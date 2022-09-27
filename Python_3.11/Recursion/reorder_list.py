'''Insights,
        - Recursion works by creating a call stack, where it moves deeper within the LL structure, creating layers, there depending on where you position your code you can do thing while the call stack is being build or while it is been unbuild
        - to know the size of the linkedlist I can use recursion forward, then once everything is on the call stack, I can get the amount of nodes that I need to change positions of, after that has happened, I can add then to the linkedlist using another stack, this other stack goes last one in first, then whatever amount the pattern commands, then based on the pattern that varies whether it is even or un even,
        - I must understand how many must rotate, whatever is half - 1
            => when it was 4, I rotated 4/2 - 1 = 1
            => when it was 8, I rotated 8/2 - 1 = 3
            => when it was 5, I rotated 5/2 lower decimal = 2
            => when it was 9, I rotated 9/2 lower decimal = 4
                => the amount of nodes that will change place is
                =>even number 
        
        - When you use recursion, every node goes into the call stack, then it is about using that structure ...
            
        - I must figure out when I must start switching value and under what rule,
        
        - I must start appending to the other stack once I have the stack size until it reaches after which I start appending the nodes in the other stack into the linkedlist 
        
        - This is working with 8 but not with 9 at the moment 
        
        
Diagramming + Logic, 

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


Understanding case scenarios, when its 9 nodes
#pre recursive call
counter  1        2        3        4        5        6        7        8       9 
        (1)=>    (2)=>    (3)=>    (4)=>    (5)=>    (6)=>    (7)=>    (8)=>   (9)=>   None
                                      
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

current_result =  [1,8,2,7,3,6,4,5]
expected       =  [1,9,2,8,3,7,4,6,5]   

Visualizing the code: 

counter           2        3        4        5        6        7        8       9
        (1)=>    (2)=>    (3)=>    (4)=>    (5)=>    (6)=>    (7)=>    (8)=>   (9)=>   None
                                                                             node
                                                                 prev_node       

VARIABLES
    self.stack = []
    self.stack_count = 0

Blueprint:
        self.stack = []
        self.stack_count = 0

        def helper(node, prev_node, counter):
            if node is None: 
                return 

            if node.next is None:  
                if counter % 2 == 0:
                    self.stack_count = counter // 2 - 1
                else:
                    self.stack_count = counter // 2

            helper(node.next, prev_node.next, counter+1)

            if self.stack_count >= 0:
                if self.stack_count == 0:
                    node.next = None
                    self.stack_count -= 1
                else:
                    node.next = None
                    self.stack.append(node)
                    self.stack_count -= 1

            else:
                #if counter == len(self.stack)-1:
                stack_node = self.stack.pop()
                stack_node.next = node
                prev_node.next = stack_node
                print(self.stack)

                
        helper(head.next, head, 2)

        return 
        
# Must figure out for [1,2] and [1,2,3], either returns an error
# For some reason 26,27 doesnt work

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

        def helper(node, prev_node, counter):
            if node is None: 
                return 

            #there is a chance that all node.val are actually the number in order, therefore I could use that instead of the counter
            if node.next is None:  
                if counter % 2 == 0:
                    self.stack_count = counter // 2 - 1
                else:
                    self.stack_count = counter // 2

            helper(node.next, prev_node.next, counter+1)

            if self.stack_count >= 0:
                if self.stack_count == 0:
                    node.next = None
                    self.stack_count -= 1
                    if len(self.stack) % 2 == 0:
                        stack_node = self.stack.pop()
                        stack_node.next = node
                        prev_node.next = stack_node
                else:
                    node.next = None
                    self.stack.append(node)
                    self.stack_count -= 1
                    

            else:
                stack_node = self.stack.pop()
                stack_node.next = node
                prev_node.next = stack_node


                
        helper(head.next, head, 2)

        return 
        

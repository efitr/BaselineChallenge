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
        # first lets do the counting on the forward path
        self.counter = 0
        self.lenght = 0
        # Now I must create another stack to store # num of stack based on the lenght of lenght
        
        def helper(node):
            if node is None: 
                if self.lenght == 0:
                    self.lenght = self.counter
                    # I must using the rule know how many nodes I must put in the stack to re organize them into the linkedlist
                return 
            
            #pre call stack
            self.counter +=1
            print("counter", self.counter)
            
            helper(node.next)
            
            #post call stack
            #self.lenght = self.counter
            #print("lenght", self.lenght)
            
        
        helper(head)
        print("Counter",self.counter)
        print("Lenght",self.lenght)
        return 
    
                

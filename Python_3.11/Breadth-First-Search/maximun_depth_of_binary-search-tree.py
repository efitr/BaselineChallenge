'''Insights,
        - You need a queue to perform Breadth First Search

Diagramming + Logic,
Input: root = 
               [3,
        9,            20,
  null,   null,   15,     7]

queue = [(                                                                                                                                                      )]

        root =                                                      TreeNode{val: 3, 
                                    left:                                                                       right:
                               TreeNode{val: 9,                                                            TreeNode{val: 20, 
                left: ,                            right: }                                 left:                                     right:                , 1
                None                               None                             TreeNode{val: 15,                            TreeNode{val: 7, 
                                                                           left:                     right:             left:                     right:
                                                                           None                      None               None                      None }}}
Xif not root: return 0

queue = [([3,9,20,null,null,15,7],1)]
self.res = 0 => 2

while queue not empty:
    root, nums = queue.pop(0)
    root => [3,9,20,15,7]
    nums => 1
    queue = []

    Xif not root.left and not root.right:
        self.res = max(self.res, nums)

    if root.left: => There is a node, therefore this happens
        queue.append((root.left, nums + 1)) => queue = [  ([9],1+1)  ]        
                                                       TreeNode{val: 9,                          
                                          left:                              right: 
                                          None,                              None  }                       

    if root.right: => There is a node, therefore this happens too! 
        queue.append((root.right, nums + 1)) => queue = [  ([9],1+1)  ,  ([20,15,7],1+1)]        
                                                                         TreeNode{val: 20, 
                                                        left:                                     right:                
                                                TreeNode{val: 15,                            TreeNode{val: 7, 
                                        left:                     right:             left:                      right:
                                        None                      None               None                       None }}}
while queue not empty:
    root, nums = queue.pop(0)
        root, nums = queue.pop(0)
        root => [9]
        nums => 2
        queue = [  ([20,15,7],1+1)  ]

    Xif not root.left and not root.right:
        self.res = max(self.res, nums) => max( 0 , 2 ) => 2

    Xif root.left:
        queue.append((root.left, nums + 1))

    Xif root.right:
        queue.append((root.right, nums + 1))

while queue:
    root, nums = queue.pop(0)
        root => [20,15,7]
        nums => 2
        queue = []

    Xif not root.left and not root.right:
        self.res = max(self.res, nums)

    if root.left:
        queue.append((root.left, nums + 1)) => queue = [  ([15],1+1+1)  ]                  
                                                    TreeNode{val: 15, 
                                            left:                     right: 
                                            None                      None   

    if root.right:
        queue.append((root.right, nums + 1)) => queue = [  ([15],1+1+1) , ([7],1+1+1)  ]                  
                                                                    TreeNode{val: 7, 
                                                           left:                      right:
                                                           None                       None }}} 

while queue:
    root, nums = queue.pop(0)
        root => [15]
        nums => 2
        queue = [7]

    if not root.left and not root.right:
        self.res = max(self.res, nums)

    if root.left:
        queue.append((root.left, nums + 1))

    if root.right:
        queue.append((root.right, nums + 1))
        
            
Blueprint

def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root: return 0

    queue = [(root, 1)]
    self.res = 0

    while queue:
        root, nums = queue.pop(0)

        if not root.left and not root.right:
            self.res = max(self.res, nums)

        if root.left:
            queue.append((root.left, nums + 1))

        if root.right:
            queue.append((root.right, nums + 1))

    return self.res

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #breadth first search solution, found it on leetcode, I didnt came up with it
        if not root: return 0
        print(root)
        queue = [(root, 1)]
        self.res = 0

        while queue:
            root, nums = queue.pop(0)

            if not root.left and not root.right:
                self.res = max(self.res, nums)

            if root.left:
                queue.append((root.left, nums + 1))

            if root.right:
                queue.append((root.right, nums + 1))

        return self.res

        '''
        #depth first search solution 
        max_depth = 0
        def helper(node,depth):
            
            if node == None:
                return
            
            nonlocal max_depth
            
            if depth > max_depth:
                max_depth = depth
            
            helper(node.left, depth+1)
            helper(node.right, depth+1)
            
        helper(root,1)
        
        return max_depth
        '''

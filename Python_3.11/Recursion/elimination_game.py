'''Insights, 
        - the data is sorted in ascending order and all values available are there
        - delete every other number, means not very next one the one after that
        
Diagramming + Logic,

n = 12

    [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 ]
    
          ( n, isLeft): 
    helper(12,    1  ) => 6
    => 
    if(n==1): 
        return 1
    # 1 is true and 0 is false
    if(isLeft): => if 1, this asks is isLeft equal to 1 or true, go in here
               2*||>3 => 6 
        return 2*helper(n//2, 0)
                 helper(  6 , 0) 
                 => 
                 Xif(n==1): 
                     return 1

                 Xif(isLeft): => if isLeft equal to 1, since 1 means true, I go in here, 0 is False
                     return 2*helper(n//2, 0)

                 Xelif(n%2==1):
                     return 2*helper(n//2, 1)

                 else:       2*||>2 =>4 - 1 => 3
                     return (2*helper(n//2   , 1)) - 1
                               helper(6//2=>3, 1)     
                                   Xif(n==1): 
                                       return 1

                                   if(isLeft):  ||>1 => 2
                                       return 2*helper(n//2, 0)
                                                helper(3//2=>1, 0)
                                                    if(n==1): 
                                                        return 1

                                                    Xif(isLeft):
                                                        return 2*helper(n//2, 0)

                                                    Xelif(n%2==1):
                                                        return 2*helper(n//2, 1)

                                                    Xelse:
                                                        return (2*helper(n//2, 1)) - 1

                                   elif(n%2==1):
                                       return 2*helper(n//2, 1)


                                   else:
                                       return (2*helper(n//2, 1)) - 1


    elif(n%2==1):
        return 2*helper(n//2, 1)

    else:
        return 2*helper(n//2, 1) - 1

Blueprint 

        def helper(n, isLeft): 
            if(n==1): 
                return 1
            
            if(isLeft):
                return 2*helper(n//2, 0)
                
            elif(n%2==1):
                return 2*helper(n//2, 1)
                
            else:
                return (2*helper(n//2, 1)) - 1
            
        return helper(n, 1)

'''

class Solution:
    def lastRemaining(self, n: int) -> int:

        def helper(n, isLeft):

            if(n==1): return 1

            if(isLeft):
                print("this is the isLeft == ",isLeft, "this is current n == ",n)
                return 2*helper(n//2, 0)

            elif(n%2==1):
                print("Does this happens? elif(n%2==1)")
                return 2*helper(n//2, 1)
                print("do I ever get here")

            else:
                print("Does this happens? else")
                return (2*helper(n//2, 1)) - 1


        return helper(n, 1)
        
        '''
        def helper(n, isLeft):
            
            if(n==1): return 1
            
            #print(isLeft)
            if(isLeft):
                print("hey")
                return 2*helper(n//2, 0)
    # if started from left side the odd elements will be removed, the only remaining ones will the the even i.e.
    #       [1 2 3 4 5 6 7 8 9]==   [2 4 6 8]==     2*[1 2 3 4]
            elif(n%2==1):
                return 2*helper(n//2, 1)
    # same as left side the odd elements will be removed
            else:
                return 2*helper(n//2, 1) - 1
    # even elements will be removed and the only left ones will be [1 2 3 4 5 6 ]== [1 3 5]== 2*[1 2 3] - 1
            
        return helper(n, 1)
        '''
        '''
        arr = []
        
        for n in range(1,n+1):
            arr.append(n)
        
        if len(arr) <= 3:
            if len(arr) == 1 :
                return arr[0]
            #elif len(arr) == 2 or len(arr) == 3
            else:
                return arr[1]
        
        else:
            while len(arr) > 1:
            
            
            
        return 
        '''

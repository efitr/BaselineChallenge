'''Insights, 
        - the data is sorted in ascending order and all values available are there
        - delete every other number, means not very next one the one after that
        
Diagramming + Logic,

n = 12

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


n = 22

return helper(22, 1)
             (22,1)
        Xif(22==1): 
            return 1

        if(1): => 1 in python is true, 0 is false
            return 2*helper(22//2, 0) =>2*4 => 8
                           ( 11 ,  0)
                    Xif(n==1): 
                        return 1

                    Xif(isLeft):=> 0 is false, therefore this doesnt work
                        return 2*helper(n//2, 0)

                    elif(n%2==1): => 11 divided by 2 would have a remainder of 1
                        return 2*helper(n//2, 1) => 2*2 => 4
                                       (  5 , 1)
                                        Xif(5==1): 
                                            return 1

                                        if(isLeft=>1): #since isLeft is 1 this means true for python
                                            return 2*helper(n//2, 0) => 2*1 => 2
                                                           (  2 , 0) 
                                                            Xif(n==1): 
                                                                return 1

                                                            Xif(isLeft):
                                                                return 2*helper(n//2, 0)

                                                            Xelif(n%2==1):
                                                                return 2*helper(n//2, 1)

                                                            else:
                                                                return (2*helper(n//2, 1)) - 1 => 2*1-1 => 1
                                                                                (  1 , 1)
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

                    else:
                        return (2*helper(n//2, 1)) - 1

        elif(n%2==1):
            return 2*helper(n//2, 1)

        else:
            return (2*helper(n//2, 1)) - 1

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
        
Solution 1: #This solution does not belong to me, I learned it from Leetcode discussion
The pattern this problem utilizes to reach to solution is it breaks down the problem into two types of steps,
    - Since the isLeft is bound to happen every other time, with a isLeft of meaning it is at the start of the number
    - Then the other option is the elif and else, since they must happen depending on whether the value is odd or not, in which case isLeft becomes 1 again implying you are at the start of the recently cut in half array
    
Hindsight:
    - This examples utilizes a very good appraoch towards recursion, since it makes full use of its potential to go into the stack call and brings back the solution while it comes back from the recursive stack


'''

class Solution:
    def lastRemaining(self, n: int) -> int:

        def helper(n, isLeft):

            if(n==1): return 1

            if(isLeft==1):
                print("if(isLeft): for n == ", n)
                print("this is the isLeft == ",isLeft, "this is current n == ",n)
                print("\n")
                return 2*helper(n//2, 0)

            elif(n%2==1):
                print("elif(n%2==1):")
                print("Does this happens? elif(n%2==1) under which n ", n)
                print("\n")
                return 2*helper(n//2, 1)
                print("do I ever get here")

            else:
                print("else: for n == ", n)
                print("\n")
                return (2*helper(n//2, 1)) - 1


        return helper(n, 1)
        
        

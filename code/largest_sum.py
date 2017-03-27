# function , give an integer, return largest sum of squares that equals that integer, F
# input = positive N , greater than 1
# output = array where 2 integers
# Example 2 is 1 and 1
# Example 5 is 1 and 2 = 1 + 4 = 5
# if there is no pair return F
# Example 8 2 and 2 = 4 + 4 = 8

def largest_sum(N):
    i = 0 # initial start
    j = int(sqrt(N)) # integer will not be greater than the square root of N
    while j >= i:  
        total = pow(i,2) + pow(j,2) # sum of squares
        if total == N: return i,j # if answer matches N return pair 
        elif total > N: j -= 1 # lower the value j
        else: i += 1 # increase the value of i 
    return False

largest_sum(1000000)
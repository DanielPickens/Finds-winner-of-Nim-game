def findWinner(A, n): 
  
    res = 0
    for i in range(n): 
        res ^= A[i] 
  
    # case when A is winner 
    if (res == 0 or n % 2 == 0): 
        return "A"
  
    # when B is winner 
    else: 
        return "B"
  
# Next 
A = [ 4, 12] 
n = len(A) 
print("Winner = ", findWinner(A, n))

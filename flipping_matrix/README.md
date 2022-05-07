# Flipping the Matrix challenge
Sean invented a game involving a 2n x 2n matrix where
 each cell of the matrix contains an integer. He can reverse 
 any of its rows or columns any number of times. The goal of the 
 game is to maximise the sum of the elements in the n x n submatrix 
 located in the upper-left quadrant of the matrix.
 
 Given the initial configurations for q matrices help Sean reverse the 
 rows and columns of each matrix in the best possible way so that 
 the sum of the elements in the matrix's upper-left quadrant is 
 maximal.
 
 ## Constraints
 
 * 1 <= q <= 16
 * 1 <= n <= 128
 * 0<= matrix[i][j] <= 4096, where 0 <= i,j <= 2n
 
 
 Example:
 
   112     42      83      119
   
   56      125     56      49
   
   15      78      101     43
   
   62      98      114     108
   
   Should give 414 as output
   
## Thinking process
Each element can only occupy a set position after any given reversion, 
i.e. the element in the top left corner (112) can only ever be placed 
in any other corner after reversion - top right, bottom right or 
bottom left. 

The same is true for every other single element in the square matrix.

Hence, the solution is to find the maximum of each set of mirror buddies 
for each element in the top left quadrant and return the sum.
   
Example: 

* Reversion buddies for the top left corner:
 
   **112**     42      83      **119**
   
   56      125     56      49
   
   15      78      101     43
   
   **62**      98      114     **108**
 
* Reversion buddies for the top right corner within the top left 
quadrant:
 
   112     **42**      **83**      119
   
   56      125     56      49
   
   15      **78**      **101**     43
   
   62      98      114     108

* Reversion buddies for the bottom right corner of the top left 
quadrant:
 
   112     42      83      119
   
   56      **125**     **56**      49
   
   15      **78**      **101**     43
   
   62      98      114     108

* Reversion buddies for the bottom left corner of the top left 
quadrant:
 
   112     42      83      119
   
   **56**      125     56      **49**
   
   **15**      78      101     **43**
   
   62      98      114     108
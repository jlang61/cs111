# Import Statements go here
import numpy as np
import numpy.linalg as npla
from scipy import sparse
def pagerank2(E, return_vector = False, max_iters = 1000, tolerance = 1e-6, m = 0.15):
    """compute page rank from dense adjacency matrix
    Inputs:
      E: adjacency matrix with links going from cols to rows.
         E is a matrix of 0s and 1s, where E[i,j] = 1 means 
         that web page (vertex) j has a link to web page i.
      return_vector = False: If True, return the eigenvector as well as the ranking.
      max_iters = 1000: Maximum number of power iterations to do.
      tolerance = 1e-6: Stop when the eigenvector norm changes by less than this.
      m = 0.15: default
      
    Outputs:
      ranking: Permutation giving the ranking, most important first
      vector (only if return_vector is True): Dominant eigenvector of PageRank matrix
    This computes page rank by the following steps:
    1. Add links from any dangling vertices to all vertices.
    2. Scale the columns to sum to 1.
    3. Add a constant matrix to represent jumping at random 15% of the time.
    4. Find the dominant eigenvector with the power method.
    5. Sort the eigenvector to get the rankings.
    
    The function takes input E as a scipy csr_sparse matrix, and then never creates 
    a full matrix or any large matrix other than E.
    """

# HERE ARE ALL THE TASKS YOU NEED TO FIGURE OUT!
#################################################

# 1. Check if E is a square matrix and that its entries are ONLY 1s and 0s, otherwise end this
    assert E.shape[0] == E.shape[1], "Not a square matrix"
    nnz = np.count_nonzero(E)
    assert np.max(E) == 1 and np.sum(E) == nnz, "Entries not only 1s and 0s"
    
# 2. Check if E is a sparse matrix. If NOT, then convert it into one.
    #sparse if number non zero is less than 1/3 of the total entries  
    if (type(E) != sparse._csr.csr_matrix):
      E = sparse.csr_matrix(E)
      
# 3. Calculate the outdegree 
    #calculate by summing up per row
    outdegree = np.sum(E,0)
# 4. Get set up for the power iteration:
#       create an initial vector (all 1s)
#       make sure you know where outdegree is 0
    v = np.ones(E.shape[0])
    n = E.shape([0])
    for iteration in range(max_iters):
        oldv = v

      #Remember: The equation we are trying to solve is: MV = (1−m)(EV+FV) + m*SV,
      #     where:  SV is the average of vector v
      #             EV is matrix E multiplied by the normalized version of vector v
      #             FV is a matrix that accounts for dangling vertices (i.e. where outdegree is 0 in E). 
      #                 Note that if there are no dangling nodes in E, F will always be 0 (easy case).
      
      
      #Part 1: SV -- This last (and easiest) part of the equation essentially is just an 
      # "average" operator on the matrix v. By this I mean that every item in the vector is just 
      # The sum of the vector components divided by the number of nodes, which is an average.
      # You can find SV with a simple and efficient alternative to actually making the dense S matrix and  
      # multiplying it by v to get the same result.
        SV = S @ v

      #Part 2: EV  -- Multiply E by normalized v vector
        EV = E @ v /outdegree
      
      #Part 3: FV -- In order to avoid having to actually construct the (likely sparse) F matrix,
      # We will take advantage of the unique properties. Essentially we know that for a dangling node,
      # the probability of landing on any other node is evenly split.  This translates to the values
      # at the index of the dangling nodes in FV being one normalized unit of v less than all the other
      # values at non-dangling indicies. You can do this in as little as 3 lines of code and thus 
      # calculate the FV vector without any matrix multiplication. 
        FV = np.ones(n)*np.sum(v[there])
        #now remove number v[there] from all positions in FV listed in there
        
        #divide FV by (n-1)
        FV = FV /(n-1)
        
        
      #Part 4: Calculate MV per the formula
        MV = (1-m)(EV + FV) + m * SV
    
    #5. And now you should be back to exactly where we were with pagerank1(), 
    #   so finish this up based on what we did in that function.
    
        v = MV
        eigval = npla.norm(v)
        print("eig_val: \n", eigval)
        print("v: \n", v)
        v = v / eigval
        if (npla.norm(v - oldv) < tolerance):
              print('Dominant eigenvalue is %f after %d iterations.\n' % (eigval, iteration+1))
              break
      
    # finish it up here, just like in pagerank1()
    assert np.all(v > 0) or np.all(v < 0), 'Error: eigenvector is not all > 0 or < 0'
    vector = np.abs(v)
    
    ranking = np.argsort(vector)[::-1]
    if return_vector: 
      return ranking, vector  
    else:
      return ranking
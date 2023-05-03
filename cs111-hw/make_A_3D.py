import numpy as np 
import numpy.linalg as npla
import scipy 
from scipy import sparse
def make_A_3D(k):
    #Revised make_A for a k by k by k grid 
    triples = [] 
    #idea of triples stays the same 
    for a in range(k):
        for b in range(k):
            for c in range(k):
                #row of matrix is the grid point 
                row = c + b * k + a * (k ** 2)
                triples.append((row,row, 6.0))
                #connect to the left grid neighbor
                if c > 0:
                    triples.append((row,row - 1, -1.0))
                #right neighbor
                if c < k - 1:
                    triples.append((row,row + 1, -1.0))
                #neighbor above
                if b > 0:
                    triples.append((row,row - k, -1.0))
                #neighbor below
                if b < k -1:
                    triples.append((row,row + k, -1.0))
                #neighbor up
                if a > 0:
                    triples.append((row,row - (k ** 2), -1.0))
                #neighbor down 
                if a < k -1:
                    triples.append((row,row + (k **2), -1.0))
    ndim = k * k * k
    rownum = [t[0] for t in triples]
    colnum = [t[1] for t in triples]
    values = [t[2] for t in triples]
    A = sparse.csr_matrix((values, (rownum, colnum)), shape = (ndim, ndim))            
    return A            
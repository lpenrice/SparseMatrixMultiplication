# SparseMatrixMultiplication
The driving question for the project was how can we optimize matrix multiplicaiton in the context of the PageRank algorithm? The matrices involved in PageRank are very sparse, causing inefficiencies. We wrote our own naive matrix multuiplication and class and sparse matrix multiplication class to analyze against SciPy's built-in matrix multiplication. To test our methods we initialized different sizes of matrices using subsets of a dataset that contains links between WikiPedia pages and calculated the power to which we take that matrix until we hit ‘convergence.’ After taking, the matrix to this power, we tracked runtime for different matrix types. We were able to optimize the naive multiplication method in our sparse method, however, we were unable to come close to the efficiency of SciPy. The analysis notebook displays our findings. 

# Authors
Louisa Penrice
Stefan Feiler
Blanche Stora

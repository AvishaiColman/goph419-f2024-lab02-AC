import numpy as np


def gauss_iter_solve(A, b, x0=None, tol=1e-8, alg='seidel'):
    '''
    Function to solve systems of linear equations (Ax=b) using the Gauss-Seidel approach.

    Inputs
    ------
    A: array_like
        contains the coefficient matrix
    b: array_like
        contains the right hand side vectors
    x0: array_like
        (optional) contains the initial guesses. Default value of None.
    tol: float
        (optional) the stopping criterion. Default value of 1e-8
    alg: str
        (optional) flag for the algorithm to be used. Default value of 'seidel'. Could use either 'seidel' or 'jacobi'.
    
    Returns
    -------
    x : array_like
        is an np.ndarray with the same shape as b
    '''
    A = np.array(A, dtype="float64")
    b = np.array(b, dtype="float64")
    # check for valid input
    A_shape = A.shape
    M = A_shape[0]
    if len(A_shape) != 2:
        raise ValueError(
            f"coefficient matrix has dimension {len(A_shape)}, should be 2."
        )
    if M != A_shape[1]:
        raise ValueError(f"a has shape {A_shape}, should be square.")
    b_shape = b.shape
    if len(b_shape) < 1 or len(b_shape) > 2:
        raise ValueError(f"b has dimension {len(b_shape)}, should be 1 or 2.")
    if M != b_shape[0]:
        raise ValueError(
            f"b has leading dimension {b_shape[0]}, should match leading dimension of a which is {M}"
        )
    #b_one_d = len(b_shape) == 1
    #if b_one_d:
    #    b = np.reshape(b, (M, 1))

    # Error checking for the initial guess vector
    if x0 is None:
        x = np.zeros_like(b)
    else:
        x = np.array(x0, dtype=float)
        x_shape = x.shape
        if x_shape != b_shape:
            raise ValueError(f'x0: {x0} and b: {b} should have the same shape.')
        elif x_shape[0] != M and x_shape[0] != b_shape[0]:
            raise ValueError(f'x0 should be a single column with the same number of rows as A and b.')
    
        
    # Error checking for algorithm type
    alg_strip_low = alg.strip().lower()
    if alg_strip_low not in {'seidel', 'jacobi'}:
        raise ValueError('Choose to use either the "jacobi" or "seidel" algorithm.')
    
    

    # Nomalize the matrices to the main diagonal entries in A
    A_diag_inv = np.diag(1 / np.diag(A))
    A_star = A_diag_inv @ A

    id = np.identity(len(A))
    A_s_star = A_star - id

    b_star = A_diag_inv @ b
    
    # Do the Gauss Seidel and Jacobi algorithms
    # First initialize the counters and set maximum iterations
    n = 0
    n_max = 100
    eps_a = 2 * tol

    # The jacobi algorithm
    if alg_strip_low == 'jacobi':
        while n < n_max and eps_a > tol:
            x_copy = x.copy()       # Create a copy of the initial guess 
            x = b_star - (A_s_star @ x)         # Do the algorithm
            dx = x - x_copy             # Calculate the difference between iterations
            n += 1      
            eps_a = np.linalg.norm(dx) / np.linalg.norm(x)      # Update the approx relative error

    # The Gauss-seidel algorithm
    else:
        x = x0.copy()       # start from the initial guess
        while n < n_max and eps_a > tol:
            x0 = x.copy()   # saves the previous estimate before updating
            for k, _ in enumerate(x):       # loop over each row (each x value)
                x[k, :] = (b_star[k, :] - np.dot(A_star[k, :k], x[:k, :]) -np.dot(A_star[k, k+1:], x[k+1, :])) / A_star[k, k]
            dx = x - x0
            eps_a = np.linalg.norm(dx) / np.linalg.norm(x)
            n += 1
    
    if n >= n_max:
        raise RuntimeWarning(f'This system has not converged after {n_max} iterations. Returning the most updated iteration.')
    
    

    return x

    

# Some tests to make sure the stuff works...
a1 = np.array([[3, 2], [4, 6]])
b1 = np.array([5, 1])
initial = np.array([1, 1])

try1 = gauss_iter_solve(a1, b1, initial, alg='jacobi')
print(try1)











def spline_function(xd, yd, order = 3):
    '''
    Function that generates a spline function given two vectors x and y of data.

    Inputs
    ------
    xd : array_like
        array_like of float data increasing in value

    yd : array_like
        array_like of float data with the same shape as xd

    order : int
        (optional) int with possible values 1, 2, 3

    Returns
    -------
    function
        function that takes one parameter (a float or array_like of float) and returns the interpolated y values
    '''
    
    if order != 1 or order != 2 or order != 3:
        raise ValueError('The order must be either 1, 2, or 3.')

    xd_flat  = xd.flatten()
    yd_flat = yd.flatten()
    if len(xd_flat) != len(yd_flat):
        raise ValueError('The inputs xd and yd must have the same length.')
    
    repeats = np.unique(xd)
    if len(repeats) != len(xd):
        raise ValueError(
            f'The number of unique independent variable values {len(xd)} != the number of independent variable values {len(repeats)}'
            )
    
    xd_sorted = np.sort(xd)
    if xd_flat != xd_sorted:
        raise ValueError('The independent variable values should be increasing in value.')
    
    # how to get the yd data sorted based on the xd data?------------------------------------------------------


    # Create the first order Newton's divided difference 
    x_diff = np.diff(xd)
    y_diff = np.diff(yd)
    first_diff = y_diff / x_diff        # This is the first order Newtons divided difference

    # Calculate the linear spline

    if order == 1:
        b = first_diff      # This is the RHS vector of the spline
        def lin_spline(x):
            return x



    return function

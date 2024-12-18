import numpy as np


def gauss_iter_solve(A, b, x0 = None, tol = 1e-8, alg = 'seidel'):
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
        (optional) flag for the algorithm to be used. Default value of 'seidel'
    
    Returns
    -------
        : array_like
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
    b_one_d = len(b_shape) == 1
    if b_one_d:
        b = np.reshape(b, (M, 1))

    
    if x0 != None:
        x0_shape = x0.shape
        if x0_shape != b_shape:
            raise ValueError(f'x0: {x0} and b: {b} should have the same shape.')
        elif len(x0_shape[0]) != len(M) and len(x0_shape[0]) != len(b_shape[0]):
            raise ValueError(f'x0 should be a single column with the same number of rows as A and b.')
    else:
        x0 = np.zeros_like(b)


    alg_strip_low = alg.strip().lower()
    if alg_strip_low != 'seidel' or alg_strip_low != 'jacobi':
        raise ValueError('Choose use the "jacobi" or "seidel" algorithm.')
    

    # Nomalize the matrices to the main diagonal entries in A
    A_diag_inv = np.diag(1 / np.diag(A))
    A_star = A_diag_inv @ A

    id = np.identity(len(A_star))
    A_s_star = np.subtract(A_star, id)

    b_star = A_diag_inv @ b
    
    # Do the Gauss Seidel algorithm

    n = 0
    n_max = 100
    stop = tol
    eps_a = 1.0
    x_old = x0

    if alg_strip_low == 'jacobi':
        while n < n_max or eps_a > stop:
            x_new = np.subtract(b_star, A_s_star @ x_old)
            x_old = x_new
            n += 1

    elif alg_strip_low == 'seidel':
        while n < n_max or eps_a > stop:
            




    



    return np.ndarray
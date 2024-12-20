import numpy as np
'''
def stir(alg = 'seidel'):
    alg_strip_low = alg.strip().lower()
    print(alg_strip_low)

stir('       jacObi  ')
'''

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)
'''
A_d_inv = np.diag(1 / np.diag(A))
print(A_d_inv)
A_star = A_d_inv @ A
print(A_star)

id = np.identity(len(A_star))
print(id)
A_s_star = np.subtract(A_star, id)
print(A_s_star)




test = np.unique(A)
print(test)
'''

xd = np.array([2, 3, 1, 4, 6, 7, 9, 21, 32, 67])
xd_flat = xd.flatten()
xd_sort = np.sort(xd)
print(xd)
print(xd_flat)
print(xd_sort)

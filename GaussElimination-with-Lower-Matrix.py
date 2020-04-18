import numpy as np
import copy
import scipy
import scipy.linalg

def gaussElimin(a,b):
    L = [[0 for i in range(len(a))]for j in range(len(a))] #inicializar matriz de ceros para la trinagular inferior
    
    n = len(b)
# Eliminación
    for j in range(0,n-1): # colunmas
        for i in range(j+1,n): # renglones
            if a[i,j] != 0.0:
                lam = a[i,j]/a[j,j]
                L[i][j] = lam
                a[i,j:n] = a[i,j:n] - lam*a[j,j:n]
                b[i] = b[i] - lam*b[j]
    # Sustitución regresiva
    for i in range(n-1,-1,-1):
        b[i] = (b[i] - np.dot(a[i,i+1:n],b[i+1:n]))/a[i,i]
    return b, L, a

def Imprime(M):
    for l in M:
        print(l)
    print("\n")

if __name__ == "__main__":
    
    a = np.array([[4,1,2,-3,5], [-3,3,-1,4,-2], [-1,2,5,1,3], [5,4,3,-1,2],[1,-2,3,-4,5.]])
    a_copy = copy.deepcopy(a)

    b = np.array ([-16, 20, -4, -10, 3.])[np.newaxis]
    b = b.T
    b_copy = copy.deepcopy(b)
    
    L = []

    x, L, a = gaussElimin(a,b)
    # P, L2, U = scipy.linalg.lu(a_copy)
    for i in range (0, len(a)):
        L[i][i] = 1
    print("La matriz de eliminacion es:")
    Imprime(L)
    
    print (f"La matriz A resultante es: \n")
    Imprime(a)


    print ("El vector b original", "\n",b_copy)
    print("\n")
    print("La solucion al sistema: ","\n", x, "\n")
    
    print(f"A = LU {np.dot(L,a)} \n")
    print (f"la comprobacion del sistema es: \n {np.linalg.solve(a_copy,b_copy)}")

#%%

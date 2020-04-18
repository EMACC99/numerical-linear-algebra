import numpy as np
import copy
import scipy
import scipy.linalg

def ResolverCosasProgresivas(a,b):
    a = np.array(a)
    n = len(b)
# Eliminación
    for j in range(0,n-1): # colunmas
        for i in range(j+1,n): # renglones
            if a[i,j] != 0.0:
                lam = a[i,j]/a[j,j]
                L[i][j] = lam
                a[i,j:n] = a[i,j:n] - lam*a[j,j:n]
                b[i] = b[i] - lam*b[j]
    for i in range (0, n-1):
        b[i] = (b[i] - np.dot(a[i,i+1:n], b[i+1:n]))/a[i,i]
    return b



def ResolverCosasRegresivas(a,b):
    a = np.array(a)
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
    return b



def LU(a):
    L = [[0 for i in range(len(a))]for j in range(len(a))] #inicializar matriz de ceros para la trinagular inferior
    for i in range(0,len(L)):
        L[i][i] = 1

    n = len(a)
# Eliminación
    for j in range(0,n-1): # colunmas
        for i in range(j+1,n): # renglones
            if a[i,j] != 0.0:
                lam = a[i,j]/a[j,j]
                L[i][j] = lam
                a[i,j:n] = a[i,j:n] - lam*a[j,j:n]
    return L, a

def Imprime(M):
    for l in M:
        print(l)
    print("\n")

if __name__ == "__main__":
    
    a = np.array([[1,-3,7], [0,3,-2], [-2,6,1.]])
    a_original = copy.deepcopy(a)
    a_inv = []

    I = np.identity(len(a))

    L = []

    L, a = LU(a)
    
    Imprime(L)
    Imprime(a)
    print (f"{np.dot(L,a)}")
    
    for i in range(0,len(a)):
        b = I[i]
        y = ResolverCosasProgresivas(L,b)
        x = ResolverCosasRegresivas(a,y)
        a_inv.append(x.T)

    a_inv = np.array(a_inv).T
    print(f"A inversa es \n")
    Imprime (a_inv)

    print (f"Comprobacion A * A^-1 \n{np.dot(a_original, a_inv)}")



#%%

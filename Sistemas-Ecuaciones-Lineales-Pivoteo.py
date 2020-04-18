import numpy as np
import copy
import scipy
import scipy.linalg
import sys

def CalcularMatrices(n = 4): #intentar con n = 2,3,4,5 y ver que onda
    A = [[(i + j)**2 for i in range (1,n+1)] for j in range (1, n+1)]
    B = [0 for _ in range (n) ]
    bi = 0
    for i in range(0,n):
        for j in range (0,n-1):
            bi += A[i][j]
            print(bi)
        B[i] = bi
        bi = 0
    
    return A, B


def swap(v,i,j):
    if len(v.shape) == 1:
        v[i],v[j] = v[j],v[i]
    else:
        temp = copy.deepcopy(v[i]) 
        v[i] = v[j]
        v[j] = temp
    return v


def gaussPivoteo(a,b, tol = 1.0e-12):
    L = [[0 for i in range(len(a))]for j in range(len(a))] #inicializar matriz de ceros para la trinagular inferior
    
    n = len(b)

    s = np.zeros(n)
    for i in range(n):
        s[i] = max(abs(a[i,:]))

    # permutaciones
    vp = np.array(range(n)) 

    for k in range(0,n-1):
        p = np.argmax(abs(a[k:n , k])/s[k:n]) + k
        if abs(a[p,k]) < tol:
            print(f"La matriz es una matrix singular :c")
            input("Presione una tecla para salir")
            sys.exit()

        if p != k:
            swap(a,k,p)
            swap(b,k,p)
            swap(s,k,p)
            swap(vp,k,p)
            print(f"Intercambie {k} y {p}")

# Eliminación
        for i in range(k+1,n): # renglones
                lam = a[i,k]/a[k,k]
                L[i][k] = lam
                a[i,k:n] = a[i,k:n] - lam*a[k,k:n]
                b[i] = b[i] - lam*b[k]
    
    if abs(a[n-1,n-1]) < tol:
        print(f"Matrix singular :c")
        input("Oprime un tecla para continuar")
        sys.exit()

    # Sustitución regresiva
    for i in range(n-1,-1,-1):
        b[i] = (b[i] - np.dot(a[i,i+1:n],b[i+1:n]))/a[i,i]
    return b, vp

def Imprime(M):
    for l in M:
        print(l)
    print("\n")

if __name__ == "__main__":
    a  = np.array([[3.,-13., 9., 3.],[-6., 4., 1., -18.],[6., -2., 2., 4.],[12., -8., 6, 10.]])
    b  = np.array([-19., -34., 16., 26.])[np.newaxis]
    # a = np.array([[0.143, 0.357, 2.01],[-1.31, 0.911, 1.99],[11.2, -4.30, -0.605]])
    # b = np.array([-5.17, -5.46, 4.42])[np.newaxis]
    # a = np.array([[4,1,2,-3,5], [-3,3,-1,4,-2], [-1,2,5,1,3], [5,4,3,-1,2],[1,-2,3,-4,5.]])
    a_copy = copy.deepcopy(a)

    # b = np.array ([-16, 20, -4, -10, 3.])[np.newaxis]
    b = b.T
    b_copy = copy.deepcopy(b)
    
    L = []

    x, a = gaussPivoteo(a,b)


    print (f"El vertor de permutaciones es: \n")
    Imprime(a)


    print ("El vector b original", "\n",b_copy)
    print(f"\n")
    print("La solucion al sistema: ","\n", x, "\n")
    
    print(f"Ax = b {np.dot(a_copy,x)} \n")
    print (f"la comprobacion del sistema es: \n {np.linalg.solve(a_copy,b_copy)}")
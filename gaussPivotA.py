''' x = gaussPivot(a,b,tol=1.0e-9).
Resuelve [a]{x} = {b} por eliminacion de Gauss 
con pivoteo parcial escalado
'''
# A  = np.array([[3.,-13., 9., 3.],[-6., 4., 1., -18.],[6., -2., 2., 4.],[12., -8., 6, 10.]])
# B  = np.array([-19., -34., 16., 26.])

# AA = np.array([[0.143, 0.357, 2.01],[-1.31, 0.911, 1.99],[11.2, -4.30, -0.605]])
# BB = np.array([-5.17, -5.46, 4.42])
import numpy as np
import sys

def gaussPivot(A,B,tol=1.0e-12):
    n = len(B)
    a = np.copy(A)
    b = np.copy(B)
    
    # Vector de escala
    s = np.zeros(n)
    for i in range(n):
        s[i] = max(abs(a[i,:]))

    # Vector de permutaciones
    vp = np.array(range(n))       
                        
    for k in range(0,n-1): # Ciclo sobre las columnas
        
        # Intercambio de renglones si es necesario
        p = np.argmax(abs(a[k:n,k])/s[k:n]) + k
        if abs(a[p,k]) < tol:
           err('La matriz es singular')
        if p != k:
           swapRensAGP(a,k,p)  #Matriz de coeficientes
           swapRensAGP(b,k,p)  #Vector independiente
           swapRensAGP(s,k,p)  #Vector de escala
           swapRensAGP(vp,k,p) #Vector de permutaciones
           print 'Intercambio:',k,p
        # Eliminacion
        for i in range(k+1,n):
            if a[i,k] != 0.0:
               lam = a[i,k]/a[k,k]
               a[i,k:n] = a [i,k:n] - lam*a[k,k:n]
               b[i] = b[i] - lam*b[k]
                
    if abs(a[n-1,n-1]) < tol:
         err('La matriz es singular')
        
      # Sustitucion regresiva
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b,vp
    
def swapRensAGP(v,i,j):
    if len(v.shape) == 1:
       v[i],v[j] = v[j],v[i]
    else:
      temp = v[i].copy()
      v[i] = v[j]
      v[j] = temp
      
def err(string):
    print string
    raw_input('Oprime return para salir')
    sys.exit()
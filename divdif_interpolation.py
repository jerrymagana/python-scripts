# ==========================================================================================================================
# Title: divdif_interpolation.py
# Author: Jerry Paul Magaña
# Contact: jerrypaulmagana@gmail.com
# Description: A rough code snippet that implements two mathematical algorithms (Newton's Divided Difference & Horner's 
# Nestled Polynomial Expansion) used to produce a polynomial that interpolates a fixed number of (x,y) cartesian points.
# ==========================================================================================================================

import numpy as np
import matplotlib.pyplot as plt

def horners(constants,t,b): # Implements Horner's Method for nestled polynomials
    k = len(constants)
    y = constants[k-1]
    for j in range(1,k):
        y = np.add(
                const[k-(j+1)],
                np.multiply(
                    np.subtract(
                        t,
                        b[k-(j+1)]
                        ),
                    y
                    )
                )
    return y

        
def divDif(xpts,ypts): # Implements Newton's Divided Difference method for determining coefficients of interpolating polynomials
    if len(xpts) != len(ypts):
        print('Error: Mismatched dimensions. Check input and run again.')
        return
    else:
        n = len(xpts)
        s = (n,n)
        triangle = np.zeros(s)
        const = []
        for j in range(0,n):
            triangle[j,0] = ypts[j]
        for i in range(1,n): # Nestled four loop creates lower triangular matrix of divided differences.  
            for j in range(0,n-i):
                triangle[j,i] = np.divide(
                                    np.subtract(
                                        triangle[j+1,i-1],
                                        triangle[j,i-1]),
                                    np.subtract(
                                        xpts[j+i],
                                        xpts[j]))
        for k in range(0,n): # Appends the appropriate divided difference for coefficient to 'const' (pivot point of each column in 'triangle').
            c = triangle[0,k]
            const.append(c)
    return const, triangle

# Everything below this line is a test implementation which utilizes the above functions. If you are incorporating this code
# into your own work, the rest should be changed to fit your needs, or otherwise removed.

t = np.linspace(-3,6,1000)
x = [1,1.01,1.02,1.03]
y = [0,0.01,0.0198,0.0296]
c = divDif(x,y)
const = c[0]
print('Constants:',c[0])
print('Triangle Matrix:\n',c[1])
#k = len(const)
#for i in range(k // 2):
#    const[i],const[k-i-1] = const[k-i-1],const[i] # Reverses list so coefficient of higest degree term comes first
#print(const)
#ft = horners(const,t,x)
r = horners(const,1.025,x)
print(r)
#plt.plot(t,ft)
#plt.plot(x,y)
#plt.plot(x,y,'o',color='black')
#plt.grid()
#plt.show()

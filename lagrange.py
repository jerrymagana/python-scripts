# ==========================================================================================================================
# Title: lagrange.py
# Author: Jerry Paul Magaña
# Contact: jerrypaulmagana@gmail.com
# Description: Implements a version of the Lagrange Interpolation algorithm. Used to get coefficients for interpolating
# polynomial.
# ==========================================================================================================================

# NOTICE: Code snippet is in alpha, and still needs debugging. Use at your own risk.

import numpy as np
import matplotlib.pyplot as plt

def lagrangeInterp(xpts,ypts,scale):
    if len(xpts) != len(ypts):
        print('Mismatched dimensions. Check your input.')
        return
    else:
        n = len(xpts)
        xmax = np.max(xpts)
        xmin = np.min(xpts)
        print('Min. x:',xmin)
        print('Max x:',xmax)
        t = np.linspace(xmin,xmax,scale)
        poly = 1
        lgConst = []
        for i in range(0,n-1):
            print('i =',i)
            k = 1
            for j in range(0,n-1):
                print('j =',j)
                if i != j:
                    k = np.multiply(
                        k,
                        np.divide(
                            np.subtract(
                                t,
                                xpts[j]
                                ),
                            np.subtract(
                                xpts[i],
                                xpts[j]
                                )
                            )
                        )
                    lgConst.append(k)
                else:
                    print('Step skipped')
                    continue
            print(lgConst)
            for l in lgConst:
                poly = np.add(
                        poly,
                        np.multiply(
                            ypts[i],
                            lgConst[i]
                            )
                        )
    return poly

x = [0,1,2,4]
y = [7,13,21,43]
t = np.linspace(-5,5,10)

lagrange = lagrangeInterp(x, y, 10)
plt.plot(t,lagrange)
plt.plot(x,y,'o',color='black')
plt.grid()
plt.show()

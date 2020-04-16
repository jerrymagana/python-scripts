# ==========================================================================================================================
# Title: hermiteInterp.py
# Author: Jerry Paul Magaña
# Contact: jerrypaulmagana@gmail.com
# Description: Code snippet implements Hermite Algorithm to produce constants for an osculating (interpolating) polynomial.
# ==========================================================================================================================

class hermiteInterp:
    def __init__(self,x,fx,dfx): # Constructor sets up intitial data points (x,f(x)) and first derivative (dfx) need.
        if len(x) == len(fx) == len(dfx):
            self.x = x
            self.fx = fx
            self.dfx = dfx
            # print(self.x) # Debugging
            # print(self.fx) # Debugging
            # print(self.dfx) # Debugging
        else:
            print('Data mismatch: Check your input.')
    def getConstants(self): # Implements the Hermite Algorithm to derive coefficients using a modified divided difference
        coef = []
        n = len(self.x)
        #print('n:',n) # Debugging
        z = [0 for i in range(n*2)]
        #print('z length:',len(z)) # Debugging
        Q = [[0 for i in range(n*2)] for j in range(n*2)] 
        #print('Q length:',len(Q)) # Debugging
        for i in range(0,n): # Divided difference replaces some values with f'(x) to avoid divide by zero, implemented here
            z[2*i] = z[2*i+1] = self.x[i]
            Q[0][2*i] = self.fx[i]
            Q[0][2*i+1] = self.fx[i]
            Q[1][2*i+1] = self.dfx[i]
            if i != 0:
                Q[1][2*i] = (Q[0][2*i]-Q[0][2*i-1])/(z[2*i]-z[2*i-1]) # This calculates Q for every other row, again to avoid divide-by-zero problem
        #print('z-list:',z)  # Debugging
        #print('Q-matrix:',Q) # Debugging
        for c in range(2,2*n+1): 
            for r in range(c,2*n):
                #print('Q: (',c,',',r,')')
                Q[c][r] = (Q[c-1][r]-Q[c-1][r-1])/(z[r]-z[r-c])  # Implementation of Thomas' Algorithm to solve tridiagonal matrix
        #print('Complete Q-Matrix:',Q) # Debugging
        for i in range(n*2):
            coef.append(Q[i][i]) # Appends pivots from above matrix to 'coef' list. These are the coefficients for the osculating polynomial
        return coef, z
# Everything below is a test implementation of the class defined above. If you are using this for your own code, you don't need this.
problem1 = hermiteInterp([8.3,8.6],[17.56492,18.50515],[3.116256,3.151762])
p1coefficients = problem1.getConstants()
print('Problem 1 Coefficients:',p1coefficients[0])
print('Problem 1 z-numbers:',p1coefficients[1])            
problem2 = hermiteInterp([0.8,1.0],[0.22363362,0.65809197],[2.1691753,2.0466965])
p2coefficients = problem2.getConstants()
print('Problem 2 Coefficients:',p2coefficients[0]),
print('Problem 2 z-numbers:',p2coefficients[1])

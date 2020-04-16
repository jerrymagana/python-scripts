# ==========================================================================================================================
# Title: spline_interp.py
# Author: Jerry Paul Magaña
# Contact: jerrypaulmagana@gmail.com
# Description: Code snippet implements an algorithm that determins the coeeficients for each spline needed to interpolate a 
# fixed set of points. Coefficients returned as 2d array, where each column is a different coefficient, and each row is a 
# different spline.
# ==========================================================================================================================

class natSpline: # Define class for Natural Spline
    def __init__(self,xlist,ylist): # Constructor accepts two lists for x and y coordinates, respectively.
        if len(xlist) != len(ylist): # Checks to make sure the number of x coordinates and y coordinates are the same.
            print('Data mismatch: Check your input.') # Returns an error if the number of x elements and y elements are different.
            self.x = [] # Initializes an empty list. Used to instantize object but disregards invalid parameters.
            self.y = [] # Same as above for y
            self.h = [] # Same as above for h. This will be the step-differences x[i+1]-x[i].
            return
        else:
            self.x = [a for a in xlist] # Copy input x list to local attribute.
            self.y = [b for b in ylist] # Copy input y list to local attribute.
            self.h = [0 for i in range(len(self.x)-1)] # Create new local attribute list from x list. This is used for the x step difference.
            for i in range(len(self.x)-1): # For loop creates x[i+1]-x[i] steps
                self.h[i] = self.x[i+1]-self.x[i]
            print('x-points:',self.x) # Prints lists (used for debuging)
            print('y-points:',self.y)
            print('Calculated h-values:',self.h)
        return
    def getCoefficients(self): # Method for calculating coefficients of splines. This is Algorithm 3.4 in the text.
        coef = [[1 for i in range(len(self.x))],[1 for i in range(len(self.x))],[1 for i in range(len(self.x))],[1 for i in range(len(self.x))]] # Initializes a list of list that will later return the coefficients of the spline.
        l = [1 for i in range(len(self.x))] # From here down, used to construct and 
        m = [0 for i in range(len(self.x))] # solve the tridiagonal linear system matrix
        z = [0 for i in range(len(self.x))] # This implementation is a variation of Thomas algorithm.
        alpha = [0 for i in range(len(self.x))]
        for i in range(1,len(self.x)-1):
            alpha[i] = (3/self.h[i])*(self.y[i+1]-self.y[i])-(3/self.h[i-1])*(self.y[i]-self.y[i-1])
        print('Alpha List:',alpha)
        for i in range(1,len(self.x)-1):
            l[i] = 2*(self.x[i+1]-self.x[i-1])-self.h[i-1]*m[i-1]
            m[i] = self.h[i]/l[i]
            z[i] = (alpha[i]-self.h[i-1]*z[i-1])/l[i]
        print('l-list:',l)
        print('m-list:',m)
        print('z-list:',z)
        c = [0 for i in range(len(self.x))] # Creates list for c-coefficients
        b = [0 for i in range(len(self.x))] # Creates list for b-coefficients
        d = [0 for i in range(len(self.x))] # Creates list for d-coefficients
        n = len(self.x) # sets n for indexing later
        j = n-2 # sets sub-index j based on n
        while j >= 0: # While loop used to count down from j=n-2 to j=0
            print('j-counter:',j)
            c[j] = z[j]-m[j]*c[j+1]
            b[j] = (self.y[j+1]-self.y[j])/self.h[j]-self.h[j]*(c[j+1]+2*c[j])/3
            d[j] = (c[j+1]-c[j])/(3*self.h[j])
            j -= 1
        print('b-coefficients:',b)
        print('c-coefficients:',c)
        print('d-coefficients:',d)
        for k in range(len(coef)): # Else-if chain used to set coef list with correct elements from b, c, and d.
            if k == 0:
                for i in range(len(self.y)):
                    coef[k][i] = self.y[i]
            elif k == 1:
                for i in range(len(b)):
                    coef[k][i] = b[i]
            elif k == 2:
                for i in range(len(c)):
                    coef[k][i] = c[i]
            elif k == 3:
                for i in range(len(d)):
                    coef[k][i] = d[i]
        return coef

problem1 = natSpline([0,1,2],[-3,-2,1])
print('Coefficients:',problem1.getCoefficients())
#problem2 = natSpline([0,1,2],[0,1,2])
#print('Coefficients:',problem2.getCoefficients())
diff_fx = natSpline([0.5,0.6,0.7],[0.4794,0.5646,0.6442])
print(diff_fx.getCoefficients())

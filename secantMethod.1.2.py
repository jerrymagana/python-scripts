import numpy as np
import matplotlib.pyplot as plt

def eq(x): # Used to describe the equation for which we are locating the root 'r'
    # y = np.sum([np.multiply(54,np.power(x,6)),np.multiply(45,np.power(x,5)),np.multiply(-102,np.power(x,4)),np.multiply(-69,np.power(x,3)),np.multiply(35,np.power(x,2)),np.multiply(16,x),-4])
    # y = np.sum([np.power(x,3),np.multiply(2,np.power(x,2)),np.multiply(10,x),-20])
    y = x**3-5*x+1
    return y

def eq2(x):
    y = np.sum([np.power(x,3),np.multiply(2,np.power(x,2)),np.multiply(10,x),-20])

def errorCalc(x): # Used to calculate the error between the approximated root 'p' and the true root 'r'.
    y = np.absolute(np.subtract(eq(x),0))
    return y

def secantMethod(p1,p2,maxit,tol): # Secant Method function
    convergence = []
    convergence.append(p1)
    convergence.append(p2)
    n = 0
    while n < maxit: # Prevents function from running past a certain max number of iterations
        n += 1
        fp1 = eq(p1) # Finds f(p1) using predefined equation
        fp2 = eq(p2) # Finds f(p2) using predefined equation
        if errorCalc(p2) < tol: # Prints the answer and breaks the loop if 'p' is sufficiently close to 'r'
            print('Convergence reached at r =',p2)
            break
        else:
            print('Step ',n,' out of ',maxit) # Prints step count to console for debugging
            p3 = np.subtract(p2,np.divide(np.multiply(fp2,np.subtract(p2,p1)),np.subtract(fp2,fp1))) #Defines next p value
            print('Step convergence: ',p3) # Prints to console current answer
            convergence.append(p3)
            p1 = p2 # Moves p2 to p1
            p2 = p3 # Sets new value to p2
            print('p1: ',p1) # Prints new values
            print('p2: ',p2)
    return p2, convergence

#xpts = np.linspace(-2,2,1000) # x-axis array for plotting
#ypts = eq(xpts) # y-axis array for plotting
#zeroline = np.zeros_like(ypts) # y=0 line for plotting
#plt.plot(xpts,ypts) 
#plt.plot(xpts,zeroline)
#plt.axis([-2,2,-25,10]) # Set margins so intercepts are visible
#plt.grid()
#plt.show()
#r1 = secantMethod(-1.5,-1.3,25,0.0001) # Finds roots on likely intervals
#r2 = secantMethod(-1,-0.5,25,0.0001)
#r3 = secantMethod(0,0.25,25,0.0001)
#r4 = secantMethod(0.25, 0.5, 25, 0.0001)
#r5 = secantMethod(1,1.5,25,0.0001)
r = secantMethod(0,1,25,0.0001)
print('Problem I.3.3.b: r =',r[0])
#print('Problem I.3.2: r =',r[0])
#print('Problem I.3.1: The roots of the equation are:',r1[0],r2[0],r3[0],r4[0],r5[0]) # Prints roots to console
root = r[0] # Extract final approximated root from tuple returned by secantMethod()
steps = r[1] # Extract list of approximations for convergence test
s = 0
if s <= len(steps): # Loop for calculating convergence speed
    a = np.absolute(np.subtract(steps[s+1],root))
    b = np.absolute(np.subtract(steps[s],root))
    x = np.divide(a,b)
    print('Convergence speed:',x)
    s += 1

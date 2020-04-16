import numpy as np
import matplotlib as plt

def funct01(x):
    fx = np.sum([np.power(x,3),np.multiply(2,np.power(x,2)),np.multiply(10,x),-20])
    return fx

#def funct02(x):
#    A = np.multiply(3,np.power(x,5))
#    B = np.multiply(5,np.power(x,3))
#    fx = np.multiply(2,np.subtract(A,B))
#    return fx

#def funct03(x):
#    fx = np.subtract(funct01(x),funct02(x))
#    return fx

def deriv01(x):
    fx = np.sum([np.multiply(3,np.power(x,2)),np.multiply(4,x),10])
    return fx

#def funct04(x):
#    A = np.multiply(np.multiply(2,x),np.log(x))
#    B = np.add(np.power(x,2),1)
#    C = np.power(x,2)
#    D = np.subtract(np.multiply(2,np.log(x)),1)
#    E = np.add(np.multiply(A,B),np.multiply(C,D))
#    fx = np.add(E,1)
#    return fx

#def deriv02(x):
#    A = np.multiply(2,np.power(x,2))
#    B = np.add(1,np.multiply(3,np.log(x)))
#    C = np.multiply(2,x)
#    D = np.multiply(2,np.log(x))
#    E = np.multiply(2,np.add(1,np.log(x)))
#    F = np.add(np.multiply(A,B),np.multiply(C,D))
#    fx = np.add(F,E)
#    return fx

#def funct05(x):
#    A = np.divide(1000,x)
#    B = np.divide(1,np.power(np.add(1,x),360))
#    C = np.subtract(1,B)
#    D = np.multiply(A,C)
#    fx = np.subtract(D,135000)
#    return fx

#def deriv03(x):
#    A = np.divide(1000,x)
#    B = np.divide(360,np.power(np.add(1,x),361))
#    C = np.divide(1,x)
#    D = np.divide(1,np.multiply(x,np.power(np.add(1,x),360)))
#    E = np.subtract(B,C)
#    F = np.subtract(E,D)
#    fx = np.multiply(A,F)
#    return fx

def newtons(p,tol,n):
    i = 1
    while i <= n:
        fp = funct01(p)
        dfp = deriv01(p)
        x = np.subtract(p,np.divide(fp,dfp))
        err = np.absolute(np.subtract(x,p))
        if err < tol:
            print('The approximate solution is: ',x)
            print('Accurate to within: ',tol)
            print('Step count:',i)
            break
        else:
            i = i+1
            p = x
    return x

def newtons02(p,tol,n):
    i = 1
    while i <= n:
        fp = funct04(p)
        dfp = deriv02(p)
        x = np.subtract(p,np.divide(fp,dfp))
        err = np.absolute(np.subtract(x,p))
        if err < tol:
            print('The approximate solution is: ',x)
            print('Accurate to within: ',tol)
            break
        else:
            i = i+1
            p = x
    return x

def newtons03(p,tol,n):
    i = 1
    while i <= n:
        fp = funct05(p)
        dfp = deriv03(p)
        x = np.subtract(p,np.divide(fp,dfp))
        err = np.absolute(np.subtract(x,p))
        if err < tol:
            print('The approximate solution is: ',x)
            print('Accurate to within: ',tol)
            break
        else:
            i = i+1
            p = x
    print('Final step solution: ',x)
    return x

#test = deriv03(256)
#print(test)

root = newtons(1,0.0001,20)
print(root)

#check = funct05(root)
#print('Sanity check: fx = ',check)

        
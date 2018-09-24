import numpy as np

def fun(x):
        a = x**2
        return (a)
        '''
        n = len(x)
        print 'n',n
        a = []
        for i in range(n):
                b = x[i]**2
                a.append(b)
        return sum(a)
        '''
'''
def sel_max_bin(population):
        a = max(population)
        b = np.binary_repr(a)
        return len(b)

def dec_bin(x,y):
        a = len(x)
        b = []
        for i in range(a):
                c =              
'''

def map_bin2real(xL,xU,a):
        s = []
        for i in range(len(a)):
                s.append(2**i * a[(len(a)-1) - i])
        return (xL + ((xU - xL)/(2**len(a) - 1.0))* sum(s))        

# Selection
def sel(a,b):
        x1 = map_bin2real(0,10,a)
        x2 = map_bin2real(0,10,b)
        #print 'x1',x1
        #print 'x2',x2
        f1 = fun(x1)
        f2 = fun(x2)
        if (f1 < f2):
                return a
        else:
                return b

# Cross-over 
def cross_over(a,b,B):#(xL,xU):
        a = np.hsplit(np.array(a),[4,B])
        b = np.hsplit(np.array(b),[4,B])
        a0 = list(a[0])
        a1 = list(a[1])
        b0 = list(b[0])
        b1 = list(b[1])
        c = a0 + b1
        d = b0 + a1
        return c,d

# Mutation
def mutation(a,B):
        v = np.random.random_integers(0,B-1)
        if (a[v] == 0):
                a[v] = 1
        else:
                a[v] = 0 
        return a
# GA
def GA(a,B,N):
        f = []
        f_max = 0 
        #a_s2 = []
        #a_c2 = []
        #a_m2 = []
        for i in range(N):
                # Selection Operation
                a_s = []
                while (len(a_s) < len(a)):
                        #print 'Selection Iteration'  
                        ls = np.random.random_integers(0,B-1)        
                        ms = np.random.random_integers(0,B-1)
                        a_s.append(sel(a[ls][:],a[ms][:]))

                # Cross-Over Operation
                a_c = []
                while (len(a_c) < len(a)):
                        #print 'Cross Over Iteration'
                        pc = 0.7
                        lc = np.random.random_integers(0,B-1)      
                        mc= np.random.random_integers(0,B-1)
                        #print 'lc',lc,'mc',mc
                        if (np.random.uniform(0,1) < pc):
                                ac1,ac2 = cross_over(a_s[lc][:],a_s[mc][:],B)
                                a_c.append(ac1)
                                a_c.append(ac2)

                # Mutation Operation
                a_m = []
                while (len(a_m) < len(a)):
                        pm = 0.01
                        lm = np.random.random_integers(0,B-1)
                        if (np.random.uniform(0,1) < pm):
                                am1 = mutation(a_c[lm][:],B)
                                a_m.append(am1)
                        else:
                                a_m.append(a_c[lm][:])

                f1 = []
                f1_at = []
                for i in range(len(a_m)):
                        f11_at = map_bin2real(0,10,a_m[i][:])
                        #print 'f11_at',f11_at,'in',i,'th iteration' 
                        f1_at.append(f11_at)
                        f11 = fun(f11_at)
                        #print 'f11',f11,'in',i,'th iteration'
                        f1.append(f11)
                #print 'f1',f1
                f1_max = max(f1)
                #print 'f1_max', f1_max
                if ( f_max < f1_max):
                        f_max = f1_max
                for i in range(len(a_m)):
                        if (f_max == f1[i]):
                                f_max_at = f1_at[i]
                #print 'f_max',f_max,'in',i,'th iteration' 
                a_s.append(a_s)
                a_c.append(a_c)
                a_m.append(a_m)
                #print f_max , f_max_at
        return f_max , f_max_at , a_m

# For generating initial trail solution 
B = 8 # No of bin
n = 8 # population size
a = []
for i in range(n):
        b = np.random.randint(2, size=B)
        a.append(b)

N = 100000 # max iteration
f_max , f_max_at , a_m = GA(a,B,N)
 
 
N1 = int(0.5 * N)
f_max1 , f_max_at1 , a_m1 = GA(a_m,B,N1)
while (f_max < f_max1):
        f_max = f_max1
        f_max_at = f_max_at1
        a_m = a_m1
        f_max1 , f_max_at1 , a_m1 = GA(a_m,B,N1)
print 'f_max', f_max
print 'f_max_at',f_max_at

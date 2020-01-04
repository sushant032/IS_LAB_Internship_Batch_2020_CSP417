def checkPrimitiveRoot(N,R):
    alist=dict.fromkeys(range(1,N), False)
    for i in range(N-1):
        temp=pow(R,i,N) 
        if alist[temp]==False:
            alist[temp]=not alist[temp]
        else:
            return False
    return True 

checkPrimitiveRoot(23,10)


def findRoot(N):
    collectRoots = []

    for i in range(1,N):
        if checkPrimitiveRoot(N,i):
            print("{} is the Primitive Root module  {}".format(i,N))
            collectRoots.append(i)
    
    return collectRoots


findRoot(23)

def generateDiscreteLogTable(N,g):
    collectRoots=findRoot(N)
    if g not in collectRoots:
        print(" {} not Root of {}".format(g,N))
        return 
    table=dict.fromkeys(range(1,N),0)
    for i in range(N-1):
        temp=pow(g,i,N)
        table[temp]=i
       
    print("\nTABLE FOR DISCRETE LOGARITHM OF {} under module {}".format(g,N))
    print("N\tLog(g)[N]")
    for k,v in table.items():
        print("{}\t{}".format(k,v))

generateDiscreteLogTable(23,10)


P = 23    
G = 10    

a = 6     
b = 15   


print( "Publicly Shared Variables:")
print( "    Publicly Shared Prime: " , P)
print( "    Publicly Shared Base:  " , G)



x = (G**a)%P

print('a sends msg to b:', str(x))




y = (G**b)%P

print('b sends msg to a:', str(y))



a_SharedSecret = (y**a)%P

b_SharedSecret = (x**b)%P

print('Shared Secret of a: ', a_SharedSecret)

print('Shared Secret of b: ', b_SharedSecret)


def Euclidean(numer:int, denom:int)->tuple:
    """
    Euclidean Algorithm
    辗转相除法
    """
    a, b = numer, denom
    while b:
        a, b = b, a % b
    return (numer // a, denom // a)

#print(Euclidean(19132241174083603, 267163316146024169))

##from time import time
##s = time()
##print(Euclidean(19132241174083603, 267163316146024169))
##print(time() - s)

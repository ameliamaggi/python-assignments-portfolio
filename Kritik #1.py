x = float(input("Enter a Number: "))
n = 0


def approximatingarctan (i):
    arctanxapprox = (((-1)**i)*(x**(2*i+1)))/(2*i+1)
    global n
    n += 1
    return arctanxapprox


if (0<=x<=1):
    i = 0
    a = approximatingarctan(i)
    errorbound = (x**((2*n)+1))/((2*n)+1)
    while (errorbound>0.0001):
        i += 1
        a += approximatingarctan(i)
        errorbound = (x**((2*n)+1))/((2*n)+1)
    print (a, n, errorbound)
else:
    print ("Error!")
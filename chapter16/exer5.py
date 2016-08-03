def calSal(p,i,n):
    if n == 1:
        return p*(i+1)
    else:
        return (i+1)*calSal(p, i, n-1)

print 100*pow(1.1, 20)
print calSal(100, 0.1, 20)
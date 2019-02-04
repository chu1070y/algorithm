def comb(n,r):

      if r ==0:
          return 1

      return comb(n,r-1)*(n-r+1)/r

print(comb(6,3))
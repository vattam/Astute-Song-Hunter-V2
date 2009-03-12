import math

def normalize(L):
  I = [i for i in range(1,len(L)+1)]
  II = [i*i for i in I]
  IL = []
  for i in I:
    IL.append(i*L[i-1])
  b = (len(I)*sum(IL) - sum(I)*sum(L)) / (len(I)*sum(II) - sum(I)*sum(I))
  return b

def rms(L,I):
  M = []
  j = 0
  for i in I:
    M.append((i-L[j])**2)
    j += 1
  return (sum(M)/len(M))**(-1)

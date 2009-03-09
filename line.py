import math

def normalize(L):
  I = [i for i in range(1,len(L)+1)]
  II = [i*i for i in I]
  IL = []
  for i in I:
    IL.append(i*L[i-1])
  b = (len(I)*sum(IL) - sum(I)*sum(L)) / (len(I)*sum(II) - sum(I)*sum(I))
  a = (sum(L) - b*sum(I)) / len(I)
  return b

def angle(m1,m2):
  if m1 > m2 :
    m1,m2 = m2,m1
  return math.atan((m2-m1)/(1+m1*m2))

def rms(L,I):
  M = []
  j = 0
  for i in I:
    M.append((i-L[j])**2)
    j += 1
#  return math.sqrt(sum(M)/len(M))
  return (sum(M)/len(M))**(-1)

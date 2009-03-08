def normalize(L):
  I = [i for i in range(len(L))]
  II = [i*i for i in I]
  IL = []
  for i in I:
    IL.append(i*L[i])
  b = (len(I)*sum(IL) - sum(I)*sum(L)) / (len(I)*sum(II) - sum(I)*sum(I))
  a = (sum(L) - b*sum(I)) / len(I)
  return a,b
  


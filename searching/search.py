import math
import pickle

File = open("tags.db","r")
Tag_List = pickle.load(File)
File.close()
Min_Threshold = (3e-03,10)

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
  return (sum(M)/len(M))**(-1)

def search_by_regression(Slope):
  Match = []
  for Tag in Tag_List:
    Min = False
    for S in Tag[1]:
      if angle(Slope,S) < Min_Threshold[0]:
        Min = True
        break
    if Min:
      Match.append(Tag[0])
  return Match

def search_by_max_min(Maxima,Minima):
  Match = []
  for Tag in Tag_List:
    Min = False
    for Var in Tag[2]:
      a = rms(Maxima,Var[0])
      b = rms(Minima,Var[1])
#      print abs(a-b)
      if int(abs(a-b)*(10**5)) < Min_Threshold[1]:
        Min = True
        break
    if Min:
      Match.append(Tag[0])
  return Match


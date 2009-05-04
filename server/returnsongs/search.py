import math

class SongTune :
  def __init__(self, Slope, MaxList, MinList):
    self.MinSlopeThreshold = 3e-03
    self.MaxMinThreshold = 10
    self.Slope = Slope
    self.MaxList = MaxList
    self.MinList = MinList

  def FindAngle(m1,m2):
    if m1 > m2 :
      m1,m2 = m2,m1
    return math.atan((m2-m1)/(1+m1*m2))

  def CalculateRMS(L,I):
    M = []
    j = 0
    for i in I:
      M.append((i-L[j])**2)
      j += 1
    return (sum(M)/len(M))**(-1)

  def SearchByRegression(S):
      if FindAngle(self.Slope,S) < self.MinSlopeThreshold:
        return True
    return False

  def FindMaxMin(Maxima,Minima):
    a = CalculateRMS(Maxima,self.MaxList)
    b = CalculateRMS(Minima,self.MinList)
    if int(abs(a-b)*(10**5)) < self.MaxMinThreshold:
      return True
    return False


import math

class SongTune :
  def __init__(self, Slope, MaxList, MinList):
    self.MinSlopeThreshold = 3e-03
    self.MaxMinThreshold = 5
    self.Slope = Slope
    self.MaxList = MaxList
    self.MinList = MinList

  def FindAngle(self,m1,m2):
    if m1 > m2 :
      m1,m2 = m2,m1
    return math.atan((m2-m1)/(1+m1*m2))

  def CalculateRMS(self,L,I):
    M = []
    j = 0
    for i in I:
      M.append((i-L[j])**2)
      j += 1
    return (sum(M)/len(M))**(-1)

  def SearchByRegression(self,S):
      if self.FindAngle(self.Slope,S) < self.MinSlopeThreshold:
        return True
      return False

  def FindMaxMin(self,Maxima,Minima):
    a = self.CalculateRMS(Maxima,self.MaxList)
    b = self.CalculateRMS(Minima,self.MinList)
    print a,b
    if int(abs(a-b)*(10**5)) < self.MaxMinThreshold:
      return True
    return False


import math


class PS1:
  def __init__(self,a,b) -> None:
    self.a=a
    self.b=b
  def show(self):
    self.rutgon()
    print(f"{self.a}/{self.b}")
  def rutgon(self):
    gcd=math.gcd(self.a,self.b)
    self.a=str(int(self.a/gcd))
    self.b=str(int(self.b/gcd))
arr=input().split()
ps=PS1(int(arr[0]),int(arr[1]))
ps.show()

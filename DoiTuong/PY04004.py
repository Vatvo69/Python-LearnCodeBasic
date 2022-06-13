import math


class PS2:
  def __init__(self,tu,mau) -> None:
    self.tu=tu
    self.mau=mau
  def show(self):
    self.rutgon()
    print(f"{int(self.tu)}/{int(self.mau)}")

  def rutgon(self):
    gcd = math.gcd(self.tu,self.mau)
    self.tu=self.tu/gcd
    self.mau=self.mau/gcd

  def sum(self,ps):
    self.tu=self.tu*ps.mau+self.mau*ps.tu
    self.mau=self.mau*ps.mau

arr=input().split()
ps1=PS2(int(arr[0]),int(arr[1]))
ps2=PS2(int(arr[2]),int(arr[3]))
ps1.sum(ps2)
ps1.show()
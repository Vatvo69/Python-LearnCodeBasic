class ThiSinh1:
  def __init__(self,ten,nam,d1,d2,d3) -> None:
    self.ten=ten
    self.nam=nam
    self.d1=d1
    self.d2=d2
    self.d3=d3
  def solve(self):
    tong=(self.d1+self.d2+self.d3)
    return tong
  def __repr__(self) -> str:
    return f"{self.ten} {self.nam} {format(self.solve(),'.1f')}"
ten=input() 
nam=input()
d1=float(input())
d2=float(input())
d3=float(input())
ts1=ThiSinh1(ten,nam,d1,d2,d3)
print(ts1)
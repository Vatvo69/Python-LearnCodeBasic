class Rectangle:
  def __init__(self,a,b,c) -> None:
    self.a=a
    self.b=b
    self.c=c
  def perimeter(self):
    return 2*(self.a+self.b)
  def area(self):
    return self.a*self.b
  def color(self):
    return self.c.title()
  def isValid(self):
    return self.a>0 and self.b>0
arr=input().split()
r=Rectangle(int(arr[0]),int(arr[1]),arr[2])
if r.isValid():
  print(f"{r.perimeter()} {r.area()} {r.color()}")
else:
  print("INVALID")
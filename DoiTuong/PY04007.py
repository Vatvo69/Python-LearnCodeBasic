from time import sleep


t=int(input())
class Matrix:
  def __init__(self,m,n,a) -> None:
    self.m=m
    self.n=n
    self.a=a

  def solve(self):
    for i in range(self.m):
      for j in range(self.m):
        sum=0
        for k in range(self.n):
          sum+=(self.a[i][k]*self.a[j][k])
        print(sum,end=" ")
      print()
while t>0:
  arr=input().split()
  m,n=int(arr[0]),int(arr[1])
  a = [[int(i) for i in input().split()] for j in range(m)]
  mt=Matrix(m,n,a)
  mt.solve()
  t-=1
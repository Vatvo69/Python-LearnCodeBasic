import math
import datetime


class ThiSinh:
    def __init__(self, name, address, end):
        self.name = name
        self.address = address
        self.end = end
        self.hour = 0
        self.id = ""
        self.vantoc = 0

    def getma(self):
        ans = ''.join([i[0] for i in self.address.split()])
        ans += ''.join([i[0] for i in self.name.split()])
        self.id = ans

    def tinhtoan(self):
        start = datetime.datetime.strptime('6:00', '%H:%M')
        end = datetime.datetime.strptime(self.end, '%H:%M')
        dis = (end-start)
        h = dis.seconds/3600
        self.vantoc = 120/h

    def __str__(self):
        return f"{self.id} {self.name} {self.address} {round(self.vantoc)} Km/h"


lst = []
for i in range(int(input())):
    name = input()
    address = input()
    end = input()
    ts = ThiSinh(name, address, end)
    ts.getma()
    ts.tinhtoan()
    lst.append(ts)
lst = sorted(lst, key=lambda x: x.vantoc, reverse=True)
for i in lst:
    print(i)

from datetime import datetime


class VanToc:
    def __init__(self, id, name, city, time):
        self.id = id
        self.name = name
        self.city = city
        self.time = time
        self.vanToc = 0

    def Tinh(self):
        a = datetime.strptime("6:00", "%H:%M")
        b = datetime.strptime(self.time, "%H:%M")
        self.vanToc = (120/((b-a).seconds/3600))

    def __str__(self):
        return f"{self.id} {self.name} {self.city} {round(self.vanToc)} Km/h"


if __name__ == '__main__':
    T = int(input())
    listVT = []
    while T > 0:
        name = input()
        city = input()
        time = input()
        id = ''.join(i[0] for i in city.split())
        id += ''.join([i[0] for i in name.split()])
        v = VanToc(id, name, city, time)
        v.Tinh()
        listVT.append(v)
        T -= 1
    sortList = sorted(listVT, key=lambda x: (x.vanToc*(-1)))
    print(*sortList, sep="\n")

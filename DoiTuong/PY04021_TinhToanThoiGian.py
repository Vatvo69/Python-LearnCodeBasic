def Tinh(gioVao, gioRa):
    h1, m1 = gioVao.split(":")
    t1 = int(h1) * 60 + int(m1)
    h2, m2 = gioRa.split(":")
    t2 = int(h2) * 60 + int(m2)
    return t2 - t1


class ThoiGian:
    def __init__(self, id, name, time):
        self.id = id
        self.name = name
        self.time = time

    def __str__(self):
        h = int(self.time / 60)
        return f"{self.id} {self.name} {h} gio {self.time-h*60} phut"


if __name__ == "__main__":
    T = int(input())
    listTG = []
    while T > 0:
        id = input()
        name = input()
        gioVao = input()
        gioRa = input()
        tg = ThoiGian(id, name, Tinh(gioVao, gioRa))
        listTG.append(tg)
        T -= 1
    sortList = sorted(listTG, key=lambda x: (x.time * (-1)))
    print(*sortList, sep="\n")

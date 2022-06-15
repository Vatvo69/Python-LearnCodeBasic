from decimal import Decimal


def Tinh(soCu, soMoi):
    d = soMoi - soCu
    if d <= 50:
        d *= 100
        d += d * 0.02
    elif d <= 100:
        d = 50 * 100 + (d - 50) * 150
        d += d * 0.03
    else:
        d = 50 * 100 + 50 * 150 + (d - 100) * 200
        d += d * 0.05
    return round(d)


class HoaDon:
    def __init__(self, id, ten, soCu, soMoi, tong):
        self.id = id
        self.ten = ten
        self.soCu = soCu
        self.soMoi = soMoi
        self.tong = tong

    def __str__(self):
        return f"{self.id} {self.ten} {self.tong}"


if __name__ == "__main__":
    T = int(input())
    listKH = []
    for i in range(1, T + 1):
        ten = input()
        soCu = int(input())
        soMoi = int(input())
        id = "KH{:02d}".format(i)
        hd = HoaDon(id, ten, soCu, soMoi, Tinh(soCu=soCu, soMoi=soMoi))
        listKH.append(hd)
    sortList = sorted(listKH, key=lambda x: (x.tong * (-1)))
    print(*sortList, sep="\n")

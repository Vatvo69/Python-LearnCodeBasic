from decimal import ROUND_HALF_UP, Decimal


class BangDiem:
    def __init__(self, ma, ten, diem):
        self.ma = ma
        self.ten = ten
        self.diem = diem

    def xepLoai(self):
        if self.diem >= 9.0:
            return "XUAT SAC"
        elif self.diem >= 8.0:
            return "GIOI"
        elif self.diem >= 7.0:
            return "KHA"
        elif self.diem >= 5.0:
            return "TB"
        else:
            return "YEU"

    def __str__(self) -> str:
        xl = self.xepLoai()
        return f"{self.ma} {self.ten} {self.diem} {xl}"


if __name__ == "__main__":
    T = int(input())
    listBD = []
    for k in range(1, T + 1):
        ten = input()
        arr = input().split()
        dtb = 0
        for i in arr:
            dtb += Decimal(i)
        dtb += Decimal(arr[0]) + Decimal(arr[1])
        dtb = dtb / 12
        id = "HS{:02d}".format(k)
        bd = BangDiem(id, ten, dtb.quantize(Decimal('0.1'),ROUND_HALF_UP))
        listBD.append(bd)
    sortList = sorted(listBD, key=lambda x: (x.diem * (-1), x.ma))
    print(*sortList, sep="\n")

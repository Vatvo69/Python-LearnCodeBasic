from datetime import datetime


def getTenTheLoai(listT1, id):
    for i in listT1:
        if i == id:
            return listT1[i]


class Phim:
    def __init__(self, id, maTL, ngay, ten, soTap, tenTL):
        self.id = id
        self.maTL = maTL
        self.ngay = ngay
        self.ten = ten
        self.soTap = soTap
        self.tenTL = tenTL
        self.day = 0

    def getNgay(self):
        arr = ngay.split("/")
        n = arr[2] + "/" + arr[1] + "/" + arr[0]
        d = datetime.strptime(n, "%Y/%m/%d")
        self.day = d.day

    def __str__(self):
        return f"{self.id} {self.tenTL} {self.ngay} {self.ten} {self.soTap}"


if __name__ == "__main__":
    T1, T2 = (int(i) for i in input().split())
    listT1 = {}
    for i in range(1, T1 + 1):
        id = "TL{:03d}".format(i)
        name = input()
        listT1[id] = name
    listT2 = []
    for i in range(1, T2 + 1):
        id = "P{:03d}".format(i)
        maTL = input()
        ngay = input()
        ten = input()
        soTap = int(input())
        tenTl = getTenTheLoai(listT1, maTL)
        p = Phim(id, maTL, ngay, ten, soTap, tenTl)
        p.getNgay()
        listT2.append(p)
    sortList = sorted(listT2, key=lambda x: (x.day * (-1), x.ten, x.soTap * (-1)))
    print(*sortList, sep="\n")

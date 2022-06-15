class HoaDon:
    def __init__(self, id, ten, soLuong, donGia, tienCK):
        self.id = id
        self.ten = ten
        self.soLuong = soLuong
        self.donGia = donGia
        self.tienCK = tienCK
        self.tien = 0

    def getGia(self):
        self.tien = self.soLuong * self.donGia - self.tienCK

    def __str__(self):
        return f"{self.id} {self.ten} {self.soLuong} {self.donGia} {self.tienCK} {self.tien}"


if __name__ == "__main__":
    T = int(input())
    listHD = []
    for i in range(1, T + 1):
        id = input()
        ten = input()
        soLuong = int(input())
        donGia = int(input())
        tienCK = int(input())
        dh = HoaDon(id, ten, soLuong, donGia, tienCK)
        dh.getGia()
        listHD.append(dh)
    sortList=sorted(listHD,key=lambda x:(x.tien*(-1)))
    print(*sortList, sep="\n")

from datetime import datetime


def tinhSoNgay(ngayNhan, ngayTra):
    arr = ngayNhan.strip().split("/")
    arr1 = ngayTra.strip().split("/")
    ngayNhan = arr[2]+"/"+arr[1]+"/"+arr[0]
    ngayTra = arr1[2]+"/"+arr1[1]+"/"+arr1[0]
    a = datetime.strptime(ngayNhan, "%Y/%m/%d")
    b = datetime.strptime(ngayTra, "%Y/%m/%d")
    return b-a


class HoaDon:
    def __init__(self, id, ten, phong, soNgay, phatSinh):
        self.id = id
        self.ten = ten
        self.phong = phong
        self.soNgay = soNgay
        self.phatSinh = phatSinh
        self.chiPhi = 0

    def Tinh(self):
        if self.phong[0] == "1":
            self.chiPhi = 25*self.soNgay+self.phatSinh
        elif self.phong[0] == "2":
            self.chiPhi = 34*self.soNgay+self.phatSinh
        elif self.phong[0] == "3":
            self.chiPhi = 50*self.soNgay+self.phatSinh
        elif self.phong[0] == "4":
            self.chiPhi = 80*self.soNgay+self.phatSinh

    def __str__(self):
        return f"{self.id} {self.ten} {self.phong} {self.soNgay} {self.chiPhi}"


if __name__ == '__main__':
    T = int(input())
    dem = 1
    listHD = []
    for i in range(T):
        id = "KH{:02d}".format(dem)
        ten = input().strip()
        phong = input().strip()
        ngayNhan = input().strip()
        ngayTra = input().strip()
        phatSinh = int(input())
        soNgay = int(tinhSoNgay(ngayNhan, ngayTra).days+1)
        hd = HoaDon(id, ten, phong, soNgay, phatSinh)
        hd.Tinh()
        listHD.append(hd)
        dem += 1
    sortList = sorted(listHD,key=lambda x: (x.chiPhi*(-1)))
    print(*sortList,sep="\n")

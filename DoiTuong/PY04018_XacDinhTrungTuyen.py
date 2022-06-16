from decimal import Decimal


class TrungTuyen:
    def __init__(self, id, name, maMH, mon1, mon2):
        self.id = id
        self.name = name
        self.maMH = maMH
        self.mon1 = mon1
        self.mon2 = mon2
        self.mon = ""
        self.diemUT = 0
        self.tongDiem = 0
        self.xepLoai = ''

    def getMon(self):
        if self.maMH[0] == 'A':
            self.mon = "TOAN"
        elif self.maMH[0] == "B":
            self.mon = "LY"
        else:
            self.mon = "HOA"

    def getXepLoai(self):
        if self.tongDiem >= 18:
            self.xepLoai = "TRUNG TUYEN"
        else:
            self.xepLoai = "LOAI"

    def getUuTien(self):
        if self.maMH[1] == '1':
            self.diemUT = Decimal(2.0)
        elif self.maMH[1] == '2':
            self.diemUT = Decimal(1.5)
        elif self.maMH[1] == '3':
            self.diemUT = Decimal(1.0)
        else:
            self.diemUT = 0

    def getTongDiem(self):
        self.tongDiem = self.mon1*2+self.mon2+self.diemUT

    def __str__(self):
        return f"{self.id} {self.name} {self.mon} {round(self.tongDiem,1)} {self.xepLoai}"


if __name__ == '__main__':
    T = int(input())
    listSV=[]
    for i in range(1, T + 1):
        name = input()
        maMH = input()
        mon1 = Decimal(input())
        mon2 = Decimal(input())
        id = "GV{:02d}".format(i)
        tt = TrungTuyen(id, name, maMH, mon1, mon2)
        tt.getMon()1
        tt.getUuTien()
        tt.getTongDiem()
        tt.getXepLoai()
        listSV.append(tt)
    sortList=sorted(listSV,key=lambda x:(x.tongDiem),reverse=True)
    print(*sortList,sep="\n")

import bdb


def change(s):
    h,m=s.split(":")
    return int(h)*60+int(m)
class LuongMua:
    def __init__(self,id,ten,bd,kt,mua) -> None:
        self.id='T'+'%02d'%id
        self.ten=ten
        self.bd=bd
        self.kt=kt
        self.mua=mua
        self.tGian=change(kt)-change(bd)
    def setTG(self,x,y):
        self.tGian+=change(y)-change(x)

    def setMua(self,x):
        self.mua+=x
        
    def __str__(self) -> str:
        return f"{self.id} {self.ten} {format(self.mua/self.tGian*60,'.2f')}"
if __name__ == '__main__':
    T=int(input())
    listLM=[]
    dem=1
    while T>0:
        ten=input()
        ok=0
        for i in listLM:
            if i.ten == ten:
                i.setTG(input(),input())
                i.setMua(int(input()))
                ok=1
                break
        if ok==0:
            listLM.append(LuongMua(dem,ten,input(),input(),int(input())))
            dem+=1
        T-=1
    print(*listLM,sep="\n")
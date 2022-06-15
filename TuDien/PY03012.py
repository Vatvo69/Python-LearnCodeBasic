class BangXepHang:
    def __init__(self, ten, c, t) -> None:
        self.ten = ten
        self.c = c
        self.t = t

    def __str__(self):
        return f"{self.ten} {self.c} {self.t}"

    def __repr__(self):
        return f"{self.ten} {self.c} {self.t}"


if __name__ == '__main__':
    T = int(input())
    listSV = []
    while T > 0:
        ten = input()
        arr = input().split()
        sv = BangXepHang(ten, int(arr[0]), int(arr[1]))
        listSV.append(sv)
        T -= 1
    sortList = sorted(listSV, key=lambda x: (x.c*(-1),x.t,x.ten))
    print(*sortList, sep="\n")

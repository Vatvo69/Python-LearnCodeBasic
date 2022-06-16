class ChuyenCan:
    def __init__(self, id, ten, lop):
        self.id = id
        self.ten = ten
        self.lop = lop
        self.diem = 10
        self.note = ''

    def Tinh(self, arr):
        for i in arr:
            if i == 'v':
                self.diem -= 2
            elif i == 'm':
                self.diem -= 1
        if self.diem <= 0:
            self.diem = 0
            self.note = 'KDDK'

    def __str__(self):
        return f"{self.id} {self.ten} {self.lop} {self.diem} {self.note}"

    def __repr__(self):
        return f"{self.id} {self.ten} {self.lop} {self.diem} {self.note}"


if __name__ == '__main__':
    T = int(input())
    listCC = {}
    for _ in range(T):
        id = input()
        ten = input()
        lop = input()
        listCC.update({id: ChuyenCan(id, ten, lop)})
    for _ in range(T):
        arr = input().split()
        listCC[arr[0]].Tinh(arr[1])
    print(*list(listCC.values()), sep='\n')

if __name__ == "__main__":
    T1, T2 = (int(i) for i in input().split())
    listT1 = {}
    for i in range(1, T1 + 1):
        maMonHoc = input()
        tenMonHoc = input()
        listT1[maMonHoc] = tenMonHoc
    listT2 = []
    for i in range(1,T2+1):
      id="T{:03d}".format(i)
      
import re


def solve(s):
    line = re.split('\.|\?|\!', s)
    for i in line:
        if i == "":
            continue
        print(" ".join(i.split()).capitalize())


if __name__ == '__main__':
    s = ""
    while True:
        try:
            s += input().lower()
        except:
            break
    solve(s)

import sys
args = sys.argv

math = int(args[1])
japa = int(args[2])
eng = int(args[3])

if math>=50 and japa>=50 and eng>=50:
    if math>=70 and japa >=70 and eng>=70:
        print("合格", end="")
    elif math+japa+eng>=220:
        print("合格", end="")
    else:
        print("不合格", end="")
else:
    print("不合格", end="")
import sys
args = sys.argv

sub_a = int(args[1])
sub_b = int(args[2])
sub_c = int(args[3])

if sub_a < 50 or sub_b < 50 or sub_c < 50:
    print("不合格",end="")
elif sub_a+sub_b+sub_c >= 220 or(sub_a >= 70 and sub_b >= 70 and sub_c >= 70):
    print("合格",end="")
else:
    print("不合格",end="")


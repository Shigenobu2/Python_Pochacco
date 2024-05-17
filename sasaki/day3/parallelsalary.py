#四捨五入用のモジュール
from decimal import Decimal, ROUND_HALF_UP
# 給与計算の自作モジュール
import func_salary
# 引数渡しのモジュール
import sys
args = sys.argv

# 引数の数だけ繰り返す
for arg in args[1:]:
    # 関数の呼び出し
    result, tax = func_salary.calc_salary(int(arg))
    # 結果の出力
    print("給与額:" + str(Decimal(arg).quantize(Decimal("0"),rounding=ROUND_HALF_UP)) 
        + "、支給額:" + str(Decimal(result).quantize(Decimal("0"),rounding=ROUND_HALF_UP)) 
        + "、税額:" + str(Decimal(tax).quantize(Decimal("0"),rounding=ROUND_HALF_UP)))



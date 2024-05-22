import sys
from sqlalchemy import Column, String, Date, Integer, VARCHAR
from database import Base
from database import ENGINE

# テーブル：商品マスタ(mst_merchandise)の定義
class Mst_Merchandise(Base):
     __tablename__ = 'mst_merchandise'
     mst_id = Column('id', VARCHAR(10), primary_key = True) # 商品ID
     mst_name = Column('name', VARCHAR(20))     # 商品名
     mst_price = Column('int', int)             # 一個当たりの金額

# テーブル：商品在庫テーブル(tbl_stock)の定義
class Tbl_Stock(Base):
     __tablname__ = 'tbl_stock' 
     stock_id = Column('id', VARCHAR(10), primary_key = True)   # 商品ID
     stock_stock = Column('stock', int)         # 自動販売機内の在庫

# テーブル：貨幣格納テーブル(tbl_money)の定義
class Tbl_Money(Base):
     __tablname__ = 'tbl_money'
     money_price = Column('price', int, primary_key = True) # 金種（1000円、500円など）
     money_number = Column('number', int)   # 自動販売機に入っている枚数

# テーブル：メッセージテーブル(tbl_message)の定義
class Tbl_Message(Base):
     __tablname__ = 'tbl_money'
     money_price = Column('price', int, primary_key = True) # 金種（1000円、500円など）
     money_number = Column('number', int)   # 自動販売機に入っている枚数



def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)
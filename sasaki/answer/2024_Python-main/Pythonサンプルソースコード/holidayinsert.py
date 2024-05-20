from datetime import date
from database import session
from tables import Holiday

# 登録するデータの編集
holiday= Holiday(
    holi_date = date(2024, 2, 12),
    holi_text = "振替休日"
)

#INSERT処理
session.add(holiday)
#コミット
session.commit()

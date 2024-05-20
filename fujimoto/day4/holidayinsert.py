from datetime import date
from database import session
from tables import Holiday

# 登録するデータの編集
jan1= Holiday(
    holi_date = date(2024, 1, 1),
    holi_text = "元日"
)

jan8= Holiday(
    holi_date = date(2024, 1, 8),
    holi_text = "成人の日"
)

feb11= Holiday(
    holi_date = date(2024, 2, 11),
    holi_text = "建国記念の日"
)

feb12= Holiday(
    holi_date = date(2024, 2, 12),
    holi_text = "振替休日"
)

feb23= Holiday(
    holi_date = date(2024, 2, 23),
    holi_text = "天皇誕生日"
)

mar20= Holiday(
    holi_date = date(2024, 3, 20),
    holi_text = "春分の日"
)

apr29= Holiday(
    holi_date = date(2024, 4, 29),
    holi_text = "昭和の日"
)

may3= Holiday(
    holi_date = date(2024, 5, 3),
    holi_text = "憲法記念日"
)

may4= Holiday(
    holi_date = date(2024, 5, 4),
    holi_text = "みどりの日"
)

may5= Holiday(
    holi_date = date(2024, 5, 5),
    holi_text = "こどもの日"
)

may6= Holiday(
    holi_date = date(2024, 5, 6),
    holi_text = "振替休日"
)

jul15= Holiday(
    holi_date = date(2024, 7, 15),
    holi_text = "海の日"
)

aug11= Holiday(
    holi_date = date(2024, 8, 11),
    holi_text = "山の日"
)

aug12= Holiday(
    holi_date = date(2024, 8, 12),
    holi_text = "振替休日"
)

sep16= Holiday(
    holi_date = date(2024, 9, 16),
    holi_text = "敬老の日"
)

sep22= Holiday(
    holi_date = date(2024, 9, 22),
    holi_text = "秋分の日"
)

sep23= Holiday(
    holi_date = date(2024, 9, 23),
    holi_text = "振替休日"
)

oct14= Holiday(
    holi_date = date(2024, 10, 14),
    holi_text = "スポーツの日"
)

nov3= Holiday(
    holi_date = date(2024, 11, 3),
    holi_text = "文化の日"
)

nov4= Holiday(
    holi_date = date(2024, 11, 4),
    holi_text = "振替休日"
)

nov23= Holiday(
    holi_date = date(2024, 11, 23),
    holi_text = "勤労感謝の日"
)

#INSERT処理
session.add(jan1)
session.add(jan8)
session.add(feb11)
session.add(feb12)
session.add(feb23)
session.add(mar20)
session.add(apr29)
session.add(may3)
session.add(may4)
session.add(may5)
session.add(may6)
session.add(jul15)
session.add(aug11)
session.add(aug12)
session.add(sep16)
session.add(sep22)
session.add(sep23)
session.add(oct14)
session.add(nov3)
session.add(nov4)
session.add(nov23)
#コミット
session.commit()

from datetime import datetime, timedelta

due = [
    ('завтра 12:45', 'ru', datetime.now().replace(hour=12, minute=45, second=0, microsecond=0) + timedelta(days=1)),
    ('послезавтра 22:11', 'ru', datetime.now().replace(hour=22, minute=11, second=0, microsecond=0) + timedelta(days=2)),
    ('через неделю в 09:51', 'ru', datetime.now().replace(hour=9, minute=51, second=0, microsecond=0) + timedelta(days=7)),
]

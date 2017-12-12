
from datetime import datetime
# 获取当前日期和时间
now = datetime.now()
print(now)
print(type(now))
# 获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20)
print(dt)
# 在计算机中，时间实际上是用数字表示的。
# 我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，
# 记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp
# datetime转换为timestamp
print(dt.timestamp())
# timestamp转换为datetime
print(datetime.fromtimestamp(dt.timestamp()))
print(datetime.utcfromtimestamp(dt.timestamp()))

# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
# datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H %M'))

# datetime 加减
from datetime import timedelta
now = datetime.now()
print(now)
now = now + timedelta(hours=10)
print(now)
now = now - timedelta(days=1)
print(now)
now = now + timedelta(days=2, hours=12)
print(now)

# 本地时间转换为UTC时间
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8)
print(dt)

# 时区转换
# 拿到UTC时间，并强制设置时区为UTC+0.00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将转换时区为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)

#如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
import datetime

d1 = datetime.datetime.strptime('20111107', '%Y%m%d')
d2 = datetime.datetime.strptime('20180903', '%Y%m%d')
delta = datetime.timedelta(days=7)
while d1 <= d2:
    print (type(d1.strftime('%Y%m%d')), d1.strftime('%Y%m%d'))
    d1 = d1 + delta
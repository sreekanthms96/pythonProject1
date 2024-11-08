import datetime
now = datetime.datetime.now()

print(now.strftime("%d/%m/%Y")) #to format date in dd/mm/yyyy we can use (%d/%m/%Y) and to format date in dd/mm/yy we can use %d/%m/%y (intead of "/" we can use "- or :" also to print in that format)

print(datetime.date.today().day) #print day only
print(datetime.date.today().month) #print month only
print(datetime.date.today().year) #print year only

x = datetime.datetime(year=2024,month=12,day=25)
y = datetime.datetime(year=2024,month=11,day=8)

dif = x-y #to find the difference of 2 time

print(dif)

end=datetime.datetime.now()

difference=end-now

print(difference)

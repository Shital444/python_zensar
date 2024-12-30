import calendar as cal
print("......calender program in python.....");
print("Enter 'X' for exit.");
y=input("Enter year:");
if y=='X':
    exit();
else:
    mm=int(input("Enter month:"));
    yy=int(mm);
    print("\n",cal.month(yy,mm))
cal= cal.TextCalendar()
for month in range(1, 13):
    year=int(input("Enter year:"));
    print(cal.formatmonth(year,month))
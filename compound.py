Max = 10
Min = 0
y = 15

if y > Max:
    print("Your value", y ,"is more than the Max", Max)
if y < Min:
    print("Your value", y ,"is less than the Min", Min)

x = 10

if Min < x < Max:
   print("Your value", x ,"is between the Min", Min, "and the Max", Max)
if Min <= x < Max:
   print("Your value", x ,"is more than or equal to Min", Min, "and less than Max", Max)
if Min < x <= Max:
   print("Your value", x ,"is between the Min", Min, "and equal to or less than Max", Max)
num = int(input("enter a number:"))
if num%4==0:
   if num%100==0:

      if num%400==0:
         print("leap year")
      else:
         print("not a leap year")
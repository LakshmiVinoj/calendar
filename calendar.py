import math
import datetime

date_dict={"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,
           "november":11,"december":12}
days_in_a_month=[31,28,31,30,31,30,31,31,30,31,30,31]
week=["sun","mon","tue","wed","thur","fri","sat"]

def is_leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
        else:
            return True
    else:
        return False
    
def calendar():
    while(1):
        month=input("Enter month: ")
        year=int(input("Enter year: "))
        if month not in date_dict:
            print("enter a month from jan to dec")
        elif year<1 or year>9999:
            print("enter a year between 1 and 9999")  
        else:
            break
    
    if is_leap(year):
        days_in_a_month[1]+=1   
    
    first_day_of_year=datetime.date(year,date_dict[month],1)
    start_day=first_day_of_year.isoweekday()
   
    print("+"+"-"*41+"+")
    
    total = len(month)+len(str(year))+1
    if total%2==0:
        print("|"+" "*int((41-total)/2)+month+" "+str(year)+" "*(int((41-total)/2)+1)+"|")
    else:
        print("|"+" "*int((41-total)/2)+month+" "+str(year)+" "*int((41-total)/2)+"|")        
        
    print("+"+"-"*41+"+"+"\n"+"| sun | mon | tue | wed | thu | fri | sat |"+"\n"+"+"+"-"*41+"+")

    braker=1
    for i in range (1,days_in_a_month[date_dict[month]-1]+1):
        if braker==1:
            if start_day==7:
                print("| {0:<3}".format(i),end=' ')
                start_day=1
                braker=0   
            elif start_day==6:
                print("|"+" "*((6*start_day)-1)+"| {0:<3}".format(i),end=' ')
                print("|\n"+"+"+"-"*41+"+")
                start_day+=1
                braker=0                  
            else:
                print("|"+" "*((6*start_day)-1)+"| {0:<3}".format(i),end=' ')
                start_day+=1
                braker=0         
        elif i==days_in_a_month[date_dict[month]-1] and start_day!=6:
            print("| {0:<3}".format(i),end=' |'+" "*(41-(6*(start_day+1)))+"|")
            print("\n+"+"-"*41+"+")   
        elif start_day==7:
            print("| {0:<3}".format(i),end=' ')
            start_day = 1            
        elif start_day!=6:
            print("| {0:<3}".format(i),end=' ')
            start_day+=1    
        else:
            print("| {0:<3}".format(i),end=' ')
            print("|\n"+"+"+"-"*41+"+")
            start_day = 0
            
    b=1
    while(b==1):
        rep=int(input("do you want to repeat? "))
        if rep == 0:
            b=0
        else:
            calendar()
        
calendar()
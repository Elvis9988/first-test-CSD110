# taking date inputs from the user

def inputfunction():
    day = int(input("Enter the day (eg: 12 or 04 or 24): "))
    month = int(input("Enter the month (eg: 12 for December, 4 for April): "))
    year = int(input("Enter the year (eg: 22 for 2022, 02 for 2002): "))
    return day, month, year

def problemsolving(day, month, year):
    if day <= 0 or month <= 0 or year <= 0:
        print ("Invalid input")
    else: 
        if day > 31:
            print ("Invalid day input")
    
        if month > 12:
            print ("Invalid month input")
        if year > 99:
            print ("Invalid year input")
        
        if month == 4 or month == 6 or month == 9 or month == 11:
            if day > 30:
                print ("Invalid day input") 
    
        if month == 1 or month == 2 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day > 31:
                print ("Invalid day input")


        if month == 2:
            if (year % 4) == 0:
                if day > 29:
                    print ("Invalid day input")
                else:
                    print ("Sucess: Congratulations! You entered a correct date.")
    
        else:
            print ("Sucess: Congratulations! You entered a correct date.")
    
    
# calling functions
day, month, year = inputfunction()
problemsolving(day, month, year)


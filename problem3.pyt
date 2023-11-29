# taking user input 
salary = int(input("Please enter your salary in Germany in Euros: "))
migrate = input("Enter the country you wish to migrate to: ")

# assigning average salaries with respect to the data provided 
CAD = 56000
USA = 45000
CAM = 7649856
UK = 45423

if migrate == "Canada" or migrate == "USA" or migrate == "Cambodia" or migrate == "United Kingdom":
    
    def migratecountry(salary, migrate):
        
        if migrate == "Canada":
            salary = salary * 1.49
        elif migrate == "USA":
            salary = salary * 1.10
        elif migrate == "Cambodia":
            salary = salary * 4525.06
        elif migrate == "United Kingdom":
            salary = salary * 0.86
        return salary, migrate
            
    def comparesalary(migrate, salary, CAD, USA, CAM, UK):
        if migrate == "Canada":
            if salary > CAD:
                print ("You will be rich in Canada with a salary of", salary, "Canadian Dollars")
            else:
                print ("You will be poor in Canada with a salary of", salary, "Canadian Dollars")
        elif migrate == "USA":
            if salary > USA:
                print ("You will be rich in USA with a salary of", salary, "US Dollars")
            else:
                print ("You will be poor in USA with a salary of", salary, "US Dollars")
        elif migrate == "Cambodia":
            if salary > CAM:
                print ("You will be rich in Cambodia with a salary of", salary, "Cambodian Riel")
            else:
                print ("You will be poor in Cambodia with a salary of", salary, "Cambodian Riel")
        elif migrate == "United Kingdom":
            if salary > UK:
                print ("You will be rich in United Kingdom with a salary of", salary, "Pound Sterling")
            else:
                print ("You will be poor in United Kingdom with a salary of", salary, "Pound Sterling")
                
    salary, migrate = migratecountry(salary, migrate)
    comparesalary(migrate, salary, CAD, USA, CAM, UK)
        

else:
    print("Invalid migrate country")
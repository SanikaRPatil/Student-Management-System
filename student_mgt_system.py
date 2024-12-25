details={1:{"name":"sanika","city":"kolhapur","passing year":2024,"percentage":84,"course":"python"},
         2:{"name":"Aarti","city":"latur","passing year":2023,"percentage":60,"course":"java"},
         3:{"name":"sanika","city":"latur","passing year":2023,"percentage":70,"course":"python"}}
print("-"*128)
print(f"{" "*45} The Kiran Academy")
print("-"*128)
while True:
    print("""
                                                DashBoard
                                            1. Add Student data
                                            2. Display Student Data
                                            3. Updata Student Data
                                            4. Delete Student Data
                                            5. Filtering
            """) 
    ch=int(input("Enter your Choice: "))
    #1. Add Student data
    if ch==1:
        rg_no=int(input("Enter registration number: "))
        name=input("Enter Name: ")
        city=input("Enter city: ")
        year=int(input("Enter Passing Year: "))
        per=eval(input("Enter Percentage: "))
        course=input("Enter Course: ")
        
        details[rg_no]={"name":name,"city":city,"passing year":year,"percentage":per,"course":course}    
        print(f"{" "*30}Registration Successfully...!")
    elif ch==2:
        #2. Display Student Data
        print(f"{" "*45}Students Details")
        print("-"*128)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("Rg_Number","Name","City","Passing Year","Percentage","Course Name"))
        print("-"*128)
        for i in details:
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,details[i]["name"],details[i]["city"],details[i]["passing year"],details[i]["percentage"],details[i]["course"]))
            print("-"*128)
    elif ch==3:
        #3. Updata Student Data
        print("""
                                    Update Data 
                                1. Name
                                2. City
                                3. Passing Year
                                4. Percentage
                                5. Course
                """)
        ch=int(input("Enter Which data you ant to updated: "))
        if ch==1:
            r_no=int(input("Enter which rg number of name is updated: "))
            uname=input("Enter Name: ")
            details[r_no]["name"]=uname
            print(f"{" "*35}Name is updated Successfully..!")
        elif ch==2:
            r_no=int(input("Enter which rg number of city is updated: "))
            ucity=input("Enter City: ")
            details[r_no]["city"]=ucity
            print(f"{" "*35}City is updated Successfully..!")
        elif ch==3:
            r_no=int(input("Enter which rg number of Passing year is updated: "))
            uyear=int(input("Enter year: "))
            details[r_no]["passing year"]=uyear
            print(f"{" "*35}Passing Year is updated Successfully..!")
        elif ch==4:
            r_no=int(input("Enter which rg number percentage is updated: "))
            uper=input("Enter Percentage: ")
            details[r_no]["percentage"]=uper
            print(f"{" "*35}Percentage is updated Successfully..!")
        elif ch==5:
            r_no=int(input("Enter which rg number name is updated: "))
            ucourse=input("Enter Course: ")
            details[r_no]["course"]=ucourse
            print(f"{" "*35}Course is updated Successfully..!")
        else:
            print(f"{" "*40}Invalid Choise...!")
    elif ch==4:
        #4. Delete Student Data
        ch=int(input("Enter which data you want to delete: "))
        del details[ch]
        print("Delete Successfully...!")
    elif ch==5:
            print("""
                    Which Data is Serach
                1. Name
                2. City
                3. Passing Year
                4. Percentage
                5. Course
                """)
            
            ch=int(input("Enter Your Choice: "))
            if ch==1:
                name=input("Enter Name: ")
                print("-"*65)
                print("|{:^30}|{:^30}|".format("Rg number","Name"))
                print("-"*65)
                for nm in details:
                    if details[nm]["name"]==name:
                        print("|{:^30}|{:^30}|".format(nm,details[nm]["name"]))
                        print("-"*65)
                    
            elif ch==2:
                city=input("Enter city: ")
                print("-"*42)
                print("{:^20}|{:^20}|".format("Rg number","City"))
                print("-"*42)
                for c in details:
                    if details[c]["city"]==city:
                        print("{:^20}|{:^20}|".format(c,details[c]["city"]))
                        print("-"*42)
            elif ch==3:
                year=int(input("Enter Year: "))
                print("-"*82)
                print("|{:^40}|{:^40}|".format("Rg_Number","Passing Year"))
                print("-"*82)
                for pyear in details:
                    if details[pyear]["passing year"]==year:
                        print("|{:^40}{:^40}|".format(pyear,details[pyear]["passing year"]))
                        print("-"*82)
            elif ch==4:
                ptg=eval(input("Enter Percentage: "))
                print("-"*63)
                print("|{:^30}|{:^30}|".format("Rg number","Percentage"))
                print("-"*63)
                for per in details:
                    if details[per]["percentage"]==ptg:
                        print("|{:^30}|{:^30}|".format(per,details[per]["percentage"]))
                        print("-"*63)
            elif ch==5:
                cour=input("Enter ocurse: ")
                print("-"*62)
                print("|{:^30}|{:^30}|".format("Rg number","Course"))
                print("-"*62)
                for co in details:
                    if details[co]["course"]==cour:
                        print("|{:^30}|{:^30}|".format(co,details[co]["course"]))
                        print("-"*62)
            else:
                print("Invalid Input")
    
    c=input("Do you want to continue: ")
    if c=="n":
        print(f"{" "*40}Thanks you....!")
        break
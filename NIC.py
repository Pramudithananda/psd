import datetime
#Old NIC number to birthday calc
def sl_id_to_dob_gender(id_num):
    if len(id_num) == 10:
        year = int(id_num[0:2])
        days = int(id_num[2:5])
        if days > 500:
            year += 1900
            days -= 500
            gender = "Female"
        else:
            year += 1900
            gender = "Male"
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                 dob = datetime.date(year, 1, 1) + datetime.timedelta(days=days-1)
            else:
                  dob = datetime.date(year, 1, 1) + datetime.timedelta(days=days-2)
                        
        return dob.strftime("%Y-%m-%d"), gender
 # New NIC number to birthday calc
    elif len(id_num) == 12:
        year = int(id_num[0:4])
        days = int(id_num[4:7])
        if days > 500:
            days -= 500
            gender = "Female"
        else:
            gender = "Male"
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                dob = datetime.date(year, 1, 1) + datetime.timedelta(days=days-1)
            else:
                dob = datetime.date(year, 1, 1) + datetime.timedelta(days=days-2)
                
        return dob.strftime("%Y-%m-%d"), gender
    else:
        return "Invalid ID number", None

id_num = input("Enter your Sri Lankan Old or New ID card number: ")
dob, gender = sl_id_to_dob_gender(id_num)

if dob == "Invalid ID number":
    print(dob)
else:
    print("Your date of birth is:", dob)
    print("Your gender is:", gender)

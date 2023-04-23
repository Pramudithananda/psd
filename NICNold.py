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
            if not (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
                if days >= 60:
                    dob = datetime.date(year, 1, 1) + datetime.timedelta(days=days-2) 
                elif days<60:
                     dob = datetime.date(year, 1, 1) + datetime.timedelta(days=days-1) 
            else:
              dob = datetime.date(year, 1, 1) + datetime.timedelta(days=days-1) 
        else:
            year += 1900
            gender = "Male"
            if not (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
                if days >= 60:
                    dob = datetime.date(year, 1, 1) + datetime.timedelta(days=days-2) 
                elif days<60:
                     dob = datetime.date(year, 1, 1) + datetime.timedelta(days=days-1) 
            else:
              dob = datetime.date(year, 1, 1) + datetime.timedelta(days=days-1) 
                    
        return dob.strftime("%Y-%m-%d, %A"), gender
 # New NIC number to birthday calc
    elif len(id_num) == 12:
        year = int(id_num[0:4])
        days = int(id_num[4:7])
        if days > 500:
            days -= 500
            gender = "Female"
            if not (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
                if days >= 60:
                    dob = datetime.date(year, 1, 1) + datetime.timedelta(days=days-2) 
                elif days<60:
                     dob = datetime.date(year, 1, 1) + datetime.timedelta(days=days-1) 
            else:
              dob = datetime.date(year, 1, 1) + datetime.timedelta(days=days-1) 
        else:
            gender = "Male"
            if not (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
                if days >= 60:
                    dob = datetime.date(year, 1, 1) + datetime.timedelta(days=days-2) 
                elif days<60:
                     dob = datetime.date(year, 1, 1) + datetime.timedelta(days=days-1) 
            else:
              dob = datetime.date(year, 1, 1) + datetime.timedelta(days=days-1)  
        return dob.strftime("%Y-%m-%d, %A"), gender
    else:
        return "Invalid ID number", None

id_num = input("Enter your Sri Lanka Old or New ID card number: ")
dob, gender = sl_id_to_dob_gender(id_num)

 #New NIC to Old NIC _______
def old_nic_1(nic:str) ->int:
    part_one = nic[2:7]
    return int(part_one) 
def old_nic_2(nic:str) ->int:
    part_two = nic[7:12]
    return int(part_two)  

 #Old NIC to New NIC _________
def new_nic1(nic:str)->int:
    part_two = 19
    return int(part_two)
def new_nic2(nic:str)->int:
    part_five = nic[:5]
    return int(part_five)  
def new_nic3(nic:str)->int:
    part_fore = 0
    return int(part_fore)   
def new_nic4(nic:str):
    part_six = nic[5:9]
    return (part_six)  
    
 #print resault__________
if dob == "Invalid ID number":
    print(dob)
else:
    print("_____________________________________________")
    print("\nYour date of birth is:", dob)
    print("\nYour gender is:", gender)
    if len(id_num) == 12:
        if int(id_num[0:4]) < 2000:
            print(  f"\nYour Old Nic :{old_nic_1(id_num)}{old_nic_2(id_num)}V")
        else:
            print("\nYour Old Nic : you don't have old one")
    else:
       print(f"\nYour New Nic : {new_nic1(id_num)}{new_nic2(id_num)}{new_nic3(id_num)}{new_nic4(id_num)}")

    print("_____________________________________________")

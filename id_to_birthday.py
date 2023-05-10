import datetime

#New NIC to Old NIC _______
def old_nic_1(nic:str) ->int:
    part_one = nic[2:7]
    return int(part_one) 

def old_nic_2(nic:str) ->int:
    part_two = nic[7:12]
    return int(part_two)  

 #Old NIC to New NIC _________
def new_nic1(nic:str)->int:
    part_one = 19
    return int(part_one)
def new_nic2(nic:str)->int:
    part_two = nic[:5]
    return int(part_two)  
def new_nic3(nic:str)->int:
    part_three = 0
    return int(part_three)   
def new_nic4(nic:str):
    part_fore = nic[5:9]
    return (part_fore)  
    
while True:
    id_num = input("Enter your Sri Lankan ID card number: ")

    if len(id_num) == 12 and id_num.isdigit:
        # New format - first 4 digits are birth year, next 3 are number of days from Jan 1
        birth_year = int(id_num[0:4])
        num_of_days = int(id_num[4:7])
    elif len(id_num) == 10 and id_num[0:9].isdigit and (id_num[-1] == 'v' or id_num[-1] == 'V'):
        # Old format - first 2 digits are birth year, next 3 are number of days from Jan 1
        birth_year = 1900 + int(id_num[0:2]) if int(id_num[0:2]) >= 0 and int(id_num[0:2]) >= 21 else 2000 + int(id_num[0:2])
        num_of_days = int(id_num[2:5])
    else:
        print("Invalid number check the number try again")
        continue

    # Determine gender based on number of days
    if 0 <= num_of_days <= 367:
        gender = 'male'
        if not (birth_year % 4 == 0 and (birth_year % 100 != 0 or birth_year % 400 == 0)):
            if num_of_days > 60:
                num_of_days -= 1
    elif 500 <= num_of_days <= 867:
        gender = 'female'
        num_of_days -= 500
        if not (birth_year % 4 == 0 and (birth_year % 100 != 0 or birth_year % 400 == 0)):
            if num_of_days > 60:
                num_of_days -= 1
    else:
        print("Invalid number check the number try again")
        continue

    # Calculate date of birth from birth year and number of days
    birth_date = datetime.date(birth_year, 1, 1) + datetime.timedelta(num_of_days - 1)

    # Print the date of birth and gender
    print("-" * 120)
    print("Your date of birth is:", birth_date.strftime("%d/%m/%Y\n"))
    print("Your born day is:", birth_date.strftime("%A\n"))
    print("Your gender is:", gender,"\n")
    if len(id_num) == 12:
        if int(id_num[0:4]) < 2000:
            print(  f"\nYour Old Nic :{old_nic_1(id_num)}{old_nic_2(id_num)}V")
        else:
            print("\nYour Old Nic : you don't have old one")
    else:
       print(f"\nYour New Nic : {new_nic1(id_num)}{new_nic2(id_num)}{new_nic3(id_num)}{new_nic4(id_num)}")

    print("-" * 120)
    break
# output
'''
Enter your Sri Lankan ID card number: 199978804387
------------------------------------------------------------------------------------------------------------------
Your date of birth is: 14/10/1999

Your born day is: Thursday

Your gender is: female


Your Old Nic :997884387V
------------------------------------------------------------------------------------------------------------------
Enter your Sri Lankan ID card number: 997884387V
------------------------------------------------------------------------------------------------------------------Your date of birth is: 14/10/1999

Your born day is: Thursday

Your gender is: female


Your New Nic : 199978804387
------------------------------------------------------------------------------------------------------------------Enter your Sri Lankan ID card number: 200034804562
------------------------------------------------------------------------------------------------------------------Your date of birth is: 13/12/2000

Your born day is: Wednesday

Your gender is: male


Your Old Nic : you don't have old one
------------------------------------------------------------------------------------------------------------------

'''
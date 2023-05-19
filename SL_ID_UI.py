import datetime
import tkinter as tk
from tkinter import messagebox

# Functions for NIC conversion
def old_nic_1(nic: str) -> int:
    part_one = nic[2:7]
    return int(part_one)

def old_nic_2(nic: str) -> int:
    part_two = nic[7:12]
    return int(part_two)

def new_nic1(nic: str) -> int:
    part_one = 19
    return int(part_one)

def new_nic2(nic: str) -> int:
    part_two = nic[:5]
    return int(part_two)

def new_nic3(nic: str) -> int:
    part_three = 0
    return int(part_three)

def new_nic4(nic: str) -> str:
    part_fore = nic[5:9]
    return part_fore


def get_nic_info():
    id_num = nic_entry.get()

    if len(id_num) == 12 and id_num.isdigit:
        birth_year = int(id_num[0:4])
        num_of_days = int(id_num[4:7])
    elif len(id_num) == 10 and id_num[0:9].isdigit and (id_num[-1] == 'v' or id_num[-1] == 'V')and int(id_num[:2]) >= 30:
        birth_year = 1900 + int(id_num[0:2]) if int(id_num[0:2]) >= 0 and int(id_num[0:2]) >= 21 else 2000 + int(id_num[0:2])
        num_of_days = int(id_num[2:5])
    else:
        messagebox.showerror("Invalid Number", "Invalid number. Please check the number and try again.")
        return

    if 0 <= num_of_days <= 366:
        gender = 'male'
        if not (birth_year % 4 == 0 and (birth_year % 100 != 0 or birth_year % 400 == 0)):
            if num_of_days > 60:
                num_of_days -= 1
    elif 500 <= num_of_days <= 866:
        gender = 'female'
        num_of_days -= 500
        if not (birth_year % 4 == 0 and (birth_year % 100 != 0 or birth_year % 400 == 0)):
            if num_of_days > 60:
                num_of_days -= 1
    else:
        messagebox.showerror("Invalid Number", "Invalid number. Please check the number and try again.")
        return

    birth_date = datetime.date(birth_year, 1, 1) + datetime.timedelta(num_of_days - 1)
    result = f"Your date of birth is: {birth_date.strftime('%d/%b/%Y')}\n"
    result += f"Your born day is: {birth_date.strftime('%A')}\n"
    result += f"Your gender is: {gender}\n"

    if len(id_num) == 12:
        if int(id_num[0:4]) < 2000:
            result += f"Your Old NIC: {old_nic_1(id_num)}{old_nic_2(id_num)}V"
        else:
            result += "Your Old NIC: You don't have an old one"
    else:
        result += f"Your New NIC: {new_nic1(id_num)}{new_nic2(id_num)}{new_nic3(id_num)}{new_nic4(id_num)}"

    messagebox.showinfo("NIC Information", result)


# Create the GUI
root = tk.Tk()
root.title("NIC Information")
root.geometry("400x200")

# Create NIC input label and entry
nic_label = tk.Label(root, text="Enter your Sri Lankan ID card number:", padx=50)
nic_label.pack(anchor="center", padx=100, pady=100)


nic_entry = tk.Entry(root, justify= "center")
nic_entry.pack(anchor="center")


# Create submit button
submit_button = tk.Button(root, text="Submit", command=get_nic_info)
submit_button.pack(anchor="center", padx=400, pady=100)

root.mainloop()

# temperature unit converter

def convert_temperature(temp, unit_from, unit_to):
    conversion_factors = {
        "C": {
            "F": lambda x: (x * 9/5) + 32,
            "K": lambda x: x + 273.15
        },
        "F": {
            "C": lambda x: (x - 32) * 5/9,
            "K": lambda x: (x + 459.67) * 5/9
        },
        "K": {
            "C": lambda x: x - 273.15,
            "F": lambda x: (x * 9/5) - 459.67
        }
    }
    try:
        conversion_func = conversion_factors[unit_from][unit_to]
    except KeyError:
        return None
    return conversion_func(temp)

# prompt user for input
temp = float(input("Enter the temperature to convert: "))
unit_from = input("Enter the unit to convert from (C/F/K): ")
unit_to = input("Enter the unit to convert to (C/F/K): ")

# convert units and print result
result = convert_temperature(temp, unit_from, unit_to)
if result is None:
    print("Invalid input.")
else:
    print(f"{temp} {unit_from} is equal to {result} {unit_to}")

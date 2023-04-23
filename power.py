def power(base, exponent):
    """
    This function calculates the power of a given number using recursion.

    Parameters:
    base (int or float): The base number.
    exponent (int): The exponent.

    Returns:
    int or float: The result of base raised to the exponent.
    """
 
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * power(base, exponent - 1)
base = int(input("Enter base of power : "))
exponent =int(input("Enter exponent of power : "))
superscript = str(exponent).translate(str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))
result = power(base, exponent)
print(f"You entered {base}{superscript} result is : ", result)  # Output: 8

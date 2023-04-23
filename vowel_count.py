def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
s = input("Enter word prase for count vowels : ")
num_vowels = count_vowels(s)
print("The number of vowels in the string is:", num_vowels)

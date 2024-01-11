#The program created need to give different outcomes dependind on the user data entries.

age = int(input("\nHow old are you? "))

#If the user is 40 or over:
if age >= 40 and age < 65: #I added <=65 to dont confuse the code below.
    print("\nYou're over the hill.")

#if the user is more than 100:
elif age > 100: 
    print("\nSorry, you're dead.")

#If the user is over 65:
elif age >= 65 and age <= 100: #also added to dont confuse the code above.
    print("\nEnjoy your retirement!")

#If the user is under 13:
elif age < 13:
    print("\nYou qualify for the kiddie discount.")

#If the user is 21:
elif age == 21:
    print("\nCongrats on your 21st!")

#Any other age:
else:
    print("\nAge is but a number.")

print("\nThank you!")
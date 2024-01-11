#ask the user to enter 3 different integers

num1 = int(input("\nPlease enter a number: "))
num2 = int(input("\nPlease enter another number: "))
num3 = int(input("\nPlease enter a last number: "))

#I didn't know how to make the numbers to be different from each other, my guess is that I could use "if" for that:
#likewise:
#if num1=num2 or num2=num3 or num1=num3
#print ("Please enter a different number")
#and how to make the digit stops after the user enters the number, or how to automatically ask for the next number after the user enters the first.

print("\nThe number entered is: {}{}{}".format(num1, num2, num3))

#the sum of all numbers:

sum = int(num1 + num2 + num3)

print("\nThe sum of all numbers is: {}".format(sum))

#The first number minus the second number:

first_minus_sec = int(num1 - num2)

print("\nThe first number minus the second one is: {}".format(first_minus_sec))

#The third number multiplied by the first number:

third_mult_one = int(num3 * num1)

print ("\nThe third number multiplied by the first number is: {}".format(third_mult_one))

#The sum of all numbers divided by the third:

sum_all_div_third = float((num1 + num2 + num3) / num3)

#or

sum_all_div_third = float (sum / num3)

print("\nThe sum of all numbers divided by the third number is: {} ".format(sum_all_div_third))

print("\n Thank you!\n")
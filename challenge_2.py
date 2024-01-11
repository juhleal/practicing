#take the name of a user's favourite restaurant
#store at string_fav

string_fav = input("\nWhat's the name of your favourite restaurant?: ")

#trying casting string_fav into an integer using the code below:

'''string_fav = int(input("\nWhat's the name of your favourite restaurant?: "))'''

#output: Error: invalid literal for int() - Well, it's not a number.

#take user's favourite number

int_fav = int(input("\nTell me your favourite number: "))

#printing two diferent statements using the format model

print("\nThe user's favourite restaurant is: {}".format(string_fav))

print("\nThe user's favourite number is: {}".format(int_fav))

#printing one statement using both entries

print("\nThe user's favourite restaurant is {}, and their favourite number is {}".format(string_fav, int_fav))

print("\nThank you!\n")
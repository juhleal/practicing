#Prompt a user to write a sentence
#Save user's response in a variable called "str_manip"

str_manip = input("\nWrite the chorus of your favourite song: ")

#calculate and display the total sentence lenght:

lenght_str_manip = len(str_manip) 
print(f"\nLenth of the str_manip: {lenght_str_manip}")

#finding the last letter of "str_manip" and replacing all occurences for "@" and displaying:

last_letter = str_manip[-1] 
str_manip_replaced = str_manip.replace(last_letter, "@")

print(f"\nThe new str_manip: {str_manip_replaced}")

#findind the last three characters backwards and displaying:

last_three_char = str_manip[-3: ][ : :-1] 
print(f"\nLast three characters backwards: {last_three_char}")

#create a five-letter word made with the first three and last two characters in strip_manip:

five_letter_word = str_manip[ :3] + str_manip[-2: ]
print(f"\nFive letters word: {five_letter_word}")

print("\nThank you!\n")

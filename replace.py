#Save the sentence "The!quick!brown!fox!jumps!over!the!lazy!dog." in a single string.

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

#Reprint the sentence above replacing all "!" for a blank space:

replaced_sentence = sentence.replace("!"," ")

print("") #How do I replace this blank space when I'm printing without """"?

print(replaced_sentence)

print("")

#Reprint the sentence in upper case:

upper_sentence = replaced_sentence.upper() 

print(upper_sentence)

print("")

#Print the sentence in reverse:

reversed_sentence = upper_sentence[ : :-1] 
print(reversed_sentence) 

print("\nThank you!\n")
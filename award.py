#Running a program that determines the award a person competing in a triathlon will receive.

#Reading in time (minutes) each different category:

swimming = float(input("\nWrite the total time (in minutes) on swimming: "))

print("\nThe total swimming time was {} minutes".format(swimming))

cycling = float(input("\nWrite the total time (in minutes) on cycling: "))

print("\nThe total cycling time was {} minutes".format(cycling))

running = float(input("\nWrite the total time (in minutes) on running: "))

print("\nThe total running time was {} minutes".format(running))

#creating one variable for triathlon and calculating the total time:

triathlon = (swimming + cycling + running)

#determining each award to the respective final time:
    
if triathlon <= 100:
    print("\nThe total triathlon time was: {}. You have won Provincial Colours. Congratulations!".format(triathlon))

elif triathlon > 100 and triathlon <= 105:
    print("\nThe total triathlon time was: {}. You have won Half Provincial Colours. Congrats!".format(triathlon))

elif triathlon > 105 and triathlon <= 110:
    print("\nThe total triathlon time was: {}. You have won Provincial Scroll. Congs..".format(triathlon))

elif triathlon > 110:
    print("\nThe total triathlon time was: {}. You have won nothing. Con!".format(triathlon))

print("\nThank you!")
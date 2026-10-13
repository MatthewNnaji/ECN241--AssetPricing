'The TRY/EXCEPT sequence is used for catching errors; if at any point in try except is triggered; the code will skip over to the except section'
while True:    # default value is true; so this loop will go on forever
    try: #do this line - however naturally errors will come
        time = int(input("Enter maturity length："))
        break  #if this line is reached it hard cuts any loop; even a while loop which can in theory can go on forever
    except ValueError:
        print("Please enter a whole number.")
print('Escaped the loop')


"""
1) infinite while loop
2) within the while loop, 'try' (go ahead with the code as normal) EXCEPT something (an error that shutsdown running) occurs
3) If this error occurs instead of the code shutting down the input/calclation will not be saved or carried out; and the code will stop running try and skip to except
4) Since it skipped to except; the loop continues and so the try section is ran again (if it continued going down try the loop would break)
5) Slightly different way of doing loops that avoids having to convert to string and back
"""


time2=input("Enter maturity length：")
while isinstance(time2, int) == False and not time2.isdigit():
    time2=input("Incorrect. enter valid number")
    if time2.isdigit(): #checks if strings are digits / "numerical" - aka if they could successfully be converted to an integer; int()
        break
    
time2=int(time2)

print("never entered the loop / escaped it")

'Can also use pass in loops to skip lines; bear in mind '
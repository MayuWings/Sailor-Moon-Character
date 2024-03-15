print ("Which Sailor Moon character are you?")
print ("Answer the questions to find out!")

amCrybaby = input ("Do you cry a lot?\n")
if amCrybaby == "yes":
    print ("You are Sailor Moon!")
    exit(0)
if amCrybaby == "no":
    print("Guess you're not Sailor Moon then")
    
amSmart = input ("Are you like super smart?\n")
if amSmart == "yes":
    print ("You are Sailor Mercury!")
    exit(0)
if amSmart == "no":
    print("welp, not Sailor Mercury either")

amStrong = input ("Are you  super strong?\n")
if amStrong == "yes":
    print ("You are Sailor Jupiter!")
    exit(0)
if amStrong == "no":
    print("not Sailor Jupiter either")

amCool = input ("Are you pretty cool?\n")
if amCool == "yes":
    print ("You are Sailor Mars!")
    exit(0)
if amCool == "no":
    print("okay so you aren't Sailor Mars either then")

amPretty = input ("Are you super pretty?\n")
if amPretty == "yes":
    print ("You are Sailor Venus!")
    exit(0)
else:
    print ("aww, guess you aren't like any of the Sailor Scouts then")
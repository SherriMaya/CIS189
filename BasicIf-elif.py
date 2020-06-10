subscribe = input("Do you want to subscribe to Programmer's Toolkit Monthly Subscription Box?")

if subscribe == "No":
    print("Okay, maybe next time you visit.")
elif subscribe == "Yes":
    print("Levels of Membership:")
    print("Platinum ($60.00)")
    print("Gold ($50.00)")
    print("Silver ($40.00)")
    print("Bronze ($30.00)")
    print("Free (Free)")
    level = input("What level membership you wouuld like?")
    if level == "Platinum":
        print("Your cost will be $60.00")
    elif level == "Gold":
        print("Your cost will be $50.00")
    elif level == "Silver":
        print("Your cost will be $40.00")
    elif level == "Bronze":
        print("Your cost will be $30.00")
    elif level == "Free":
        print("Your cost will be $0.00")
    else:
        print("Sorry, I didn't understand your response")
else:
    print("Sorry, I didn't understand your response")
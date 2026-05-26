MEMBER_STATUS = "GOLD"
passenger_row = int (input("Enter your seat row:"))
has_ticket = input("Do you have a valid ticket? (yes/no):")
if has_ticket.lower() == "yes":
    print("Access Granted. Have a fun trip.")
if passenger_row <= 8 and MEMBER_STATUS == "GOLD":
    print("Welcome to priority boarding! Please make your way on board now.")
elif passenger_row <= 8 or MEMBER_STATUS == "GOLD":
    print("Welcome to priority boarding! Please wait for our Gold Business Flyers to finish boarding.")
else:
    print("Please wait for general boarding.")
destination = input("Enter your destination code: ")
if destination == "AKL" or destination == "WLG":
    print("Flight is delayed 5 minutes.")
elif not destination is "CHC":
    print ("Flight is on time.")
else:
    print ("Flight has been cancelled")
banned_items = ["slingshot","laser"]
inventory = ["apple","slingshot","book","laser"]
confiscated = []
print(f"Scanning inventory: {inventory}")
for item in inventory:
    if item in banned_items:
        print(f"Alert! Found banned item: Slingshot, Laser")
        confiscated.append(item)
        inventory.pop(1 and 3)
print(f"Scan complete. Total flag matches: {len(banned_items)}")
if len(confiscated) > 0:
    print(f"Items confiscated:")
    for item in confiscated:
        print ("1. Slingshot\n2. Laser")
else:
    print("No items confiscated\nHave a great day")

        
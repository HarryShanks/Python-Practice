import random
MAX_ATTEMPTS = 3
attempts = 0
system_status = "OFFLINE"
while attempts < MAX_ATTEMPTS and system_status == "OFFLINE":
    boot_code = input("Enter boot code (START): ").upper().strip()
if boot_code == "START":
    print("System booting...")
    system_status = "ONLINE"
else:
    print("Invalid boot code.")
rand_num = random.randintint(1,10)
if rand_num == 5:
    print("Something went wrong")
else:
    print("System online.")

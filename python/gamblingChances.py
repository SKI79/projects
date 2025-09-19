
import random
import datetime

# Initialize count for tracking attempts
count = 0

# Prompt user for win percentage
print("What percentage do you have to win?")
beforePercent = input("")

# Validate and convert percentage input
try:
    beforePercentInt = float(beforePercent)
except:
    print("Number was not a valid percentage. Exiting...")
    exit()

# Check if percentage is within valid range
if beforePercentInt > 100.0:
    print("Number too high. Exiting...")
    exit()

# Prompt user for cost per attempt
print('How much does it cost?')
moneyCost = input("")
try:
    moneyCostInt = float(moneyCost)
except:
    print('Invalid response. Exiting...')
    exit()

# Calculate probability and odds
afterPercent = beforePercentInt / 100
chances = 1 / afterPercent

# Ask user for simulation mode
option = input("Brute force (run until success) or run set amount of times? (brute/set):")
# Ask user if they want to count attempts (required for cost calculation)
countOption = input("Count how many tries it took? (required for cost calculation) (y/n):")

# Display calculated odds
print(f"Chances: 1 in {chances}")

if option == "brute":
    # Brute force mode: run until success
    while True:
        startDate = datetime.datetime.now()
        # Generate random number to simulate chance
        randomNumber = random.randint(1,int(chances))
        if countOption == "y":
            count = count + 1
        # Check if success is achieved
        if randomNumber == 1:
            endDate = datetime.datetime.now()
            diff = endDate - startDate
            if countOption == "y":
                print(f"Took {count} tries.")
                print(f"Costs {count * moneyCostInt} for {count} tries.")
            print(f"Success! Processing took {diff.total_seconds()} seconds. Press enter to continue.")
            input("")
            exit()
elif option == "set":
    # Set mode: run a fixed number of times
    print("How many times to run?")
    times = input("")
    try:
        timesInt = int(times)
    except:
        print("Invalid response. Exiting...")
        exit()
    startDate = datetime.datetime.now()
    for i in range(timesInt):
        # Generate random number to simulate chance
        randomNumber = random.randint(1,chances)
        if countOption == "y":
            count = count + 1
        # Check if success is achieved
        if randomNumber == 1:
            endDate = datetime.datetime.now()
            diff = endDate - startDate
            if countOption == "y":
                print(f"Took {count} tries.")
            print(f"Success! Processing took {diff.total_seconds()} seconds. Press enter to exit.")
            input("")
            exit()
    # If success not achieved after all runs
    print("Number not found. Press enter to exit.")
    input("")
    exit()
    pass
else:
    # Handle invalid option
    print("Invalid option selected. Exiting...")
    exit()

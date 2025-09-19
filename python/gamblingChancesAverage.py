
import random
import datetime

# Initialize count for tracking attempts
count = 0

# Prompt user for win percentage
print("What percentage do you have to win? (some percentages are more accurate than others. This tool is purely for fun.)")
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

# Option to count attempts per success
countOption = "y"

# Ask user if they want to see total attempts after each success
print("Show the total amount of times the program has run after each success? Turning this off improves performance slightly. (y/n)")
showPrints = input("")
if showPrints != "y" and showPrints != "n":
    print("Invalid response. Exiting...")
    exit()

# Ask user for number of simulation runs
print("How many times should the program run? Higher numbers for better results:")
runCount = input("")
try:
    runCountInt = int(runCount)
except:
    print("Invalid response. Exiting...")
    exit()

# Display calculated odds
print(f"Chances: 1 in {chances}")
print("Processing...")

# Initialize accumulators for averages
countAverages = 0
costAverages = 0
totalRuns = 0

# Record start time
startDate = datetime.datetime.now()

# Run simulation for specified number of times
for i in range(runCountInt):
    while True:
        # Generate random number to simulate chance
        randomNumber = random.randint(1,int(chances))
        if countOption == "y":
            count = count + 1
        # Check if success is achieved
        if randomNumber == 1:
            endDate = datetime.datetime.now()
            diff = endDate - startDate
            if countOption == "y":
                # Update averages and counters
                countAverages = countAverages + count
                costAverages = costAverages + (count * moneyCostInt)
                totalRuns = totalRuns + 1
                # Optionally print total runs
                if showPrints == "y":
                    print(totalRuns)
                # Reset count for next run
                count = 0
                break

# Record end time and calculate total duration
endDate = datetime.datetime.now()
diff = endDate - startDate
totalSeconds = diff.total_seconds()

# Display results
print(f"Successfully calculated! ({totalSeconds} seconds)")
print(f"On average, it took {countAverages / totalRuns} tries for success.")
print(f"It also cost about {costAverages / totalRuns} to get success.")


import random
import datetime
# Import required libraries, random for random number generation, and datetime for time calculation
count = 0
average = 0
# Set average and count variables to 0 as default (these are used to calculate the average)
iterationNum = -1
rangeNumVar = -1
# Set default value for iteration variables (these are used to determine how many times to run the program, and at which range)
rangeNum = input("Range (1-?):")
try:
    rangeNumVar = int(rangeNum)
except:
    print("Not valid integer, setting default to 100")
    rangeNumVar = 100
iterationsVar = input("Iteration Count:")
try:
    iterationNum = int(iterationsVar)
except:
    print("Not valid integer, setting default to 100")
    iterationNum = 100
# Convert string input to integer for the loop, setting a default value if invalid (example: user types "sixty" instead of 60)
doAverages = input("Perform averages? Turning this off doesn't display averages but reduces RAM significantly for larger computes (y/n):")
numDict = {}
# Set default number dictionary
startDate = datetime.datetime.now()
# Set startDate for program runtime calculation
for i in range(int(iterationNum)):
    x = random.randint(1,rangeNumVar)
    numDict[x] = numDict.get(x, 0) + 1
    if doAverages == "y":
        average = average + x
    count = count + 1
    print(count)
# This loop generates a random number, and saves it to the dictionary, adding 1 to the amount of times that number has been chosen
largestNumberKey = -1
largestCount = -1
# Set default values for largestNumber and largestCount variables (these determine the most common occurance)
for item in numDict:
    if largestNumberKey == -1:
        largestNumberKey = item
    if largestCount == -1:
        largestCount = numDict[item]
    if numDict[item] > largestCount:
        largestCount = numDict[item]
        largestNumberKey = item
# This loop determines the most common occurance. First, it checks if the variables are at -1, their default, which means that the loop just started.
# If so, it sets them to the current value, because it's the highest at that moment.
# Then, if the new item is bigger than the old one, it sets the new one as the highest. This repeats for every number.
endDate = datetime.datetime.now()
diff = endDate - startDate
# Sets endDate for runtime calculation, and calculates the difference between the dates
print("-----------------------")
print("Calculations Completed!")
print(f"Range: (1-{rangeNumVar}), ran {iterationNum} times.")
if doAverages == "y":
    print("Average:", average/count)
print("Most Common:", largestNumberKey, "with", largestCount, "occurrences")
print("Calculations took", diff.total_seconds(), "seconds to compute.")
print("-----------------------")
# Prints out statistics
input("Press enter to finish...")

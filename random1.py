import random  # Importing module
import time

def getRandomDate(startDate, endDate):  # Defining function
    print("Printing random date between", startDate, "and", endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))
    
    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

# Display result
print("Random Date =", getRandomDate("1/1/2016", "12/12/2018"))
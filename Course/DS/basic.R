x = BikeData$cyc_freq[1:10] == 'Daily'
x
female = BikeData[BikeData$gender == 'F',]$speed[1]
female

# How many of the cyclists in the data frame were students?
count = sum(BikeData[BikeData$student == 1,]$student)
# How often do they ride?
BikeData[BikeData$student == 1,]$cyc_freq
# And what was the average distance that they rode?
# sum(BikeData[BikeData$student == 1,]$distance) / count
mean(BikeData[BikeData$student == 1,]$distance)


library(SDSFoundations)
bike = BikeData

student <-bike[bike$student==1,]

sum(bike[bike$student == 1,]$student)


# Import the BikeData dataset, name it "bike"

# Find the number of students in the dataset
table(bike$student)

# Pull out student data into a new dataframe
student <- bike[bike$student==1,]

# Find how often the students ride, using the new dataframe
table(student$cyc_freq)

# Create a vector for the distance variable
distance <-student$distance

# Find average distance ridden
mean(distance)

daily_riders = bike[bike$cyc_freq == 'Daily',]
table(daily_riders$gender)
ages = mean(daily_riders$age)
ages

mean(daily_riders[daily_riders$gender=='F',]$age)

male_daily_rider = daily_riders[daily_riders$gender=='M',]
mean(male_daily_rider$age)
male_daily_rider[male_daily_rider$age>=30,]


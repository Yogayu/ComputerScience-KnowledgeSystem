library(SDSFoundations)
animalData = AnimalData

head(animalData, 10)

head(animalData[animalData$Dog.Group],2)

table(animalData$Outcome.Type)
# First 10 animal in the dataset were adopted
table(head(animalData$Outcome.Type, 10))

plot(animalData$Color, main="The animal data")

table(animalData$Sex)

plot(animalData$Sex)

mean(animalData$Days.Shelter)
median(animalData$Days.Shelter)
fivenum((animalData$Days.Shelter))

hist(animalData$Age.Intake,main="Histgram of Intake Ages", xlab = "Age at Intake")

femalleage = animalData$Age.Intake[animalData$Sex=='Female']
maleage = animalData$Age.Intake[animalData$Sex=='Male']

head(femalleage)

hist(femalleage)
hist(maleage)

which(femalleage == 1)
which(animalData$Age.Intake == 17)

animalData[415,]


Owner_Surrender = animalData[animalData$Intake.Type=="Owner Surrender",]
head(Owner_Surrender,1)

animaldata = animalData

#Find the number of animals that were adopted
table(animaldata$Outcome.Type)

#Pull out only adopted animals
adopted <- animaldata[animaldata$Outcome.Type=="Adoption",]

#Pull out just the days in shelter for the adopted animals
daystoadopt <- adopted$Days.Shelter

#Visualize and describe this variable
hist(daystoadopt)
fivenum(daystoadopt)
mean(daystoadopt)
sd(daystoadopt)
median(daystoadopt)
which(animaldata$Days.Shelter==max(daystoadopt))
IQR(daystoadopt)

animaldata[425,]

x = daystoadopt[13]
x
x_average = mean(daystoadopt)
x_average
zScore = (x- x_average)/sd(daystoadopt)
zScore


# Problem two
# how many adult (at intake) cats and dogs are in the dataset.
adult = animaldata[animaldata$Age.Intake >=1,]
head(adult)

dogs = adult[adult$Animal.Type == "Dog",]
dogs_weight = dogs$Weight
hist(dogs_weight, main= "Adult dogs weight")
mean(dogs_weight)
dog_median = median(dogs_weight)
fivenum(dogs_weight)
which(dogs_weight==13)
dog_IQE = IQR(dogs_weight)

q = (13 - dog_median)/dog_IQE*2
q

cats = adult[adult$Animal.Type == "Cat",]
cats_weight = cats$Weight


hist(cats_weight, main="Adult cats weight")
mean_cat = mean(cats_weight)
sd_cat = sd(cats_weight)
median(cats_weight)


which(cats_weight==13)
score = (13-mean)/sd_cat
score
1-pnorm(score)

animaldata

dogs = animaldata[animaldata$Animal.Type=="Dog",]
table(dogs$Intake.Type)

dogs_owner_surrender = dogs[dogs$Intake.Type == "Owner Surrender",]
table(dogs_owner_surrender$Outcome.Type)
return_dog = dogs_owner_surrender[dogs_owner_surrender$Outcome.Type=='Return to Owner',]
mean(return_dog$Days.Shelter)

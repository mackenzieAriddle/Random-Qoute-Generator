import random
famousName = ["Ronald Mcdonald", "George Floyd", "Lee Harvey Oswald", "State Farm",
 "Ronald Raegan", "Jimmy Carter", "Miley Cyrus", "Christopher Columbus", "The Red Power Ranger", "Forest Gump",
 "The Boy From UP", "Jimmy Neutron", "Belle Delephine", "Mr. Clean", "Naruto", "Popeye", "The Green Power Ranger", "Shia Labeouf",
 "Michilin Tire Guy", "Pilsbury Dough Boy", "Koolaid Guy", "The Leprichon? From Lucky Charms", "Obama", "Veggie Tales Tomato",
 "Veggie Tales Cucumber", "Veggie Tales Pea Army", "Avacodo-Jager", "Albert Einestein", "Nikolai Tesla"]
famousQoute = ["Like a good neighbor, TRADEMARKED COMPANY is there!", "I can't breathe", "OH YEAH", "BELIEVE IT", "Trix are for kids!",
 "GET THAT OUT OF YOUR MOUTH", "the only thing you have to fear is fear itself", "um... I think i poked a hole in my hand",
 "Two things are infinite- the univers and human stupidity", "Anyone who has never made a mistake has never tried anything new",
 "save 15 percemt or more on car insurance", "If we shouldn't eat at night, why is there a light in the fridge?"]

print("Would you like to play a little game?")
print("Press Enter if you dare...")

while True:
	input("...")
	print(" '" + random.choice(famousQoute) + "'  - " + random.choice(famousName))

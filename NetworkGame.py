import csv
import random
from os import system 
contents = []
IPs = ["216.58.213.14","140.82.118.4", "151.101.60.193", "143.204.188.44"]
sites = ["YouTube.com","Github.com","Imgur.com","Soundcloud.com"]
SSP = ["1.	Encryption - take the three letters and XOR encrypt them with the key - Do this by your next turn or miss a turn", "2.	Database request needed - Miss next turn","3.	Compression - Data is reduced to one packet","4.	Cache prize - Store all DNS entries","5.	Corrupter - move the corrupter 3 spaces","6.	Gigabit Ethernet - make your next roll now"]
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
with open('GSALEpicGlossary.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		contents.append(row)
while True:
	randomNum1 = random.randint(0,len(contents)-1)
	diceroll = random.randint(1,11)
	print("For a roll of ", diceroll, " for MCQ or ", diceroll*2, " to take a guess now")
	input("What is this defining?  --> "+contents[randomNum1][1])
	possanswers = []
	for i in range(3):
		possanswers.append(contents[random.randint(0,len(contents)-1)][0])
	possanswers.append(contents[randomNum1][0])
	possanswers.sort()
	print(possanswers)
		
	input('\nReturn to reveal answer\n\n')
	print ("Correct definition -->  ",contents[randomNum1][0],"\n")
	nextStep = input('Return for next definition, type site for a new site or server if you have landed on a web server')
	if nextStep == "site":
		print(random.choice(sites))
		input()
	if nextStep == "server":
		randomnumber = random.randint(0,5)
		print(SSP[randomnumber])
		if randomnumber == 0:
			print("Word = ",random.choice(letters),random.choice(letters),random.choice(letters))
			print("Key = ",random.choice(letters),random.choice(letters),random.choice(letters))
			print("A is 65 and a is 97")
		
			
		input()
	_ = system('cls') # Windows use 'cls', everyone else use 'clear'

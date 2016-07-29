from ftplib import FTP
import os
import zipfile
import json
import ConfigParser
import mysql.connector

config = ConfigParser.ConfigParser()
config.read('config.ini')

username = config.get('db', 'username')
password = config.get('db', 'password')
host = config.get('db', 'host')
database = config.get('db', 'database')

currentPath = config.get('config', 'filepath')

orgsFilename = config.get('files', 'orgs')
newpetsFilename = config.get('files', 'newpets')
petsFilename =  config.get('files', 'pets')
updatedpetsFilename = config.get('files', 'updatedpets')

unzipPath = os.path.join(currentPath, 'RGFilesUnzipped')


if False:
	print "RUNNING ORGS"
	
	# Orgs import
	orgsJSON = []
	with open(os.path.join(unzipPath, orgsFilename), 'r') as orgFile:
		for org in orgFile:
			orgsJSON.append(json.loads(org))
			

	insertOrg = ("INSERT INTO `orgs` (`orgID`, `status`, `name`, `address`, `city`, `state`, `zip`, `country`, `phone`, `fax`, `email`, `orgurl`, `facebookUrl`, `orgType`, `orgSpecies`, `serveAreas`, `about`, `meetPets`, `services`, `allowAppSubmissions`, `messageOrg`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s);")

	cnx = mysql.connector.connect(user=username, password=password, host=host, database=database)
	curA = cnx.cursor(buffered=True)
	curA.execute(insertOrg,(orgsJSON[1]["orgID"], 
							orgsJSON[1]["status"], 
							orgsJSON[1]["name"], 
							orgsJSON[1]["address"], 
							orgsJSON[1]["city"], 
							orgsJSON[1]["state"], 
							orgsJSON[1]["zip"], 
							orgsJSON[1]["country"], 
							orgsJSON[1]["phone"], 
							orgsJSON[1]["fax"], 
							orgsJSON[1]["email"], 
							orgsJSON[1]["orgurl"], 
							orgsJSON[1]["facebookUrl"], 
							orgsJSON[1]["orgType"], 
							orgsJSON[1]["orgSpecies"], 
							orgsJSON[1]["serveAreas"], 
							orgsJSON[1]["about"], 
							orgsJSON[1]["meetPets"], 
							orgsJSON[1]["services"], 
							orgsJSON[1]["allowAppSubmissions"], 
							orgsJSON[1]["messageOrg"]))
	cnx.commit()
	cnx.close()


# Pets import
petsJSON = []	
with open(os.path.join(unzipPath, petsFilename), 'r') as dataFile:
    for line in dataFile:
		petsJSON.append(json.loads(line))        


# SDP
# this is returning 0 objects, and I don't know why     
# open the object as a file
# for each line, json.loads   

insertPet = ("INSERT INTO `animals` (`animalID`, `orgID`, `lastUpdated`, `rescueID`, `name`, `species`, `breed`, `primaryBreed`, `secondaryBreed`, `sex`, `mixed`, `dogs`, `cats`, `kids`, `declawed`, `housetrained`, `age`, `birthdate`, `specialneeds`, `altered`, `size`, `sizecurrent`, `sizepotential`, `sizeuom`, `uptodate`, `color`, `coatlength`, `pattern`, `courtesy`, `found`, `founddate`, `foundzipcode`, `animallocation`, `killdate`, `killreason`, `needsfoster`, `adoptionfee`, `description`, `descriptionplain`, `okwithadults`, `obediencetraining`, `ownerexperience`, `exerciseneeds`, `energylevel`, `groomingneeds`, `yardrequired`, `fence`, `shedding`, `newpeople`, `vocal`, `activitylevel`, `eartype`, `eyecolor`, `tailtype`, `olderkidsonly`, `nosmalldogs`, `nolargedogs`, `nofemaledogs`, `nomaledogs`, `okforseniors`, `hypoallergenic`, `goodincar`, `leashtrained`, `cratetrained`, `fetches`, `playstoys`, `swims`, `lap`, `okwithfarmanimals`, `drools`, `apartment`, `noheat`, `nocold`, `protective`, `escapes`, `predatory`, `hasallergies`, `specialdiet`, `ongoingmedical`, `hearingimpaired`, `obedient`, `playful`, `timid`, `skittish`, `independent`, `affectionate`, `eagertoplease`, `intelligent`, `eventempered`, `gentle`, `goofy`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '%s', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);")

cnx = mysql.connector.connect(user=username, password=password, host=host, database=database)
curA = cnx.cursor(buffered=True)

for pet in petsJSON:
	curA.execute(insertPet,(pet["animalID"], 						 #91
						pet["orgID"], 
						pet["lastUpdated"], 
						pet["rescueID"], 
						pet["name"], 
						pet["species"], 
						pet["breed"], 
						pet["primaryBreed"], 
						pet["secondaryBreed"], 
						pet["sex"], 
						pet["mixed"], 
						pet["dogs"], 
						pet["cats"], 
						pet["kids"], 
						pet["declawed"], 
						pet["housetrained"], 
						pet["age"], 
						pet["birthdate"], 
						pet["specialNeeds"], 
						pet["altered"], 
						pet["size"], 
						pet["sizeCurrent"], 
						pet["sizePotential"], 
						pet["sizeUOM"], 
						pet["uptodate"], 
						pet["color"], 
						pet["coatLength"], 
						pet["pattern"], 
						pet["courtesy"], 
						pet["found"], 
						pet["foundDate"], 
						pet["foundZipcode"], 
						pet["animalLocation"], 
						pet["killDate"], 
						pet["killReason"], 
						pet["needsFoster"], 
						pet["adoptionFee"], 
						pet["description"], 
						pet["descriptionPlain"], 
						pet["oKWithAdults"], 
						pet["obedienceTraining"], 
						pet["ownerExperience"], 
						pet["exerciseNeeds"], 
						pet["energyLevel"], 
						pet["groomingNeeds"], 
						pet["yardRequired"], 
						pet["fence"], 
						pet["shedding"], 
						pet["newPeople"], 
						pet["vocal"], 
						pet["activityLevel"], 
						pet["earType"], 
						pet["eyeColor"], 
						pet["tailType"], 
						pet["olderKidsOnly"], 
						pet["noSmallDogs"], 
						pet["noLargeDogs"], 
						pet["noFemaleDogs"], 
						pet["noMaleDogs"], 
						pet["oKForSeniors"], 
						pet["hypoallergenic"], 
						pet["goodInCar"], 
						pet["leashtrained"], 
						pet["cratetrained"], 
						pet["fetches"], 
						pet["playsToys"], 
						pet["swims"], 
						pet["lap"], 
						pet["oKWithFarmAnimals"], 
						pet["drools"], 
						pet["apartment"], 
						pet["noHeat"], 
						pet["noCold"], 
						pet["protective"], 
						pet["escapes"], 
						pet["predatory"], 
						pet["hasAllergies"], 
						pet["specialDiet"], 
						pet["ongoingMedical"], 
						pet["hearingImpaired"], 
						pet["obedient"], 
						pet["playful"], 
						pet["timid"], 
						pet["skittish"], 
						pet["independent"], 
						pet["affectionate"], 
						pet["eagerToPlease"], 
						pet["intelligent"], 
						pet["eventempered"], 
						pet["gentle"], 
						pet["goofy"]))
						
cnx.commit()
cnx.close()












  

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
with open(os.path.join(unzipPath, petsFilename), 'r') as petFile:
	for pet in petFile:	    
		petsJSON.append(json.loads(pet))


# SDP
# this is returning 0 objects, and I don't know why        

insertPet = ("INSERT INTO `animals` (`animalID`, `orgID`, `lastUpdate`, `rescueID`, `name`, `species`, `breed`, `primaryBreed`, `secondaryBreed`, `sex`, `mixed`, `dogs`, `cats`, `kids`, `declawed`, `houseTrained`, `age`, `birthdate`, `specialNeeds`, `altered`, `size`, `sizeCurrent`, `sizePotential`, `sizeUOM`, `upToDate`, `color`, `coatLength`, `pattern`, `courtesy`, `found`, `foundDate`, `foundZipCode`, `animalLocation`, `killDate`, `killReason`, `needsFoster`, `adoptionFee`, `description`, `descriptionPlain`, `oKWithAdults`, `obedienceTraining`, `ownerExperience`, `exerciseNeeds`, `energyLevel`, `groomingNeeds`, `yardRequired`, `fence`, `shedding`, `newPeople`, `vocal`, `activityLevel`, `earType`, `eyeColor`, `tailType`, `olderKidsOnly`, `noSmallDogs`, `noLargeDogs`, `noFemaleDogs`, `noMaleDogs`, `oKForSeniors`, `hypoallergenic`, `goodInCar`, `leashtrained`, `cratetrained`, `fetches`, `playsToys`, `swims`, `lap`, `oKWithFarmAnimals`, `drools`, `apartment`, `noHeat`, `noCold`, `protective`, `escapes`, `predatory`, `hasAllergies`, `specialDiet`, `ongoingMedical`, `hearingImpaired`, `obedient`, `playful`, `timid`, `skittish`, `independent`, `affectionate`, `eagerToPlease`, `intelligent`, `eventempered`, `gentle`, `goofy`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'xxxxxxxx', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);")

cnx = mysql.connector.connect(user=username, password=password, host=host, database=database)
curA = cnx.cursor(buffered=True)
curA.execute(insertPet,(petsJSON[0]["animalID"], 						
						petsJSON[0]["orgID"], 
						petsJSON[0]["lastUpdate"], 
						petsJSON[0]["rescueID"], 
						petsJSON[0]["name"], 
						petsJSON[0]["species"], 
						petsJSON[0]["breed"], 
						petsJSON[0]["primaryBreed"], 
						petsJSON[0]["secondaryBreed"], 
						petsJSON[0]["sex"], 
						petsJSON[0]["mixed"], 
						petsJSON[0]["dogs"], 
						petsJSON[0]["cats"], 
						petsJSON[0]["kids"], 
						petsJSON[0]["declawed"], 
						petsJSON[0]["houseTrained"], 
						petsJSON[0]["age"], 
						petsJSON[0]["birthdate"], 
						petsJSON[0]["specialNeeds"], 
						petsJSON[0]["altered"], 
						petsJSON[0]["size"], 
						petsJSON[0]["sizeCurrent"], 
						petsJSON[0]["sizePotential"], 
						petsJSON[0]["sizeUOM"], 
						petsJSON[0]["upToDate"], 
						petsJSON[0]["color"], 
						petsJSON[0]["coatLength"], 
						petsJSON[0]["pattern"], 
						petsJSON[0]["courtesy"], 
						petsJSON[0]["found"], 
						petsJSON[0]["foundDate"], 
						petsJSON[0]["foundZipCode"], 
						petsJSON[0]["animalLocation"], 
						petsJSON[0]["killDate"], 
						petsJSON[0]["killReason"], 
						petsJSON[0]["needsFoster"], 
						petsJSON[0]["adoptionFee"], 
						petsJSON[0]["description"], 
						petsJSON[0]["descriptionPlain"], 
						petsJSON[0]["oKWithAdults"], 
						petsJSON[0]["obedienceTraining"], 
						petsJSON[0]["ownerExperience"], 
						petsJSON[0]["exerciseNeeds"], 
						petsJSON[0]["energyLevel"], 
						petsJSON[0]["groomingNeeds"], 
						petsJSON[0]["yardRequired"], 
						petsJSON[0]["fence"], 
						petsJSON[0]["shedding"], 
						petsJSON[0]["newPeople"], 
						petsJSON[0]["vocal"], 
						petsJSON[0]["activityLevel"], 
						petsJSON[0]["earType"], 
						petsJSON[0]["eyeColor"], 
						petsJSON[0]["tailType"], 
						petsJSON[0]["olderKidsOnly"], 
						petsJSON[0]["noSmallDogs"], 
						petsJSON[0]["noLargeDogs"], 
						petsJSON[0]["noFemaleDogs"], 
						petsJSON[0]["noMaleDogs"], 
						petsJSON[0]["oKForSeniors"], 
						petsJSON[0]["hypoallergenic"], 
						petsJSON[0]["goodInCar"], 
						petsJSON[0]["leashtrained"], 
						petsJSON[0]["cratetrained"], 
						petsJSON[0]["fetches"], 
						petsJSON[0]["playsToys"], 
						petsJSON[0]["swims"], 
						petsJSON[0]["lap"], 
						petsJSON[0]["oKWithFarmAnimals"], 
						petsJSON[0]["drools"], 
						petsJSON[0]["apartment"], 
						petsJSON[0]["noHeat"], 
						petsJSON[0]["noCold"], 
						petsJSON[0]["protective"], 
						petsJSON[0]["escapes"], 
						petsJSON[0]["predatory"], 
						petsJSON[0]["hasAllergies"], 
						petsJSON[0]["specialDiet"], 
						petsJSON[0]["ongoingMedical"], 
						petsJSON[0]["hearingImpaired"], 
						petsJSON[0]["obedient"], 
						petsJSON[0]["playful"], 
						petsJSON[0]["timid"], 
						petsJSON[0]["skittish"], 
						petsJSON[0]["independent"], 
						petsJSON[0]["affectionate"], 
						petsJSON[0]["eagerToPlease"], 
						petsJSON[0]["intelligent"], 
						petsJSON[0]["eventempered"], 
						petsJSON[0]["gentle"], 
						petsJSON[0]["goofy"]))
						
cnx.commit()
cnx.close()












  

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
orgsData = []
with open(os.path.join(unzipPath, orgsFilename), 'r') as orgFile:
    for org in orgFile:
        temp = json.loads(org)
        if 'orgID' in temp:  
	        orgsData.append((
				temp["orgID"],
				temp['status'],
				temp['name'],
				temp['address'],
				temp['city'],
				temp['state'],
				temp['zip'],
				temp['country'],
				temp['phone'],
				temp['fax'],
				temp['email'],
				temp['orgurl'],
				temp['facebookUrl'],        
				temp['orgType'],
				temp['orgSpecies'],        
				temp['serveAreas'],                
				temp['about'],
				temp['meetPets'],
				temp['services'],
				temp['allowAppSubmissions'],
				temp['messageOrg']    
			))
        

insertOrg = ("INSERT INTO `orgs` (`orgID`, `status`, `name`, `address`, `city`, `state`, `zip`, `country`, `phone`, `fax`, `email`, `orgurl`, `facebookUrl`, `orgType`, `orgSpecies`, `serveAreas`, `about`, `meetPets`, `services`, `allowAppSubmissions`, `messageOrg`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s);")

cnx = mysql.connector.connect(user=username, password=password, host=host, database=database)
curA = cnx.cursor(buffered=True)

try:
    curA.executemany(insertOrg, orgsData)
    cnx.commit()
    
except Exception,e:
    print str(e)
	cnx.rollback()


# Pets import
petsData = []
with open(os.path.join(unzipPath, petsFilename), 'r') as petFile:
	for pet in petFile:	    
		temp = json.loads(pet)		
		petsData.append((
			temp["animalID"],                          
			temp["orgID"], 
			temp["lastUpdated"], 
			temp["rescueID"], 
			temp["name"], 
			temp["species"], 
			temp["breed"], 
			temp["primaryBreed"], 
			temp["secondaryBreed"], 
			temp["sex"], 
			temp["mixed"], 
			temp["dogs"], 
			temp["cats"], 
			temp["kids"], 
			temp["declawed"], 
			temp["housetrained"], 
			temp["age"], 
			temp["birthdate"], 
			temp["specialNeeds"], 
			temp["altered"], 
			temp["size"], 
			temp["sizeCurrent"], 
			temp["sizePotential"], 
			temp["sizeUOM"], 
			temp["uptodate"], 
			temp["color"], 
			temp["coatLength"], 
			temp["pattern"], 
			temp["courtesy"], 
			temp["found"], 
			temp["foundDate"], 
			temp["foundZipcode"], 
			temp["animalLocation"], 
			temp["killDate"], 
			temp["killReason"], 
			temp["needsFoster"], 
			temp["adoptionFee"], 
			temp["description"], 
			temp["descriptionPlain"], 
			temp["oKWithAdults"], #40
			temp["obedienceTraining"], 
			temp["ownerExperience"], 
			temp["exerciseNeeds"], 
			temp["energyLevel"], 
			temp["groomingNeeds"], 
			temp["yardRequired"], 
			temp["fence"], 
			temp["shedding"], 
			temp["newPeople"], 
			temp["vocal"], 
			temp["activityLevel"], 
			temp["earType"], 
			temp["eyeColor"], 
			temp["tailType"], 
			temp["olderKidsOnly"], 
			temp["noSmallDogs"], 
			temp["noLargeDogs"], 
			temp["noFemaleDogs"], 
			temp["noMaleDogs"], 
			temp["oKForSeniors"], 
			temp["hypoallergenic"], 
			temp["goodInCar"], 
			temp["leashtrained"], 
			temp["cratetrained"], 
			temp["fetches"], 
			temp["playsToys"], 
			temp["swims"], 
			temp["lap"], 
			temp["oKWithFarmAnimals"], 
			temp["drools"], #70
			temp["apartment"], 
			temp["noHeat"], 
			temp["noCold"], 
			temp["protective"], 
			temp["escapes"], 
			temp["predatory"], 
			temp["hasAllergies"], 
			temp["specialDiet"], 
			temp["ongoingMedical"], 
			temp["hearingImpaired"], 
			temp["obedient"], 
			temp["playful"], 
			temp["timid"], 
			temp["skittish"], 
			temp["independent"], 
			temp["affectionate"], 
			temp["eagerToPlease"], 
			temp["intelligent"], 
			temp["eventempered"], 
			temp["gentle"], 
			temp["goofy"]      
		))


insertPet = ("INSERT INTO `animals` (`animalID`, `orgID`, `lastUpdated`, `rescueID`, `name`, `species`, `breed`, `primaryBreed`, `secondaryBreed`, `sex`, `mixed`, `dogs`, `cats`, `kids`, `declawed`, `houseTrained`, `age`, `birthdate`, `specialNeeds`, `altered`, `size`, `sizeCurrent`, `sizePotential`, `sizeUOM`, `upToDate`, `color`, `coatLength`, `pattern`, `courtesy`, `found`, `foundDate`, `foundZipCode`, `animalLocation`, `killDate`, `killReason`, `needsFoster`, `adoptionFee`, `description`, `descriptionPlain`, `oKWithAdults`, `obedienceTraining`, `ownerExperience`, `exerciseNeeds`, `energyLevel`, `groomingNeeds`, `yardRequired`, `fence`, `shedding`, `newPeople`, `vocal`, `activityLevel`, `earType`, `eyeColor`, `tailType`, `olderKidsOnly`, `noSmallDogs`, `noLargeDogs`, `noFemaleDogs`, `noMaleDogs`, `oKForSeniors`, `hypoallergenic`, `goodInCar`, `leashtrained`, `cratetrained`, `fetches`, `playsToys`, `swims`, `lap`, `oKWithFarmAnimals`, `drools`, `apartment`, `noHeat`, `noCold`, `protective`, `escapes`, `predatory`, `hasAllergies`, `specialDiet`, `ongoingMedical`, `hearingImpaired`, `obedient`, `playful`, `timid`, `skittish`, `independent`, `affectionate`, `eagerToPlease`, `intelligent`, `eventempered`, `gentle`, `goofy`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '%s', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);")


try:
    curA.executemany(insertOrg, orgsData)
    cnx.commit()
    
except Exception,e:
    print str(e)
	cnx.rollback()
    

cnx.close()



# TODO

# Perform daily updates of the data
# On a daily basis, download the adoptable pet data from your API key's FTP account.  Process the updated data.
# Process the data for each pet in the updatedpets_n.json files.
# Add the pets that are in the newpets_n.json files.
# Delete any pets (by animalID) that are not listed in the petlist.csv file.



# Perform regular scrubs of the data
# On a regular basis (e.g., weekly or monthly), perform a full refresh of data from the orgs_n.json and pets_n.json data files.










  

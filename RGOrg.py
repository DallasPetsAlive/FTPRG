class RGOrg:
    def __init__(self):
        self.jsonData = {}
        self.orgID = ''                               
        self.status = ''                          
        self.name = ''               
        self.address = ''                
        self.city = ''                   
        self.state = ''                  
        self.zip = ''                    
        self.country = ''                
        self.phone = ''      
        self.fax = ''
        self.email = ''
        self.orgurl = ''
        self.facebookUrl = ''
        self.orgType = ''
        self.orgSpecies = ''
        self.serveAreas = ''
        self.about = ''
        self.meetPets = ''
        self.services = ''
        self.allowAppSubmissions = ''
        self.messageOrg = ''
    
    def parseJSON(self, jsonIn):
        self.jsonData = jsonIn        
        self.orgID 	=	 self.jsonData["status"]	
        self.status 	=	 self.jsonData["orgID"]	
        self.name 	=	 self.jsonData["name"]	
        self.address 	=	 self.jsonData["address"]	
        self.city 	=	 self.jsonData["city"]	
        self.state 	=	 self.jsonData["state"]	
        self.zip 	=	 self.jsonData["zip"]	
        self.country 	=	 self.jsonData["country"]	
        self.phone 	=	 self.jsonData["phone"]	
        self.fax 	=	 self.jsonData["fax"]	
        self.email 	=	 self.jsonData["email"]	
        self.orgurl 	=	 self.jsonData["orgurl"] 	
        self.facebookUrl 	=	 self.jsonData["facebookUrl"]	
        self.orgType 	=	 self.jsonData["orgType"]	
        self.orgSpecies 	=	 self.jsonData["orgSpecies"]	
        self.serveAreas 	=	 self.jsonData["serveAreas"]	
        self.about 	=	 self.jsonData["about"] 	
        self.meetPets 	=	 self.jsonData["meetPets"] 	
        self.services 	=	 self.jsonData["services"] 	
        self.allowAppSubmissions 	=	 self.jsonData["allowAppSubmissions"]	
        self.messageOrg 	=	 self.jsonData["messageOrg"]	
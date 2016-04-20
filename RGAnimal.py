class RGAnimal:
    def __init__(self):
        self.jsonData = {}
        self.species = ''
        self.ID = ''
        self.name = ''
        self.pictures = []
        self.description = ''
        self.size = ''
        self.coatLength = ''
        self.age = ''
        self.breed = ''
        self.size = ''

    def parseJSON(self, jsonIn):
        self.jsonData = jsonIn
        self.ID = self.jsonData['animalID']
        self.species = self.jsonData['species']


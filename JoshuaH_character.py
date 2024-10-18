#This is a change


class Character(object):
    
    def __init__(self, name = "Velder",
                 hitPoints = 20,
                 hitChance = 70,
                 maxDamage = 10,
                 armor = 5):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        value = testInt(self, value)
        self.__name = value
    
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        self.hitPoints = value
       
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @property
    def armor():
        return self.__armor
    
    def printStats(self):
        print(name)
        print(hitPoints)
        print(maxDamage)
        print(armor)
    
    #def hit(self, enemy):
        
    def testInt(self, value, min = 0, max = 100, default = 0):
    """ takes in value 
        checks to see if it is an int between
        min and max.  If it is not a legal value
        set it to default """

    out = default

    if type(value) == int:
        if value >= min:
            if value <= max:
                out = value 
            else:
                print("Too large")
        else:
            print("Too small")
    else:
        print("Must be an int")

    return out
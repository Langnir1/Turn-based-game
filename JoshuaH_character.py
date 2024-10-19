import random

class Character(object):
  # Check if my stuff is right
  # What do I do about the tbc module
  # Did I implement the 
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
        self.__name = value
    
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        self.__hitPoints = self.testInt(value, 0, 100, 10)
        
    @property
    def hitChance(self):
        return self.__hitChance
    
    @hitChance.setter
    def hitChance(self, value):
        self.__hitChance = self.testInt(value, 0, 100, 50)
       
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value):
        self.__maxDamage = self.testInt(value, 0, 100, 10)
    
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, value):
        self.__armor = self.testInt(value, 0, 10, 2)
        
    def printStats(self):
        print(self.name)
        print(self.hitPoints)
        print(self.hitChance)
        print(self.maxDamage)
        print(self.armor)
    
    def hit(self, enemy):
        if random.randint(1, 100) < self.hitChance:
            print(f"{self.name} hits {enemy.name}.")
            damage = random.randint(1, self.maxDamage)
            print(f"{enemy.name} takes {damage} points of damage")
            damage -= enemy.armor
            if damage < 0:
                damage = 0
            if enemy.armor > 0:
                print(f"{enemy.name} has armor and it takes {enemy.armor} points of damage")
            enemy.hitPoints -= damage
            return enemy.hitPoints
        else:
            print(f"{self.name} missed {enemy.name}")
            
        
    def testInt(self, value, min = 0, max = 100, default = 0):
        """takes in value 
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
    
    def fight(self, hero, monster):
        hero.hit(monster)
        print(f"The {monster.name} has {monster.hitPoints} hp remaining")
        monster.hit(hero)
        print(f"{hero.name} has {hero.hitPoints} hp remaining")
        
        keepGoing = True
        while(keepGoing):
            if monster.hitPoints <= 0:
                print(f"{hero.name} was won the fight!")
                keepGoing = False
            if hero.hitPoints <= 0:
                print(f"The {monster.name} has won the fight")
                keepGoing = False
            else:
                print("----------")
                hero.hit(monster)
                print(f"The {monster.name} has {monster.hitPoints} hp remaining")
                if monster.hitPoints <= 0:
                    print(f"{hero.name} has won")
                    break;
                monster.hit(hero)
                print(f"{hero.name} has {hero.hitPoints} hp remaining")
                
        
        

def main():
    hero = Character()
    hero.printStats()
    enemy = Character("Goblin", 20, 30, 50, 5)
    enemy.printStats()
    #hero.hit(enemy)
    #enemy.printStats()
    combat = Character()
    combat.fight(hero, enemy)
    

if __name__ == "__main__":
    main()
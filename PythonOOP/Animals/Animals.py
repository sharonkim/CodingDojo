class Animal(name, health):

    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -=1
        return self

    def run(self):
        self.health -=5
        return self

    def displayHealth(self):
        print self.name, 'Health: ', self.health

animal = Animal('animal')
animal.walk().walk().run().run().displayHealth()
# animal.fly().pet()

class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health +=5
        return self

spot = Dog('spot')
spot.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):

    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -=10
        return self

    def displayHealth(self):
        print 'This is a Dragon!'
        super(Dragon, self).displayHealth()

toothless = Dragon('toothless')
toothless.walk().walk().walk().run().run().fly().fly().displayHealth()

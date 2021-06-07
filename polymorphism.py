

# Parent Class
class Boat:
    model = 'Unknown'
    length = 22
    color =  'Black'
    propultion = 'gas engine'
    price = 'Unknown'

    def information(self): # Defines a method for parent class
        x = "\nModel: {}\nLength: {}\nColor: {}\nPropultion: {}".format(self.model,self.length,self.color,self.propultion,self.price)
        return x

# Child Class 1 -- Inherits parent class properties plus
class SpeedBoat(Boat):
    model = 'hurricane'
    length = 22
    color = 'blue' #child class overrides parent class color
    propultion = 'gas engine'
    price = 80000
    engine = 'Honda 4-stroke'
    swim_platform = True

    def speed(self): # Defines a method for child class 1
        x = "\nHits 60 in 6 seconds and is perfect to get where you need to go with time to spare!"
        return x

# Child Class 2 --Inherits parent properties plus
class Kayak(Boat):
    model = 'Chatham'
    length = 17 # Child class overrides parent class length
    color = 'yellow' # Child class overrides parent class color
    propultion = 'paddle'  # Child class overrides parent class propultion
    price = 2000
    rudder = False
    skeg = True
    max_capacity = 350

    def paddle(self): # Defines a method for child class 2
        x = "\nEasily glides through the water with effortless paddling!"
        return x

if __name__ == "__main__":
    speedboat = SpeedBoat()  
    print(speedboat.information())
    print(speedboat.speed())

    kayak = Kayak()
    print(kayak.information())
    print(kayak.paddle())
    


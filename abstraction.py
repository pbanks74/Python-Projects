

#import  “abstractmethod” from the abc module (Abstract Base Class
from abc import ABC, abstractmethod 

class boat(ABC) :
    def billing_Statement(self, amount):
        print ("Your purchase amount: ",amount) # abstract function
    @abstractmethod
    def payment(self, amount):  
            pass
        
class VisaCardPayment(boat) :
    # Defines how to implement from parent class
    def payment(self, amount) :
        print('Your boat purchase amount of {} exceeded your $1000 limit '.format(amount))

obj = VisaCardPayment()
obj.billing_Statement("$1100")
obj.payment("$1100")
    

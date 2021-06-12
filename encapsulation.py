
class integer : # class utilizing "_protected" function
    def __init__(self) :
        self._protectedVar = 0 

obj = integer()
obj._protectedVar = 74 # changes the protected variable
print(obj._protectedVar) # prints the changed variable



class string : # class utilizing "__private" function
    def __init__(self):
        self.__privateVar = "Game"

    def getPrivate(self) :
        print(self.__privateVar) # prints variable "Game"

    def setPrivate(self, private) :
        self.__privateVar = private

obj = string()
obj.getPrivate()
obj.setPrivate("Settlers of Catan") # changes the private variable value
obj.getPrivate()

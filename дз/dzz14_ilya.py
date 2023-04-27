#1
class Car:
    def __init__(self, model, year, manuf, engine, color, price):
        self._model = model
        self._year = year
        self._manuf = manuf
        self._engine = engine
        self._color = color
        self._price = price
        
        
    def getAll(self):
        return self._model, self._year, self._manuf, self._engine, self._color, self._price
    
    def getModel(self):
        return self._model
    
    def getYear(self):
        return self._year
    
    def getManuf(self):
        return self._manuf
    
    def getEngine(self):
        return self._engine
    
    def getColor(self):
        return self._color
    
    def getPrice(self):
        return self._price
    
    
    def setModel(self, smth):
        self._model = smth
    
    def setYear(self, smth):
        self._year = smth
    
    def setManuf(self, smth):
        self._manuf = smth
    
    def setEngine(self, smth):
        self._engine = smth
    
    def setColor(self, smth):
        self._color = smth
    
    def setPrice(self, smth):
        self._price = smth
        
#2
class Book:
    def __init__(self, name, year, pub, author, genre, price):
        self._name = name
        self._year = year
        self._pub = pub
        self._author = author
        self._genre = genre
        self._price = price
        
        
    def getAll(self):
        return self._name, self._year, self._pub, self._author, self._genre, self._price
    
    def getName(self):
        return self._name
    
    def getYear(self):
        return self._year
    
    def getPubl(self):
        return self._pub
    
    def getAuthor(self):
        return self._author
    
    def getGenre(self):
        return self._genre
    
    def getPrice(self):
        return self._price
    
    
    def setName(self, smth):
        self._name = smth
    
    def setYear(self, smth):
        self._year = smth
    
    def setPubl(self, smth):
        self._pub = smth
    
    def setAuthor(self, smth):
        self._author = smth
    
    def setGenre(self, smth):
        self._genre = smth
    
    def setPrice(self, smth):
        self._price = smth
        
        
#3
class Car:
    def __init__(self, name, date, coun, city, cap):
        self._name = name
        self._date = date
        self._coun = coun
        self._city = city
        self._cap = cap
        
        
    def getAll(self):
        return self._name, self._date, self._coun, self._city, self._cap
    
    def getName(self):
        return self._name
    
    def getDate(self):
        return self._date
    
    def getCountry(self):
        return self._coun
    
    def getCity(self):
        return self._city
    
    def getCapacity(self):
        return self._cap
    
    
    def setName(self, smth):
        self._name = smth
    
    def setDate(self, smth):
        self._date = smth
    
    def setCountry(self, smth):
        self._coun = smth
    
    def setCity(self, smth):
        self._city = smth
    
    def setCapacity(self, smth):
        self._cap = smth

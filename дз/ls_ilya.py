#1
class Human:
    firstName = "Ivanov"
    lastName = "Ivan"
    middleName = "Ivanovich"
    tel = 87879654123
    city = "Moscow"
    country = "Russia"
    addr = "Petrovka"

    def getfName(self):
        return self.firstName
    def getlName(self):
        return self.lastName
    def getmName(self):
        return self.middleName
    def getTel(self):
        return self.tel
    def getCity(self):
        return self.city
    def getCountry(self):
        return self.country
    def getAddress(self):
        return self.addr
    
    def setfName(self, newfName):
        self.firstName = newfName
    def setlName(self, newlName):
        self.lastName = newlName
    def setmName(self, newmName):
        self.middleName = newmName
    def setTel(self, newTel):
        self.tel = newTel
    def setCity(self, newCity):
        self.city = newCity
    def setCountry(self, newCountry):
        self.country = newCountry
    def setAddress(self, newAddress):
        self.addr = newAddress


#2
class City:
    name = "Funburg"
    region = "Funburg region"
    country = "Qwertyng"
    people = 123456
    postIndex = 100000
    telCode = "+69"

    def getName(self):
        return self.name
    def getRegion(self):
        return self.region
    def getContry(self):
        return self.country
    def getPeople(self):
        return self.people
    def getPostIndex(self):
        return self.postIndex
    def getTelCode(self):
        return self.telCode
    
    def setName(self, newName):
        self.name = newName
    def setRegion(self, newRegion):
        self.region = newRegion
    def setCountry(self, newCountry):
        self.country = newCountry
    def setPeople(self, newPeople):
        self.people = newPeople
    def setPostIndex(self, newPostIndex):
        self.postIndex = newPostIndex
    def setTelCode(self, newTelCode):
        self.telCode = newTelCode

#3
class Country:
    name = "Qwertyng"
    continent = "IDK"
    people = 3000000
    telCode = "+69"
    capital = "Funburg"
    cities = ""

    def getName(self):
        return self.name
    def getContinent(self):
        return self.continent
    def getPeople(self):
        return self.people
    def getTelCode(self):
        return self.telCode
    def getCapital(self):
        return self.capital
    def getCities(self):
        return self.cities
    
    def setName(self, newName):
        self.name = newName
    def setContinent(self, newCont):
        self.continent = newCont
    def setPeople(self, newPeople):
        self.people = newPeople
    def setTelCode(self, newTC):
        self.telCode = newTC
    def setCapital(self, newCapital):
        self.capital = newCapital
    def setCities(self, newCities):
        self.cities = newCities


#4
class Fraction:
    divider = 3
    denominator = 6

    def getDivider(self):
        return self.divider
    def getDenominator(self):
        return self.denominator
    
    def setDivider(self, newDiv):
        self.divider = newDiv
    def setDenominator(self, newDen):
        self.denominator = newDen
    
    def sum(self):
        return self.divider + self.denominator
    def diff_DivDen(self):
        return self.divider - self.denominator
    def diff_DenDiv(self):
        return self.denominator - self.divider
    def mult(self):
        return self.divider * self.denominator
    def division_DivDen(self):
        return self.divider / self.denominator
    def division_DenDiv(self):
        return self.denominator / self.divider

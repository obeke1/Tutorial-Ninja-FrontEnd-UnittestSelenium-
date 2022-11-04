import configparser

config=configparser.RawConfigParser()
config.read("../configurations/guest.ini")

#print(config.sections())
#print(config.get('guest info', 'firstName'))

class readGuestConfig():
    @staticmethod
    def getfirstName():
        firstname=config.get('guest info', 'firstName')
        return firstname
    @staticmethod
    def getlastName():
        lastname=config.get('guest info', 'lastName')
        return lastname
    @staticmethod
    def getEmail():
        email=config.get('guest info', 'email')
        return email
    @staticmethod
    def getTelephone():
        telephone=config.get('guest info', 'telephone')
        return telephone
    @staticmethod
    def getAddress():
        address=config.get('guest info', 'address')
        return address
    @staticmethod
    def getCity():
        city=config.get('guest info','city')
        return city
    @staticmethod
    def getpostalCode():
        postalCode=config.get('guest info', 'postalCode')
        return postalCode
    @staticmethod
    def getCountry():
        country=config.get('guest info', 'country')
        return country
    @staticmethod
    def getRegion():
        region=config.get('guest info', 'region')
        return region



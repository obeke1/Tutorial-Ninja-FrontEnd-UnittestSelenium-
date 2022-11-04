import configparser

config=configparser.RawConfigParser()
config.read("../configurations/url.ini")

#print(config.sections())
#print(config.get('url','URL'))
class readURL():
    @staticmethod
    def url():
        url=config.get('url','URL')
        return url

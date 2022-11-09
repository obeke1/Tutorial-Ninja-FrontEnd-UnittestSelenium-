import configparser

config=configparser.RawConfigParser()
config.read("../configurations/url.ini")

#print(config.sections())
#print(config.get('url','URL'))
#print(config.get('url','month-year'))
class readURL():
    @staticmethod
    def url():
        url=config.get('url','URL')
        return url
    @staticmethod
    def month_year():
        month_year=config.get('url','month-year')
        return month_year



import requests as req
import xmltodict
import pprint

def stations(data):
    for x in data['Stations']['Station']:
        if x['Land'] == 'NL':
            print(x['Namen']['Kort'])

class apimanagement:
    ''' The ns api call system.
    The api call system  has the following properties:

    Attributes:
        station: A string representing the station name wich in turn is used in the api calls
        url: A string representing the url used to make api calls
    '''
    settings = str
    def __init__(self):
        ''' Return an api manager object wich can be used to make api calls'''
        with open('settings.xml') as settingsFile:
            self.settings = xmltodict.parse(settingsFile.read())
            print(self.settings)

    def getvertrektijden(self,station):
        '''Request an api call for "vertrektijden" '''
        url =  self.settings['settings']['api']['url']['vertrektijden'] + station
        data = self.sendcall(url)
        return  data

    def getstoring(self,station):
        '''Request an api call for "storingen" '''
        url =self.settings['settings']['api']['url']['storingen'] + station
        data = self.sendcall(url)
        return data

    def getstationlijst(self):
        '''request an api call for "stationlijst" '''
        url =  self.settings['settings']['api']['url']['stationlijst']
        data = self.sendcall(url)
        return data

    def sendcall(self,url):
        '''Make an api call and return it\'s data'''
        try:
            r = req.get(url, auth=(
            self.settings['settings']['api']['auth']['username'], self.settings['settings']['api']['auth']['password']))
            r.raise_for_status()
        except req.exceptions.HTTPError as e:
            print("Http Error:", e)
        except req.exceptions.ConnectionError as e:
            print("Error Connecting:", e)
        except req.exceptions.Timeout as e:
            print("Timeout Error:", e)
        except req.exceptions.RequestException as e:
            print("Er ging iets fout:", e)

        dict = xmltodict.parse(r.text)
        return dict

api = apimanagement()
stationdict = api.getstationlijst()
vertrektijden = api.getvertrektijden('utrecht centraal')
storingen = api.getstoring('utrecht centraal')
pprint.pprint(storingen)
pprint.pprint(vertrektijden)
stations(stationdict)

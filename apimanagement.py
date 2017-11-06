import requests as req
import xmltodict

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
        data = self.sendcall(station, self.settings['settings']['api']['url']['vertrektijden'])
        return  data

    def getstoring(self,station):
        '''Request an api call for "storingen" '''
        data = self.sendcall(station, self.settings['settings']['api']['url']['storingen'])
        return data

    def sendcall(self,station,url):
        '''Make an api call and return it\'s data'''
        try:
            r = req.get(url + station, auth=(
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

        nicetext = xmltodict.parse(r.text)
        return nicetext

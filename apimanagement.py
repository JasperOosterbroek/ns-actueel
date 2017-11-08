import requests as req
import xmltodict
import datetime

class apiManagement:
    """The ns api call system.
    The api call system  has the following properties:
    """
    settings = str

    def __init__(self):
        """Return an api manager object wich can be used to make api calls"""
        with open('settings.xml') as settingsFile:
            self.settings = xmltodict.parse(settingsFile.read())

    def getvertrektijden(self, station):
        """Request an api call for "vertrektijden" """
        url = self.settings['settings']['api']['url']['vertrektijden'] + station
        data = self.sendcall(url)
        return data

    def getstoring(self, station):
        """Request an api call for "storingen" """
        station = station
        url = self.settings['settings']['api']['url']['storingen'] + station
        data = self.sendcall(url)
        return data

    def getstationlijst(self):
        """request an api call for "stationlijst" """
        url = self.settings['settings']['api']['url']['stationlijst']
        data = self.sendcall(url)
        return data

    def getroute(self,startstation,endstation):
        """request an api call to generate a route"""
        url = self.settings['settings']['api']['url']['route'] + 'fromStation=' + startstation + '&toStation='+ endstation
        data = self.sendcall(url)
        return data

    def sendcall(self, url):
        """Make an api call and return it's data"""

        username = self.settings['settings']['api']['auth']['username']
        password = self.settings['settings']['api']['auth']['password']
        try:
            r = req.get(url, auth=(username, password))
            r.raise_for_status()
        except req.exceptions.HTTPError as e:
            print("Http Error:", e)
        except req.exceptions.ConnectionError as e:
            print("Error Connecting:", e)
        except req.exceptions.Timeout as e:
            print("Timeout Error:", e)
        except req.exceptions.RequestException as e:
            print("Er ging iets fout:", e)
        else:
            dataasdict = xmltodict.parse(r.text)
            return dataasdict
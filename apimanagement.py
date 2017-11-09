import collections
import requests as req
import xmltodict


class ApiManagement:
    """The ns api call system.
    The api call system  has the following properties:
    """
    settings = str

    def __init__(self):
        """Return an api manager object wich can be used to make api calls"""
        with open('settings.xml') as settingsFile:
            self.settings = xmltodict.parse(settingsFile.read())

    def getvertrektijden(self, station):
        """
        Get current travel times for the selected station

        :param station: the station for the vertrektijden
        :return: A dictionary with the station current planned trains

        Since the api return data is different every time we can only test the type
        >>> apimanager = ApiManagement()

        >>> type(apimanager.getvertrektijden('Utrecht centraal')) is collections.OrderedDict
        True

        This will throw an error because one of them is not a string
        >>> apimanager.getvertrektijden(0)
        'Error'

        This will throw an error because one of them is not a string
        >>> apimanager.getvertrektijden((1, 2, 3))
        'Error'

        This will throw an error because one of them is not a string
        >>> apimanager.getvertrektijden(['as','test'])
        'Error'

        This will throw an error because one of them is not a string
        >>> apimanager.getvertrektijden({'test': 'test','aap':'aap'})
        'Error'

        his will throw an error because one of them is not a string
        >>> apimanager.getvertrektijden({'test','test','aap','aap'})
        'Error'

        """
        try:
            url = self.settings['settings']['api']['url']['vertrektijden'] + station
        except (TypeError, AttributeError, ValueError):
            return 'Error'
        else:
            data = self.sendcall(url)
            return data

    def getstoring(self):
        """
        Request an api call for "storingen"
        >>> apimanager = ApiManagement()

        >>> type(apimanager.getstoring()) is collections.OrderedDict
        True

        """
        url = self.settings['settings']['api']['url']['storingen']
        data = self.sendcall(url)
        return data

    def getstationlijst(self):
        """
        request an api call for "stationlijst"
        >>> apimanager = ApiManagement()

        >>> type(apimanager.getstationlijst()) is collections.OrderedDict
        True

        """
        url = self.settings['settings']['api']['url']['stationlijst']
        data = self.sendcall(url)
        return data

    def getroute(self, startstation, endstation):
        """
        request an api call to generate a route

        :param startstation: the station for the start of the route
        :param endstation: the station for the end of the route
        :return: A dictionary with the route information

        >>> apimanager = ApiManagement()

        Since the api return data is different every time we can only test the type
        >>> type(apimanager.getroute('Utrecht centraal','Amsterdam')) is collections.OrderedDict
        True

        This will throw an error because one of them is not a string
        >>> apimanager.getroute(0,'Amsterdam')
        'Error'

        This will throw an error because one of them is not a string
        >>> apimanager.getroute((1, 2, 3),'Amsterdam')
        'Error'

        This will throw an error because one of them is not a string
        >>> apimanager.getroute(['as','test'],'Amsterdam')
        'Error'

        This will throw an error because one of them is not a string
        >>> apimanager.getroute({'test': 'test','aap':'aap'},'Amsterdam')
        'Error'

        his will throw an error because one of them is not a string
        >>> apimanager.getroute({'test','test','aap','aap'}, 'Amsterdam')
        'Error'

        """
        baseurl = self.settings['settings']['api']['url']['route']
        try:
            url = baseurl + 'fromStation=' + startstation + '&toStation=' + endstation
        except (TypeError, AttributeError, ValueError):
            return 'Error'
        else:
            data = self.sendcall(url)
            return data

    def sendcall(self, url):
        """
        Make an api call and return it's data

        :param url: the url to make the call
        :return: An ordered dictonary with the data

        >>> apimanager = ApiManagement()

        Since the api return data is different every time we can only test the type
        >>> type(apimanager.sendcall('https://webservices.ns.nl/ns-api-avt?station=Utrecht centraal')) is collections.OrderedDict
        True

        This will throw an error because one of them is not a string
        >>> apimanager.sendcall(0)
        'error'

        This will throw an error because one of them is not a string
        >>> apimanager.sendcall((1, 2, 3))
        'error'

        This will throw an error because one of them is not a string
        >>> apimanager.sendcall(['as','test'])
        'error'

        This will throw an error because one of them is not a string
        >>> apimanager.sendcall({'test': 'test','aap':'aap'})
        'error'

        his will throw an error because one of them is not a string
        >>> apimanager.sendcall({'test','test','aap','aap'})
        'error'

        """

        username = self.settings['settings']['api']['auth']['username']
        password = self.settings['settings']['api']['auth']['password']
        try:
            r = req.get(url, auth=(username, password))
            r.raise_for_status()
        except req.exceptions.HTTPError as e:
            # print("Http Error: ", e) #dev mode
            return 'error'
        except req.exceptions.ConnectionError as e:
            # print("Error Connecting: ", e) #dev mode
            return 'error'
        except req.exceptions.Timeout as e:
            # print("Timeout Error: ", e) #dev mode
            return 'error'
        except req.exceptions.RequestException as e:
            # print("RequestException error: ", e) #dev mode
            return 'error'
        except (TypeError, AttributeError, ValueError) as e:
            # print("type, value or atribute error: ", e) #dev mode
            return 'error'
        else:
            dataasdict = xmltodict.parse(r.text)
            if 'error' in dataasdict.keys():
                return 'error'
            else:
                return dataasdict


# When the file is ran from itself, it will be doctested
if __name__ == '__main__':
    import doctest
    doctest.testmod()

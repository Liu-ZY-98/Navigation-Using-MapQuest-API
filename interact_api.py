import json
import urllib.parse
import urllib.request

MAPQUEST_API_KEY = '8MvqeOLdGZdj92HTGRsmY6QrbPy1jD8y'
BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2'
BASE_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1'


def build_route_url() -> str:
    '''
    This function asks the user for the number of locations that the user
    wants, and builds and returns a string of URL that will be connecting to
    MapQuest Route to get all the data.
    '''
    
    num_of_locations = int(input())
    query_parameters = _enter_locations(num_of_locations)
    return BASE_MAPQUEST_URL + '/route?' + urllib.parse.urlencode(query_parameters)


def get_result(url: str) -> dict:
    '''
    This function takes a URL and returns a Python dictionary representing the
    parsed JSON response.
    '''
    
    response = None
    try:
        response = urllib.request.urlopen(url)
        return json.load(response)

    finally:
        if response != None:
            response.close()


def build_elev_url(lati: float, long: float) -> str:
    '''
    This function takes the latitude and longitude data from MapQuest Route, and
    builds and returns a URL that will be connecting to MapQuest Elevation to
    get all the data there.
    '''
    
    query_parameters = [
        ('key', MAPQUEST_API_KEY),('shapeFormat', 'raw'),
        ('latLngCollection',str(lati) + ',' + str(long))]
    return BASE_ELEVATION_URL + '/profile?' + urllib.parse.urlencode(query_parameters)


def get_elev_result(url: str) -> dict:
    '''
    This function takes a URL and returns a Python dictionary representing the
    parsed JSON response.
    '''
    
    response = None
    try:
        response = urllib.request.urlopen(url)
        return json.load(response)

    finally:
        if response != None:
            response.close()

            
def _enter_locations(location_num: int) -> list:
    '''
    This function takes the number of locations the user wants, and builds and
    returns a list of query parameters needed for building an URL.
    '''
    
    inputs = 0
    query_parameters = [('key', MAPQUEST_API_KEY)]
    while inputs < location_num:
        if inputs == 0:
            query_parameters.append(('from', input()))
            inputs += 1
        else:
            query_parameters.append(('to', input()))
            inputs += 1
    return query_parameters
        


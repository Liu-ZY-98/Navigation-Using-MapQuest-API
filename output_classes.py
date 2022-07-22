import interact_api

METER_TO_FEET_CONSTANT = 3.2808399

class Steps:
    'print out the directions'
    
    def get_info(self, url_result: dict) -> None:
        print('DIRECTIONS')
        for leg in url_result['route']['legs']:
            for maneuver in leg['maneuvers']:
                print(maneuver['narrative'])
        print()


class LatLong:
    'print our the latitude and longitude'
    
    def get_info(self, url_result: dict) -> None:
        print('LATLONGS')
        for location in url_result['route']['locations']:
            long = '{0:.2f}'.format(location['latLng']['lng'])
            lati = '{0:.2f}'.format(location['latLng']['lat'])
            print(_lati_long(lati, long))
        print()


class TotalDistance:
    'print out the total distance'
    
    def get_info(self, url_result: dict) -> None:
        print('TOTAL DISTANCE: ' + '{0:.0f}'.format(
            url_result['route']['distance']) + ' miles')
        print()


class TotalTime:
    'print out the total time'
    
    def get_info(self, url_result: dict) -> None:
        total_time = 0
        for leg in url_result['route']['legs']:
            total_time += leg['time']
        print('TOTAL TIME: ' + '{0:.0f}'.format(
            total_time/60) + ' minutes')
        print()


class Elevation:
    'print out the elevation'
    
    def get_info(self, url_result: dict) -> None:
        print('ELEVATIONS')
        for location in url_result['route']['locations']:
            lati = location['latLng']['lat']
            long = location['latLng']['lng']
            elev_result = interact_api.get_elev_result(
                interact_api.build_elev_url(lati,long))
            print(_get_elev_in_ft(elev_result))
        print()

def _lati_long(lati: str, long: str) -> str:
    '''
    This function takes the latitude and longitude which are already formatted
    to the second decimal, and returns them with direction letters.
    '''
    
    if float(long) <= 0:
        if float(long) < 0:
            long = long[1:] + 'W'
        else:
            long = long + 'W'
    elif float(long) > 0:
        long = long + 'E'
    if float(lati) < 0:
        lati = lati[1:] + 'S'
    elif float(lati) >= 0:
        lati = lati + 'N'
    return lati + ' ' + long


def _get_elev_in_ft(url_result: dict) -> str:
    '''
    This function takes the parsed JSON response of MapQuest Elevation, and
    gets the elevation in meters, and returns the elevation that is converted
    to feet.
    '''
    
    elev_m = url_result['elevationProfile'][0]['height']
    elev_ft = elev_m * METER_TO_FEET_CONSTANT
    return '{0:.0f}'.format(elev_ft)



    

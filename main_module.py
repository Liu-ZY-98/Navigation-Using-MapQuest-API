import interact_api
import output_classes
import urllib
import socket

def _user_input() -> list:
    'return a list of commands that the user wants the output to be'
    
    num_of_outputs = int(input())
    list_of_inputs = _build_user_input_list(num_of_outputs)
    return list_of_inputs

def _create_dictionary() -> dict:
    '''
    This function will create and return a dictionary, with its keys being
    the user's commands and values being the corresponding classes in
    output_classes.py.
    '''
    
    outputs = {'LATLONG': output_classes.LatLong(),
               'STEPS': output_classes.Steps(),
               'TOTALTIME': output_classes.TotalTime(),
               'TOTALDISTANCE': output_classes.TotalDistance(),
               'ELEVATION': output_classes.Elevation()}
    return outputs


def _build_user_input_list(num_of_outputs: int) -> list:
    '''
    The function takes the number of outputs the user want to have, and asks
    the user for that number of outputs, then returns it in a list.
    '''
    
    user_input_list = []
    inputs_num = 0
    while inputs_num < num_of_outputs:
        inputs = input()
        user_input_list.append(inputs)
        inputs_num += 1
    return user_input_list

def _main_function() -> None:
    '''
    This function asks the user and prints out the outputs that the user
    expects.
    '''
    
    route_url_result = interact_api.get_result(interact_api.build_route_url())
    list_of_inputs = _user_input()
    class_dictionary = _create_dictionary()
    try:
        # Set a variable to a random item in the route_url_result.
        # If the route does not exist, it will give an exception
        # which will be handled without calling the classes.
        test_route = route_url_result['route']['legs']
            
        print()
        for inp in list_of_inputs:
            class_dictionary[inp].get_info(route_url_result)
        print('Directions Courtesy of MapQuest;' +
                ' Map Data Copyright OpenStreetMap Contributors')
    except KeyError:
        print('\nNO ROUTE FOUND')

if __name__ == '__main__':
    try:
        _main_function()
    except urllib.error.HTTPError:
        print('\nMAPQUEST ERROR')
    except socket.gaierror:
        print('\nMAPQUEST ERROR')
    except urllib.error.URLError:
        print('\nMAPQUEST ERROR')

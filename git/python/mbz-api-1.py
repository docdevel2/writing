import json
import os
import urllib.request
import webbrowser
import pprint


# Justice's Groove URL
api_url = 'https://musicbrainz.org/ws/2/recording/b97670e0-08fe-42fe-af39-7367a710c299?&fmt=json'

def mbz_recording(api_url):
    
    request = urllib.request.Request(api_url)
    print('request.type: ', request.type)
    print('request.host: ', request.host)
    print('request.get_method(): ', request.get_method())
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode("utf-8"))
        statcode = response.status
    
    # Pretty Print 
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)
    #
    print('Print response status:\n', statcode)
    webbrowser.open_new_tab(api_url)

    return

def use_urllib(api_url):
    # This function was used as the model for the mbz_recording() function.
    
    request = urllib.request.Request(api_url)
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode("utf-8"))
        photo_url = data['url']
        print('\nphoto_url: ', photo_url)
        #print('Commented out "webbrowser.open_new_tab"')
        webbrowser.open_new_tab(photo_url)

    return

mbz_recording(api_url)

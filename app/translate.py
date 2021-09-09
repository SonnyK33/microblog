import json
import requests
from app import app

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config:
        return ('not in config file')
    if not app.config['MS_TRANSLATOR_KEY']:
        print(app.config['MS_TRANSLATOR_KEY'])
        print(app.config['LANGUAGES'])

        return ('Error: the translation  is not configured')

    auth = {
        'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
        'Ocp-Apim-Subscription-Region': 'eastus2'}
    r = requests.post(
        'https://api.cognitive.microsofttranslator.com'
        '/translate?api-version=3.0&from={}&to={}'.format(
            source_language, dest_language), headers=auth, json=[{'Text': text}])
    
    if r.status_code != 200:
        print(r.status_code)
        return ('Error: the translation service failed')
    print(r)
    print('test')
    return r.json()[0]['translations'][0]['text']
        
    

    
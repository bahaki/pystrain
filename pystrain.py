import requests

class Wrapper:
    def __init__(self):
        self.url = 'https://en.seedfinder.eu/api/json/'

    def request_data(self, path, params):
        response = requests.get(self.url + path, params = params)
        return response

class Breeders(Wrapper):
    def __init__ (self, breeders, show_strains = False):
        super().__init__()
        params = {}
        if breeders:
            separator = '|'
            params['br'] = '|'.join(breeders)
        params['strains'] = int(show_strains)
        
        self.breeders = self.request_data('ids.json', params)
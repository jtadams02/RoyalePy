import requests


BASE_URL = "https://api.clashroyale.com/v1/"

PLAYERS = "players/%23"


class ClashAPI(object):

    def __init__(self):
        """
        Basic Constructor. Should not be used at all!
        """
        # If no API key is provided we will have to ask for one?
        self.key = None

    def __init__(self,api_key):
        """
        This is the only object constructor that should ever be called!
        """
        self.key = api_key
        self.h = {'Authorization' : 'Bearer {}'.format(self.key)}







    

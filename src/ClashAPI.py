import requests

BASE_URL = 'https://api.clashroyale.com/v1/'
PLAYERS_URL = "players/%23"

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
    
    def get_player_basic(self,player_id):
        """ This method will handle grabbing a players information

        Args:
            player_id (str): Argument will be a string of the userID
        """
        
        # First thing we need to do is handle the input incase it starts with 
        
        # Now we can make the request
        response = requests.get(BASE_URL+PLAYERS_URL+player_id,headers=self.h)
        
        
        







    

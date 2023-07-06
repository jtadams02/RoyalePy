import requests
import helper

BASE_URL = 'https://api.clashroyale.com/v1/'
PLAYERS_URL = "players/%23"
CARDS_URL = 'cards/'

class ClashAPI(object):


    def __init__(self,api_key):
        """This is the only constructor. It will take an API key and test its validity. If it is not valid, it will throw an error

        Args:
            api_key (str): String API key

        Raises:
            ConnectionError: I didn't really know what error to use cuz I'm new but I like this one
        """
        self.key = api_key
        self.h = {'Authorization' : 'Bearer {}'.format(self.key)}

        # We're going to test the API key and throw an error if it does not work
        # Just going to request the cards
        test_request = requests.get(BASE_URL+CARDS_URL,headers=self.h)
        if not test_request:
            raise ConnectionError("API Key is not valid")
        else:
            print("Success")

        

    # TODO: Add some error handling
    def get_player_basic(self,player_id):
        """ This method will handle grabbing the very basics of a users profile from the Clash Royale API


        Args:
            player_id (str): Argument will be a string of the userID. This can start with # or not

        Returns:
            Will return a dictionary with only certain 
        """
        
        # First thing we need to do is handle the input incase it starts with 
        if player_id.startswith("#"):
            player_id = player_id[1:]
        
        # I'm also going to make an empty dictionary right here
        d = {}
        
        # Now we can make the request
        response = requests.get(BASE_URL+PLAYERS_URL+player_id,headers=self.h)
        
        
        if response:
            # Format the response into a json format so we can use it
            json_data = response.json()
            d['tag'] = json_data['tag']
            d['name'] = json_data['name']
            d['trophies'] = json_data['trophies']
            # Handle clan checking
            if json_data['clan']:
                d['clan_name'] = json_data['clan']['name']
            else:
                d['clan'] = "null"
            
            if json_data['currentPathOfLegendSeasonResult'] == 'null':
                d['league'] = "null"
            else:
                d['league'] = helper.league_translator(json_data['currentPathOfLegendSeasonResult']['leagueNumber'])

            if d['league'] == 'Ultimate Champion':
                d['uc_trophies'] = json_data['currentPathOfLegendSeasonResult']['trophies']
            else:
                d['uc_trophies'] = "null"
            
            return d
        else:
            print('invalid')
            if response.status_code == 403:
                # When the status code is of code 403, I believe raising an error is the best idea because it means something is severely wrong
                raise ConnectionError("API Key is not valid, or your IP does not match with the API allowance")
            elif response.status_code == 404:
                # Error 404 means that the user is probably not found
                # Not sure what to return here. Maybe just the empty dict?
                return d
        


 
    
                
            
            
        
        
        
        







    

# RoyalePy <sub>V0.1</sub>

RoyalePy is my attempt at learning how to handle querying APIs and what an API Wrapper does. And I want to publish my first Python Package so this is a great one to try!
  
The [Clash Royale API](https://developer.clashroyale.com/#/) is a very simple API, which makes it a great place for me to start learning.  
Along with that, I happen to be addicted to the game so why not make something for a game I enjoy?  

My goal for this API Wrapper is to allow newbies like me able to make Clash Royale tools easily if they desire too. My goal is to simplify requests and returns. Even the basic requsts return hundreds of lines of data a new developer would have to sift through, so I hope ease the work of all of that by doing it myself.  

  ## Requirements: 

  So far, the only package I am using is the requests package. If this is not installed, please install with the following:  
  
  ``pip install requests``  

  Until I publish this to [PyPi](https://pypi.org/), you will also need to manually download ``RoyalePy.py`` and import the ClashAPI() object like so:  

  ``from RoyalePy import ClashAPI`` 

  ## Usage:  

  When initializing the ClashAPI() object, it will require that you put an api_key as its one argument. If your key is not valid it will throw an error. Click the link above to get your key.  
    
  ```
  from RoyalePy import ClashAPI
  
  api = ClashAPI(api_key)
  ```  
      
  In V0.1, there is only 1 main function that is usable, that is:  
    
  ``get_player_basic(tag)``
  - Summary: This grabs just the bare minimum of information about a player. There will be multiple ``get_player_####`` functions eventually. This shows how simple I am trying to make this for new users. There will be a lot more data in future functions
  - Args: This function takes 1 argument, which is the ID tag of the Clash Royale Player. This argument can contain the '#' that preceeds the ID or it can be removed. Both inputs work
  - Returns: This returns a shortened dictionary of the JSON response with only a few details. The setup of this dictionary is displayed below:
    - ``['tag']`` Which contains the ID tag of the player. This will be the same as the ID passed as the argument, but this will have a '#' in front of it
    - ``['name']`` Which contains the username of the player
    - ``['trohpies']`` Which contains an integer count of the players current trophies
    - ``['clan_name']`` Which contains the name of the clan a user is in. If they are not in a clan, this will have a value of None. I suggest checking to see if the user is in a clan and changing how you use this response
    - ``['league']`` Which will contain the name of the league the user is in
    - ``['uc_trophies']`` Which will contain the current trophies of the user IF they are in league 10. If they are not, this will be None
    
  I will add more features obviously as time goes on and the documentation will be held in the ``docs/`` folder on this repository.  
  I hope this helps you!

  
    
  

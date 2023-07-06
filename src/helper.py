       
def league_translator(league_num):
    """This function is just a helper to translate the league number to a name

    Args:
        league_num (int): the league number
    """

    # This is just going to be a gigantic if-else thing so this is gonna be fun

    if league_num == 1:
        return "Challenger I"
    elif league_num == 2:
        return "Challenger II"
    elif league_num == 3:
        return "Challenger III"
    elif league_num == 4:
        return "Master I"
    elif league_num == 5:
        return "Master II"
    elif league_num == 6:
        return "Master III"
    elif league_num == 7:
        return "Champion"
    elif league_num == 8:
        return "Grand Champion"
    elif league_num == 9:
        return "Royal Champion"
    else:
        return "Ultimate Champion"
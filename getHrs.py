# getHrs.py
# Creator: Robert Toribio
# Date: 10/28/2021


import statsapi
from datetime import date
import re

def totalhrsToday(all_hrs):
    total_hrs = 0
    for element in all_hrs:
       total_hrs +=  int(element[1])
    return total_hrs


def getGames(date):
    game_ids = []
    gamesToday = statsapi.schedule(date)

    for game in gamesToday:
        game_ids.append(game['game_id'])
    return game_ids


def getTodaysHr(game_ids):
    all_hrs = []
    my_keys = ["namefield",'hr']
   
    for game_id in game_ids:
    

        box_scoredata = statsapi.boxscore_data(game_id)
        playerHr_list_away = []
        playerHr_list_home = []

        for d in box_scoredata["homeBatters"]:
            playerHr_list_home.append( {my_key: d[my_key] for my_key in my_keys})
        
        team_name_home = playerHr_list_home[0]["namefield"].replace(" Batters", "")
        del playerHr_list_home[0]
    
        for d in box_scoredata["awayBatters"]:
            playerHr_list_away.append( {my_key: d[my_key] for my_key in my_keys})

        team_name_away = playerHr_list_away[0]["namefield"].replace(" Batters","")
        del playerHr_list_away[0]
  
        for element in playerHr_list_home:
            if element['hr']  != '0' :
                all_hrs.append ([element['namefield'],element['hr'],team_name_home])
  
    
        for element in playerHr_list_away:
            if element['hr']  != '0':
                all_hrs.append ([element['namefield'],element['hr'], team_name_away])
    strip(all_hrs)
    return all_hrs


def strip(all_hrs):
  for element in all_hrs:
      for i in range(len(element)):
          if i == 0:
             element[i] = element[i].replace("b-", " ")
             element[i] = element[i].replace("a-", " ")
             pattern = r'(?:(?<=^)|(?<=[^.]))\s+([A-Z][a-z\u00C0-\u00FF]+)'
             x = re.findall(pattern,element[i])
             element[i] = " ".join(x)
           
           
            
def main():
    game_ids = getGames("10/30/2021")
    all_hrs = getTodaysHr(game_ids)
    for player in all_hrs:
        print(player[0])
    #strip(all_hrs)
    print(all_hrs)
    print(totalhrsToday(all_hrs))
    
if __name__ == "__main__":
    main()

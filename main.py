import random
import time

import requests

import starwars as sw

your_score = 0
rival_score = 0

#Game Introduction and rules
print('Welcome to Top Trumps!')
time.sleep(1.5)
print('The first player to win three points is the winner!')
time.sleep(1.5)
print("To win a point, you must pick a stat of the random character given to you.")
time.sleep(1.5)
print("If your chosen stat is higher than the rival's stat, you win the round.")
time.sleep(1.5)
print("If your chosen stat is lower than the rival's, you will lose the round.")
time.sleep(2)

# Store the player's name for the high score file
name = input('What is your name? ')

#choosing the API
round_type = input("Which card deck would you like to use? (pokemon or star wars) ")
round_type = round_type.lower()  #Convert the input to lowercase

#assigns random pokemon from pokeapi
def random_pokemon (): 
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
'name': pokemon['name'],
'id': pokemon['id'],
'height': pokemon['height'],
'weight': pokemon['weight'],
'health': pokemon['stats'][0]['base_stat'],
'attack': pokemon['stats'][1]['base_stat'],
'defence': pokemon['stats'][2]['base_stat']
}
 
#assigns random character from star wars API
def random_starwars ():
  player_card_id = random.randint(1, 83)  # Random Card ID given to player
  while (player_card_id == 17):  # 17 does not have any content
      player_card_id = random.randint(1, 83)  # Random Card ID given to player
  print("Getting a card ready...\n")  # The Star Wars APi is slower than the others
  player_card = sw.get_character_stats(player_card_id)
  return player_card

#main body of pokemon game
def pokemon_round():
    print('New Round! \n')
    my_pokemon = random_pokemon()
    time.sleep(1)
    print('{} you have been given {}. \n'.format(name,my_pokemon['name']))
    print("Player Top Trumpz Card Stats are: \nName: {}, id: {}, Height {}m, Weight {}kg, Health {}, attack {}, defence {}\n".format(
        my_pokemon["name"], my_pokemon["id"], (my_pokemon["height"]/10), (my_pokemon["weight"]/10), (my_pokemon["health"]),
        my_pokemon["attack"], my_pokemon["defence"]))
    stat_choice = input('Which stat would you like to use? (id, height, weight, health, attack, defence) ')
    stat_choice = stat_choice.lower() #changes stat choice to lowercase
  
    print(stat_choice)

    opponent_pokemon = random_pokemon()
    if my_pokemon == opponent_pokemon:
        opponent_pokemon = random_pokemon()
    time.sleep(2)
    print('Your rival has been given {}'.format((opponent_pokemon['name']).capitalize()))
    time.sleep(2)
    my_stat = my_pokemon[stat_choice]
    print('Your {} stat is {}'.format(my_pokemon['name'], my_stat))
    opponent_stat = opponent_pokemon[stat_choice]
    time.sleep(2)
    print("Your rival's {} stat is {} \n".format((opponent_pokemon['name']), opponent_stat))
    time.sleep(2)

    if my_stat > opponent_stat:
        print('You win!\n')
        won_round = 1
    elif my_stat < opponent_stat:
        print('You lose!\n')
        won_round = -1
    else:
        print('Its a draw!\n')
        won_round = 0

    return won_round

#main body of star wars game
def starwars_round():
    print('New Round! \n')
    my_character = random_starwars()
    time.sleep(1)
    print('{} you have been given {}'.format(name,my_character['name']))
    print("Player Top Trumpz Card Stats are: \nName: {}, ID: {}, Height {}cm, Weight {}kg, No. of films {}\n".format(
        my_character["name"], my_character["id"], my_character["height"], my_character["weight"], my_character["films"]))
    stat_choice = input('Which stat would you like to use? (id, height, weight, films) ')
    stat_choice = stat_choice.lower() #changes stat choice to lowercase
    print(stat_choice)

    opponent_character = random_starwars()
    if my_character == opponent_character:
        opponent_character = random_starwars()
    time.sleep(2)
    print('Your rival has been given {}'.format(opponent_character['name']))
    time.sleep(2)
    my_stat = my_character[stat_choice]
    print('Your {} stat is {}'.format(my_character['name'], my_stat))
    opponent_stat = opponent_character[stat_choice]
    time.sleep(1)
    print("Your rival's {} stat is {} \n".format(opponent_character['name'], opponent_stat))
    time.sleep(2)
  
    #decides who won round
    if my_stat > opponent_stat:
        print('You win!\n')
        won_round = 1
    elif my_stat < opponent_stat:
        print('You lose!\n')
        won_round = -1
    else:
        print('Its a draw!\n')
        won_round = 0

    return won_round

rounds_to_win = 3 #First to 3 wins the game.

while (your_score < rounds_to_win) and (rival_score < rounds_to_win):
  if round_type == 'pokemon':
    result = pokemon_round() # Get the result of the round
    if result > 0 : # If the player won
        your_score +=1 # Increase their score
    elif result < 0:
        rival_score +=1
  else:
    result = starwars_round() # Get the result of the round
    if result > 0: # If the player won
        your_score +=1 # Increase their score
    elif result < 0:
        rival_score += 1

  print('{} your score is {}'.format(name,your_score))
  print("Your rival's score is {} \n".format(rival_score))
  

highscore_data = ("{}'s total score is {}".format(name, your_score))
print(highscore_data)



#Congratulate the player on winning the game
if your_score == rounds_to_win:
    print("Congratulations! You've won the game!")
  
#Tell the player they have lost the game
elif rival_score == rounds_to_win: 
  print("You have lost the game! Better luck next time!")

#Add high score to text file
with open('highscore.txt', 'a') as highscore_file:
    highscore_data = ("{}'s total score is {}\n".format(name, your_score))
    highscore_file.write(highscore_data)
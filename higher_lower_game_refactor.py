import os
import functions as f

from random import shuffle
from art import logo
from game_data import data


game_score = 0
held_dict = {}
playing = True

while playing:
    os.system('cls')
    print(logo)

    if held_dict:
        print(f"\nCorrect! Your score is: {game_score}\n\n")
        shuffle(data)
        game_objects = f.pick_objects(data, held_dict)
        game_objects[0] = held_dict
    else:
        shuffle(data)
        game_objects = f.pick_objects(data, held_dict)

    object_dictionary = f.get_object_info(game_objects)
    game_dictionary = f.create_game_dict(object_dictionary)

    if f.compare_player_choice(game_dictionary):
        game_score += 1
        held_dict = game_dictionary[1]
    else:
        print("\n\nIncorrect!")
        print(f"\nYour final score is {game_score}.\n\nThanks for playing!")

        play_again = input("\nPlay again? y/n ")
        if play_again.lower() == 'y':
            game_score = 0
            held_dict = {}
            continue
        else:
            playing = False

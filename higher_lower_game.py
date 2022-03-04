import os

from random import choice, choices

from art import logo
from game_data import data


def pick_objects(list_of_objects):
    """
    Picks two items from a data set at random. Returns a list of those items.
    Prevents identical objects from being picked.
    """
    objects = choices(list_of_objects, k=2)
    while objects[0] == objects[1]:
        objects = choices(list_of_objects, k=2)
    return objects


def get_object_info(list_of_objects):
    """
    Takes a list of two objects and prints a descriptive statement about them.
    Returns name and follower_count for object_a and object_b as a list of dictionaries.
    """
    object_a = list_of_objects[0]
    object_a_name = list_of_objects[0]['name']
    object_a_followers = list_of_objects[0]['follower_count']

    object_b = list_of_objects[1]
    object_b_name = list_of_objects[1]['name']
    object_b_followers = list_of_objects[1]['follower_count']

    print("Who has more Instagram followers:\n")
    print(f"A: {object_a['name']}, a(n) {object_a['description'].lower()} from {object_a['country']}.")
    print("\nOR\n")
    print(f"B: {object_b['name']}, a(n) {object_b['description'].lower()} from {object_b['country']}.")

    object_a_dict = {'object': 'a', 'name': object_a_name, 'followers': object_a_followers}
    object_b_dict = {'object': 'b', 'name': object_b_name, 'followers': object_b_followers}

    list_of_dictionaries = [object_a_dict, object_b_dict]

    return list_of_dictionaries


def hold_lower_followers(list_of_dictionaries):
    """Compare the follower_count of two dictionaries, then stores the lower to a variable."""
    if list_of_dictionaries[0]['followers'] > list_of_dictionaries[1]['followers']:
        held_object = list_of_dictionaries[1]
        held_object['object'] = 'a'
    else:
        held_object = list_of_dictionaries[0]
        held_object['object'] = 'a'
    return held_object


def create_game_dict(list_of_dictionaries):
    """Adds a player's choice to the list of object dictionaries."""
    player_dict = {}

    player_choice = input("Guess A or B: ")
    if player_choice.lower() == 'a':
        player_dict = list_of_dictionaries[0]
    elif player_choice.lower() == 'b':
        player_dict = list_of_dictionaries[1]

    player_dict_copy = player_dict.copy()
    list_of_dictionaries.append(player_dict_copy)
    return list_of_dictionaries


def compare_player_choice(game_dict):

    if game_dict[2] == game_dict[0] and game_dict[0]['followers'] > game_dict[1]['followers']:
        print("\nCorrect!")
        return True
    elif game_dict[2] == game_dict[1] and game_dict[1]['followers'] > game_dict[0]['followers']:
        print("\nCorrect!")
        return True
    else:
        print("\nIncorrect choice!")
        return False


print(logo)
game_score = 0
held_object = {}
playing = True

while playing:
    game_objects = pick_objects(data)
    object_dictionary = get_object_info(game_objects)
    game_dictionary = create_game_dict(object_dictionary)

    if compare_player_choice(game_dictionary):
        game_score += 1
        print(f"Your score is {game_score}.\n")
    else:
        print(f"\nYour final score is {game_score}.\nThanks for playing!")
        playing = False

    held_object = hold_lower_followers(object_dictionary)




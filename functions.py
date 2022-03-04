from random import choice, choices, shuffle

from art import logo, vs


def pick_objects(list_of_objects, held_dictionary):
    """
    Pops two items from a data set at random. Returns a list of those items.
    Prevents identical objects from being picked.
    """
    objects = choices(list_of_objects, k=2)

    while held_dictionary == objects[1]:
        objects[1] = choice(list_of_objects)

    while objects[0] == objects[1]:
        objects = choices(list_of_objects, k=2)

    return objects


def get_object_info(list_of_objects):
    """
    Takes a list of two objects and prints a descriptive statement about them.
    Returns name and follower_count for object_a and object_b as a list of dictionaries.
    """
    object_a_dict = list_of_objects[0]
    object_a_dict['object'] = 'a'

    object_b_dict = list_of_objects[1]
    object_b_dict['object'] = 'b'

    print("Who has more Instagram followers:\n")
    print(f"A: {object_a_dict['name']}, a(n) {object_a_dict['description'].lower()} from {object_a_dict['country']}.")
    print(f"\n{vs}\n")
    print(f"B: {object_b_dict['name']}, a(n) {object_b_dict['description'].lower()} from {object_b_dict['country']}.")

    list_of_dictionaries = [object_a_dict, object_b_dict]

    return list_of_dictionaries


def create_game_dict(list_of_dictionaries):
    """Adds a player's choice to the list of object dictionaries."""
    selected_dict = {}

    player_choice = input("\nGuess A or B: ")
    if player_choice.lower() == 'a':
        selected_dict = list_of_dictionaries[0]
    elif player_choice.lower() == 'b':
        selected_dict = list_of_dictionaries[1]

    selected_dict_copy = selected_dict.copy()
    list_of_dictionaries.append(selected_dict_copy)
    return list_of_dictionaries


def compare_player_choice(game_dict):
    if game_dict[0]['follower_count'] > game_dict[1]['follower_count']:
        return game_dict[0] == game_dict[2]
    else:
        return game_dict[1] == game_dict[2]
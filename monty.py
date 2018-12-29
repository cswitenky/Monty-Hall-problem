"""
file: monty.py
language: python3.7
author cswitenky@mail.rit.edu connor switenky

description: A probability puzzle based on the television game show
Let's Make a Deal. In this problem, Monty Hall, the host of the show, gives you
the choice of three doors. Only one door has a car behind it, another two have
goats. Let's say you pick the door number one, and the host knows what behind
the doors, opens door number two that does not have a goat. Would you change
your pick to three or remain with one? This simulation proves that you that you
DO have a better chance of winning if you change to
door number three (approx. 2/3 chance) than it is to remain with
door number 1 (approx. 1/3 chance). In this simulation, you have options to
choose # of doors, # of tests, and whether you want to always change your
pick to the remaining door or not.
"""
from dataclasses import dataclass
import random


@dataclass
class Door:
    id: int
    goat: bool


def generate_doors(int):
    """
    function: generate a set of doors with only one door without a goat
    :param int: the amount of doors
    :return: a set of doors
    """
    target, doors = random.randint(0, int-1), []
    for idx in range(0, int):
        if idx != target:
            doors += [Door(idx, True)] # has a goat
        elif idx == target:
            doors += [Door(idx, False)] # has a car
    return doors


def open_doors(pick, doors):
    """
    function: returns with only two choices: an user chosen door or change to a
    remaining door
    :param pick: user's chosen door's id
    :param doors: a set of doors
    :return: an user chosen door and a remaining door
    """
    picked_door, remaining_door, correct_door = None, None, None

    for door in doors:
        if door.goat == False:
            if pick == door.id:
                remaining_door = doors[random.randint(0, len(doors)-1)]
            else:
                remaining_door = door
            correct_door = door
        if pick == door.id:
            picked_door = door

    if picked_door != None and remaining_door != None and correct_door != None:
        return picked_door, remaining_door, correct_door


def play(doors_count, change):
    """
    function: perform a test with a given set of doors and option to change
    :param doors_count: the amount of doors
    :param change: boolean value on whether to change the pick or not
    :return: boolean value states whether the choice is a winning or losing move
    """
    doors = generate_doors(doors_count)

    pick = random.randint(0, doors_count-1)

    picked_door, remaining_door, correct_door = open_doors(pick, doors)

    if change:
        pick = remaining_door.id

    if correct_door.id == pick:
        return True
    else:
        return False


def test(tries, doors, change):
    """
    function: performs # of tests
    :param tries: the amount of tests to perform
    :param doors: the amount of doors
    :param change: boolean value on whether to change the pick or not
    :return: # of wins and attempts,
    chance = wins / attempts %
    """
    wins, attempts = 0, 0
    for idx in range(tries):
        result = play(doors, change)
        if result:
            wins += 1
        attempts += 1

    chance = str(round((wins/attempts)*100)) + "%"
    return wins, attempts, chance


def check(integer):
    """
    function: check whether a given integer is greater than 0
    :param integer: a given integer
    :return: ignore if correct, and raise an error if incorrect
    """
    if int(integer) > 0:
        pass
    else:
        raise IndexError(str(integer) + " is less than 0. The integer must" \
                                        " be greater than 0.")


def main():
    """
    function: The main function that interacts with the user.
    :return: n/a
    """

    while True:
        print("\nInput blank to quit.\n")
        # get a number of doors
        doors = input("How many doors would you like to have? (N>0) ")
        if doors == "":
            break
        check(doors) # validate the input

        # get a number of tries
        tries = input("How many tries would you like to execute? (N>0) ")
        if tries == "":
            break
        check(tries) # validate the input

        # change?
        change = input("Would you like to change your pick? (Y/N) ")
        if change == "":
            break
        # validate the input
        if change.upper() == "Y" or change.upper() == "YES":
            change = True
        elif change.upper() == "N" or change.upper() == "NO":
            change = False
        else:
            raise RuntimeError(change + " is an invalid input.")

        wins, attempts, chance = test(int(tries), int(doors), change)

        print("\nYou won", wins, "time(s) out of", attempts, "attempt(s).")

        if change:
            print("\nIf you change your pick, the chances of you winning is", \
                  chance + ".")
        else:
            print("\nIf you refuse to change your pick, " \
                  "the chance of you winning is", chance + ".")

        print("\nStarting over.")


if __name__ == '__main__':
    main()
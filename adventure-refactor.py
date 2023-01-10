import time
import random
ammunition = []
creatures = ["Dragon", "Troll", "Pirate", "Gorgon",
             "Wicked Fairie", "Monster"]
creature = random.choice(creatures)


def print_pause(message_passed):
    print(message_passed)
    time.sleep(2)


def field():
    knock_peer = input("Enter 1 to knock on the door of the house. \n"
                       "Enter 2 to peer into the cave. \n"
                       "What would you like to do? \n"
                       "(Please enter 1 or 2) \n")
    if knock_peer == '1':
        house()
        fight()
    elif knock_peer == '2':
        cave()
    else:
        print_pause("Enter 1 or 2")
        field()


def intro():
    global creature
    creature = random.choice(creatures)
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a {} is somewhere around here, "
                "and has been terrifying the nearby "
                "village..".format(creature))
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                " (but not very effective) dagger.")


def fight():
    fight_run = input("Would you like to (1) fight or (2) run away? \n")
    if fight_run == '1':
        if 'sword' in ammunition:
            print_pause("As the {} moves to attack, you unsheath "
                        "your new sword.".format(creature))
            print_pause("The Sword of Ogoroth shines brightly in your"
                        " hand as you brace yourself for the attack.")
            print_pause("But the {} takes one look at your shiny "
                        "new toy and runs away!".format(creature))
            print_pause("You have rid the town of the {}. "
                        "You are victorious!".format(creature))
        else:
            print_pause("You feel a bit under-prepared for this,"
                        " what with only having a tiny dagger.")
            print_pause("You do your best...")
            print_pause("but your dagger is no match "
                        "for the {}.".format(creature))
            print_pause("You have been defeated!")
        play_again = input("Would you like to play again? (y/n) \n")
        if 'y' in play_again:
            print_pause("Excellent! Restarting the game ...")
            ammunition.clear()
            intro()
            field()
        elif 'n' in play_again:
            print_pause("Thanks for playing! See you next time")

    elif fight_run == '2':
        print_pause("You run back into the field."
                    " Luckily, you don't seem to have been followed.")
        field()


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                "and out steps a {}.".format(creature))
    print_pause("Eep! This is the {}'s house!".format(creature))
    print_pause("The {} attacks you!".format(creature))


def cave():
    if 'sword' in ammunition:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the"
                    " good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        field()
    else:
        ammunition.append("sword")
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take"
                    " the sword with you.")
        print_pause("You walk back out to the field. \n")
        field()


def play_game():
    intro()
    field()


play_game()

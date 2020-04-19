# Rawley Moyer
# Integration Project-Pycharm
# This is Dragon Realm. An adventure game where you pick your own journey.

def main():
    print("Welcome to my integration project!")
    name = input("What is your name, traveler? ")
    print("Hello, " + name)

    # Dragon Realm

    # Defining distances used in this game using arithmetic

    lives = 3
    score = 0
    level = 1
    while lives > 0:

        # Creating List
        # Rucksack prints all materials
        rucksack = ["sword", "armor", "potion", "firewood", "flint", "Rope"]
        # #Intro
        choice_1 = input("Would you like to go on a quest? (yes/no) ", )
        if choice_1 == "yes":
            print("Excelsior")

            choice_2 = input("Would you like to go left or right?, ", )
            if choice_2 == "right":
                print("Good Choice you avoided that pesky quick-sand")
                choice_3 = int(input("How many Furlong's would you like to go before resting? "))
                while choice_3 >= 3:
                    print("You're a sturdy one")
                    print()
                    print("Unfortunately you find yourself walking into a herd of sorcerers")
                    print()
                    print("Thank goodness you remembered your trusty bag of help.")
                    print("However, there are many evil wizards")
                    print()
                    choice_4 = input("Do you wish to sneak away or fight? ")
                    if choice_4 == "fight":
                        print("Take a look inside your rucksack to see what you have")
                        print(rucksack)
                        choice_weapon = input("Please pick weapon of choice ")
                        if choice_weapon == "sword":
                            print()
                            print("You beat the wizards!")
                            score += 1
                            print_score(score)
                            level += 1
                            print("You moved up to level", level)
                            print()
                            choice_scavenge = input("Do you wish to collect the wizard's items? (yes/no )", )
                            if choice_scavenge == "yes":
                                print("Move quickly. Danger approaches!")
                                print("You find a mysterious pair of black dice with many sides on it ")
                                print("Accompanied by a small scroll that was wore off almost to illegibility")
                                print("It says 'Whoever roll these dice must not repeat, for doom will call'")
                                print("Although you need to hurry the dice seem to beckon for you to roll them, do you?")
                                choice_dice_roll = input("yes/no ", )
                                if choice_dice_roll == "yes":
                                    # Using a random function for the dice roll
                                    import random
                                    dice_roll = random.randint(1, 13)
                                    dice_roll_list = []
                                    print("You rolled a ", dice_roll)
                                    # Storing the rolls into a list to later retrieve
                                    dice_roll_list.insert(0, dice_roll)
                                    print("The ground begins to shake underneath you.")
                                    print("Do you go into the trees to escape or draw your sword?", )
                                    dice_danger_choice = input("Trees/Sword ")
                                    if dice_danger_choice == "sword" or "Sword":
                                        print("The ground starts to crumble beneath your feat!")
                                        print("The stones and trees around you begin to fall ")
                                        level -= 1
                                        print("level = ", level)

                            if choice_scavenge == "no":
                                print("You may regret it when supplies run low")
                                print("A mountain, glooming with malice lies ahead. Stay sharp ")
                                print("A path from the underside seems to be safe and well traveled,")
                                print("but can take many days, from which you do not have time")
                                print("there is another however...")
                                print("A underwhelming path up the mountain can be seen heading North")
                                print("Though treacherous by the looks, could save much time.")
                                print("You seem to still have some supplies")
                                print(rucksack)
                                choice_mountain_path = input("Which path do you choose?", name)
                                print("Safe/Treacherous")
                                if choice_mountain_path == "Safe" or "safe":
                                    print()
                                else:
                                    print()

                        elif choice_weapon == "potion":
                            print("The potion caused a thunderous explosion, which scared away the villainous wizards")
                            print()
                            level += 1
                            print(level)
                            score += 10
                            print_score(score)
                            print("You moved up to level ", level)
                        else:
                            print(
                                "Unfortunately the wizards outsmarted you")
                            print("They have cast a potion of immortality upon you")
                            print()
                            print("You will now be their slave for eternity")
                            lives -= 1
                            print("Your lives are now down to", lives)
                            break
                    else:
                        print("Avoiding confrontation when possible is honorable")
                        print("You will have to set up camp for the night")
                        print("Take a look in your rucksack to see what you can use.")
                        print(rucksack)
                if choice_3 > 10:
                    print("You went a little too far without rest, you should be fine though")
                    lives -= 1
                    print(lives)

                if choice_3 < 3:
                    print("Resting is wise, for it is a long journey")

            else:  # Not right
                print("Oh no! Quicksand! Quick look inside your ruck sack to see what you can use")
                print(rucksack)
                print("You only have five minutes to free yourself!")
                quicksand_tool = input("Move quickly! Pick something that you think will help!"),
                if quicksand_tool == "rope":
                    print("Use the rope to hoist yourself up on a nearby tree!")
                    print("In order to escape the treacherous quick sand...")
                    print("You must find the the area of an acute triangle. ")
                    print("The sides are 5, 6 and 7")
                    a = 5
                    b = 6
                    c = 7
                    s = (a + b + c) / 2
                    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
                    choice_area = float(input("Choose what you think the right answer is")),
                    if choice_area == area:
                        print("congratulations")

                else:
                    print("Unfortunately that wont help in this situation.")
                    lives -= 1
                    print(lives)
        else:
            print("Well that's just poor sportsmanship")


def print_score(score):
    print("Your score is", score)


def print_level(level):
    print("Level = ", level)


main()

# Citations:
# https://www.youtube.com/watch?v=UXkuJlDVEdo&list=PLvrGx2UE_sKSYMRFIzeLDMDqiI_8WBJ-_

# https://www.w3schools.com/python/python_lists.asp

# https://developers.google.com/edu/python/lists

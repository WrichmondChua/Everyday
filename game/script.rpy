# The script of the game goes in this file.~
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    #Where you input the name of the player.
    python:
        player_name = renpy.input("Please enter the protagonist's name: ", length = 32, exclude = "0123456789+=,.?!{}[]()<>[ ]-")
        player_name = playername.strip()
        
    #Player name by default if the player entered the game w/o inputting a player name.
        if not player_name:
            player_name = "Default"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define battle = False
define level = 1


define cake_recipe = '''2 sticks unsalted butter, at room temperature, plus more for the pans.

3 cups all-purpose flour, plus more for the pans.

"1 tablespoon baking powder.

1/2 teaspoon salt.

1 1/4 cups sugar.

4 large eggs, at room temperature.

1 tablespoon vanilla extract.

1 1/4 cups whole milk (or 3/4 cup heavy cream mixed with 1/2 cup water).'''

define inventory = list()

image monster1:

    "frame01.png"
    1
    "frame02.png"
    1
    repeat

image doc:
    "doc1.png"
    1
    "doc2.png"

# The game starts here.

define hp = 100

label attack1:

    menu:
        "Which attack?"

        "Fireball":
            "Sorry, that's locked. Level up."
            jump attack1
        "Electric Shock":
            "Sorry, that's locked. Level up."
            jump attack1

        "Punch":     
            n "You attacked!"
            n "To your surprise, the blob monster is kind.."
            n"But you made it hostile."
            $ hp = hp - 5
            n"The blob attacks you!"
            n"Your hp lowered by 5. Your hp is now [hp]."
            show monster1 at offscreenright with moveinleft
            n"The blob angrily runs away."
            n"In his tracks, he leaves behind a document."
            play music "audio/bg.mp3"
            jump document
            

label start:

    init python:    
        def mid_beep(event, **kwargs):
            if event == "show":
                renpy.music.play("mid_beep.ogg", channel="sound", loop=True)
            elif event == "slow_done" or event == "end":
                renpy.music.stop(channel="sound")

        def high_beep(event, **kwargs):
            if event == "show":
                renpy.music.play("high_beep.ogg", channel="sound", loop=True)
            elif event == "slow_done" or event == "end":
                renpy.music.stop(channel="sound")
            
        def low_beep(event, **kwargs):
            if event == "show":
                renpy.music.play("low_beep.ogg", channel="sound", loop=True)
            elif event == "slow_done" or event == "end":
                renpy.music.stop(channel="sound")

    define n = Character("Narrator",callback=low_beep)
    define  b = Character("Blob",callback=high_beep)
    define y = Character("You",callback=mid_beep)



    scene bg

    show mc at left:
        zoom 2.0
    n "Welcome to our village."
    n "Home of amazing treasures-"
    n "But also weird creatures."
    n "So you need to be prepared for everythi-{nw}"
    show shadow with Dissolve(0.3)
    $ battle = True
    play music "audio/battle.mp3"
    play sound "audio/bang.ogg"
    centered "{size=+80}Fight!"
    hide shadow
    show mc at left with pixellate:
        zoom 0.5
    show monster1 at right with pixellate:
        zoom .5

    b "Please don't hurt me!"
    b "I was just strolling around and came upon you."
    menu:

        "Attack":
            jump attack1
            

        "Don't Attack":
            n "The blob monster is..."
            n "Not hostile."
            stop music
            play music "audio/bg.mp3"
            n "It is kind, it doesn't attack."
            n "In return, it gives you a document."
            hide mc

            hide monster1 with pixellate
            jump document
            

label document:

    show doc
    n ".."
    n "The document states the following..."
    n "2 sticks unsalted butter, at room temperature, plus more for the pans.

    3 cups all-purpose flour, plus more for the pans. {nw}"

    n "1 tablespoon baking powder.

    1/2 teaspoon salt.

    1 1/4 cups sugar. {nw}"

    n "4 large eggs, at room temperature.

    1 tablespoon vanilla extract.

    1 1/4 cups whole milk (or 3/4 cup heavy cream mixed with 1/2 cup water)."
    y "A recipe?!"
    y "For a cake?"
    y "Well, I  guess I'll hold onto this."
    jump adventure
    
    scene black with pixellate
    

label crafting:
    n"You decide to do some crafting."
    n"There's not much to craft, but there is one thing in particular."
    y "Something to store things."
    n"You need cotton, cloth, something to stick things together, and string."
    n"Luckily, you have all of those!"
    scene black with dissolve
    n"You're done crafting your sack!"
    centered "{size=+20}Sack-pack!"
    scene black with dissolve
    pause 0.2
    show pack at truecenter with pixellate
    n'Congrats, you made your first craft!'
    n'This backpack can be used to store things. An option in the menu will show up if storing items.'
    n"Would you like to store the cake recipe? \n (NOTE: If not saved, you will not be able to find the recipe later in the game.)"
    jump cake

label cake:
    menu:
        "Yes":
            $ inventory = inventory.append(cake_recipe)
            hide pack with dissolve
            centered "{size=+50}End of day 1."
            scene black with dissolve
            $ MainMenu(confirm=False)()
        
        "No":
            n "Are you sure?"
            jump cake

label taming:
    n"You decide to tame some animals in order to find a new animal companian."
    scene bg with pixellate
    show bird with pixellate:
        xpos 0
        zoom 0.2
    n"Aha! You found an animal!"
    n"It seems to be hiding behind the clouds."
    n"But what is it?"
    show bird with pixellate:
        zoom 1.0
        
    n"You go closer to the animal, examining it carefully."
    y "It's a bird?"
    y "But it's pink?"
    y "Huh."
    show bird at left:
        zoom 1.2
    n"You take your chances, moving closer to the bird."
    y "Does the bird.. like me?"
    n"The bird is closer to you, but you're not the one moving!"
    show bird at left:
        zoom 1.5
    n"The bird is moving towards you!"
    $ renpy.music.set_volume(30,0,channel='sound')
    play sound "audio/bark.ogg"
    "Bird" "{size=+20}BARK BARK BARK!{/size}"
    y "Woah, calm down!"
    y "Wait. Did that bird just bark?"
    n 'Like I said, our village is the "home of weird creatures."'
    n"Anyways, it seems you've made a fighting buddy."
    n"During battles, your pet can attack for you if your HP is too low."
    hide bird with dissolve
    scene black with dissolve
    centered "{size=+50}End of day 1."
    $ MainMenu(confirm=False)()

label fishing:
    scene black
    n"You decide to go fishing."
    n"You let down your rod..."
    n"Slowly pull it up..."
    $ chance = renpy.random.randint(1,2)
    if chance == 1:
        n"Congrats! You caught your first fish."
        centered "{size=+20}Fish!"
        show fish with pixellate
        ".."
        hide fish with dissolve
        centered "{size=+50}End of day 1."
        scene black with dissolve
        $ MainMenu(confirm=False)()
    else:
        n "Unfortunately, you didn't catch a fish."
        n "Try again?"
        menu:
            "Try again":
                jump fishing
            "Don't try again":
                n "Okay, then!"
                centered"{size=+50}End of day 1."
                scene black with dissolve
                $ MainMenu(confirm=False)()
label adventure:
    hide mc
    scene black with dissolve
    n "You wake up, sleepy, but still hazily put on your jacket and head outside."
    scene bg
    show mc with dissolve
    y "Hmmm... what should I do today?"
    menu:
        "Animal Taming":
            jump taming

        "Crafting":
            jump crafting

        "Fishing":
            jump fishing

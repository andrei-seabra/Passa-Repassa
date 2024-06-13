import tkinter, random

class GameWindow:
    # cretate the game window
    window = tkinter.Tk()

    # window format
    window.geometry("1280x720")
    window.title("Passa Repassa")

    # custom icon
    icon = tkinter.PhotoImage(file = "Assets/Images/Logo.png")
    window.iconphoto(False, icon)

class MainCanvas:
    # game window
    window = GameWindow.window

    # create and format of the main canvas
    canvas = tkinter.Canvas(window, width = 1280, height = 720)
    canvas.pack(fill = "both", expand = True)

class GameData:
    # questions and answer data
    questionsAnswer = {
        "Quem descobriu o Brasil?": "pedro álvares cabral",
        "Qual o maior time do futebol brasileiro?" : "flamengo"
    }

    # image references
    paths = {
        "backgroundImage" : [
            "Assets/Images/InicialMenu.png",
            "Assets/Images/Player1Screen.png",
            "Assets/Images/Player2Screen.png",
            "Assets/Images/TimeOutScreen.png",
            "Assets/Images/LoseScreen.png",
            "Assets/Images/WinScreen.png"
        ],

        "icons" : [
            "Assets/Images/PlayButton.png",
            "Assets/Images/Shield.png",
            "Assets/Images/Rocket.png",
            "Assets/Images/Clock.png",
            "Assets/Images/SubmitArrow.png"
        ]
    }

    # colors references
    backgroundColors = {
        "player1" : "#004AAD",
        "player2" : "#D12424"
    }

    # players data
    players = {
        "player1" : {
            "points" : 0,
            "inv" : {
                "shield" : 0,
                "timeFreezer" : 0,
                "doublePoints" : 0
            }
        },

        "player2" : {
            "points" : 0,
            "inv" : {
                "shield" : 0,
                "timeFreezer" : 0,
                "doublePoints" : 0
            }
        }
    }
    
class CanvasManipulation:
    # variables


    # functions
    def canvasCleaner():
        # variables
        canvas = MainCanvas.canvas
        widgets = canvas.find_all()

        # loop to delete every widget of the screen
        for widget in widgets:
            canvas.delete(widget)

 # screen classes
class PlayerScreen:
    def playerScreenHandler(playerBackgroundImage, powerUpImage, backgroundColor, roundTime, qtyShield, qtyFrezzer, qtyDoublePoints):
        # variables
        canvas = MainCanvas.canvas
        window = GameWindow.window
        paths = GameData.paths
        
        # cleans the canvas
        CanvasManipulation.canvasCleaner()

        # widgets

        # add the background image
        backgroundImage = tkinter.PhotoImage(file = playerBackgroundImage)
        canvas.create_image(0, 0, anchor = "nw", image = backgroundImage)
        
        # labels

        # question display
        canvas.create_text(400, 250, anchor="nw", font = ("System", 32), fill = "white", text = f"Quem descobriu o Brasil?")

        # timer display
        canvas.create_text(570, 130, anchor="nw", font = ("System", 40), fill = "white", text = f"00:{roundTime}")

        # score display

        # player1 score display
        canvas.create_text(1080, 75, anchor = "nw", font = ("System", 40), fill = "#004AAD", text = f"0")
        # division display
        canvas.create_text(1125, 75, anchor = "nw", font = ("System", 40), fill = "white", text = "-")
        #player2 score display
        canvas.create_text(1150, 75, anchor = "nw", font = ("System", 40), fill = "#D12424", text = f"0")

        # power up display
        powerUpImageDisplay = tkinter.PhotoImage(file = powerUpImage)
        canvas.create_image(142, 135, anchor = "nw", image = powerUpImageDisplay)

        # interactable

        # answer entry
        answerEntry = tkinter.Entry(window, border = 0, bd = 0, fg = "black", font = ("System", 20), highlightbackground = "#FFF7EC", background = "#FFF7EC")
        canvas.create_window(465, 360, width = 325, height = 50, anchor = "nw", window = answerEntry)

        # submit button
        submitButtonImage = tkinter.PhotoImage(file = paths["icons"][4])
        submitButton = tkinter.Button(window, image = submitButtonImage, bd = 0, activebackground = "#A8A39B", background = "#A8A39B")

        # adds the button to the canvas
        canvas.create_window(799, 368, anchor = "nw", window = submitButton)

        # power ups buttons

        # shield power up button
        shieldButtonImage = tkinter.PhotoImage(file = paths["icons"][1])
        shieldButton = tkinter.Button(window, image = shieldButtonImage, bd = 0, activebackground = "#0A3A7B", background = "#0A3A7B")

        # adds the button to the canvas
        canvas.create_window(930, 583, anchor = "nw", window = shieldButton)

        # quantity display
        canvas.create_text(980, 630, anchor = "nw", font = ("System", 20), fill = "white", text = f"x{qtyShield}")

        # freeze time power up button
        freezeTimeButtonImage = tkinter.PhotoImage(file = paths["icons"][3])
        freezeTimeButton = tkinter.Button(window, image = freezeTimeButtonImage, bd = 0, activebackground = "#0A3A7B", background = "#0A3A7B")

        # adds the button to the canvas
        canvas.create_window(1035, 583, anchor = "nw", window = freezeTimeButton)

        # quantity display
        canvas.create_text(1085, 630, anchor = "nw", font = ("System", 20), fill = "white", text = f"x{qtyFrezzer}")

        # double points power up button
        doublePointsButtonImage = tkinter.PhotoImage(file = paths["icons"][2])
        doublePointsButton = tkinter.Button(window, image = doublePointsButtonImage, bd = 0, activebackground = "#0A3A7B", background = "#0A3A7B")

        # adds the button to the canvas
        canvas.create_window(1143, 583, anchor = "nw", window = doublePointsButton)

        # quantity display
        canvas.create_text(1190, 630, anchor = "nw", font = ("System", 20), fill = "white", text = f"x{qtyDoublePoints}")

        # updates the images into the canvas
        canvas.mainloop() # rever essa parte

class EndingScreen:
    def endingScreenHandler(backgroundImage):
        # variables
        canvas = MainCanvas.canvas

        # cleans the canvas
        CanvasManipulation.canvasCleaner()

        # adds the background image to the screen
        endingBackgroundImage = tkinter.PhotoImage(file = backgroundImage)
        canvas.create_image(0, 0, anchor = "nw", image = endingBackgroundImage)

        # updates the images into the canvas
        canvas.pack()

class Match:
    #variables


    # functions
    def timeHandler():
        # variables
        roundTime = 15 # in seconds

        # timer
        for i in range(roundTime, -1, -1):
            print(i)

    def matchHandler(): # debuger
        # variables
        paths = GameData.paths
        colors = GameData.backgroundColors

        player1Background = paths["backgroundImage"][1]
        player2Background = paths["backgroundImage"][2]
        clockIcon = paths["icons"][3]

        # creates the player screen instances
        PlayerScreen.playerScreenHandler(player1Background, clockIcon, colors["player1"],  15, 0, 0, 0)

        Match.timeHandler()

class InicialMenu:
    # variables
    window = GameWindow.window
    canvas = MainCanvas.canvas
    paths = GameData.paths
    
    # add the background image
    backgroundImage = tkinter.PhotoImage(file = paths["backgroundImage"][0])
    canvas.create_image(0, 0, anchor = "nw", image = backgroundImage)
    
    # create and format the play button
    playButtonImage = tkinter.PhotoImage(file = paths["icons"][0])
    playButton = tkinter.Button(window, image = playButtonImage, bd = 0, activebackground = "#004AAD", background = "#004AAD", command = Match.matchHandler)

    # adds the play button to the canvas
    canvas.create_window(500, 350, anchor = "nw", window = playButton)

GameWindow.window.mainloop()

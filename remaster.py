import tkinter, random

class GameWindow:
    # cretate the game window
    window = tkinter.Tk()

    # window format
    window.geometry("1280x720")
    window.title("Passa Repassa")
    window.configure(bg="white")

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
            "Assets/Images/Lamp.png",
            "Assets/Images/SubmitArrow.png"
        ]
    }

    # questions and answer data
    questionsAnswer = {
        "Quem descobriu o Brasil?": "pedro álvares cabral",
        "Qual o maior time do futebol brasileiro?" : "flamengo"
    }

    # players data
    player1 = {
            "points" : 0,
            "powerUps" : {
                "shield" : 1,
                "timeFreeze" : 1,
                "doublePoints" : 1
            }     
                }
    
    player2 = {
            "points" : 0,
            "powerUps" : {
                "shield" : 1,
                "timeFreeze" : 1,
                "doublePoints" : 1
            }     
                }
    
class CanvasManipulation:
    # variables


    # functions
    def canvasCleaner():
        # variables
        canvas = MainCanvas.canvas
        widgets = canvas.find_all()

        for widget in widgets:
            canvas.delete(widget)

class Match:
    # screen classes
    class PlayerScreen:
        def __init__(self):
            print("player screen")
            # variables
            window = GameWindow.window
            canvas = MainCanvas.canvas
            paths = GameData.paths

            player1Screen = paths["backgroundImage"][1]
            player2Screen = paths["backgroundImage"][2]
        
            # add the background image
            backgroundImage = tkinter.PhotoImage(file = player1Screen)
            self.canvas.create_image(0, 0, anchor = "nw", image = backgroundImage)

    # functions
    def timeHandler():
        # variables
        roundTime = 15 # in seconds

        # timer
        for i in range(roundTime, -1, -1):
            print(i)

    def matchHandler():
        playerScreen = Match.PlayerScreen()

        CanvasManipulation.canvasCleaner()
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
    playButton = tkinter.Button(window, image = playButtonImage, bd = 0, fg = "#004AAD", highlightbackground = "#004AAD", activebackground = "#004AAD", background = "#004AAD", command = Match.matchHandler)

    # adds the play button to the canvas
    canvas.create_window(500, 350, anchor = "nw", window = playButton)

GameWindow.window.mainloop()

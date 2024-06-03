import tkinter, random

class GameWindow:
    # cretates the game window
    window = tkinter.Tk()

    # window format
    window.geometry("1280x720")
    window.title("Passa Repassa")
    window.configure(bg="white")

class GameData:
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
    
class WindowManipulation:
    # clean all the widgets of the main canvas
        def cleanCanvas(canvas):
            widgets = canvas.find_all()

            for widget in range (len(widgets)):
                widgets[widget].destroy()

class InicialMenu:
    # game window
    window = GameWindow.window

    # create and format of the main canvas
    canvas = tkinter.Canvas(window, width = 1280, height = 720)
    canvas.pack(fill = "both", expand = True)
    
    # add the background image to the inicial menu
    backgroundImage = tkinter.PhotoImage(file = "Assets/Images/InicialMenu.png")
    backgroundImageLabel = canvas.create_image(0, 0, anchor = "nw", image = backgroundImage)

    # create and format of the play button
    playButtonImage = tkinter.PhotoImage(file = "Assets/Images/PlayButton.png")
    playButton = tkinter.Button(window, bg = "blue", fg = "#004AAD", highlightbackground = "#004AAD", activebackground = "#004AAD", background = "#004AAD", command = WindowManipulation.cleanCanvas(canvas))

    # adds the play button to the canvas
    canvas.create_window(500, 350, anchor = "nw", window = playButton)

GameWindow.window.mainloop()

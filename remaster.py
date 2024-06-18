import tkinter as tk
import random

class GameWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1280x720")
        self.window.title("Passa Repassa")
        self.icon = tk.PhotoImage(file="Assets/Images/Logo.png")
        self.window.iconphoto(False, self.icon)

class MainCanvas:
    def __init__(self, window):
        self.canvas = tk.Canvas(window, width=1280, height=720)
        self.canvas.pack(fill="both", expand=True)

class GameData:
    questionsAnswer = {
        "Quem descobriu o Brasil?": "pedro álvares cabral",
        "Qual o maior time do futebol brasileiro?": "flamengo",
        # Adicione mais perguntas e respostas aqui
    }

    paths = {
        "backgroundImage": [
            "Assets/Images/InicialMenu.png",
            "Assets/Images/Player1Screen.png",
            "Assets/Images/Player2Screen.png",
            "Assets/Images/TimeOutScreen.png",
            "Assets/Images/LoseScreen.png",
            "Assets/Images/WinScreen.png"
        ],
        "icons": [
            "Assets/Images/PlayButton.png",
            "Assets/Images/Shield.png",
            "Assets/Images/Rocket.png",
            "Assets/Images/Clock.png",
            "Assets/Images/SubmitArrow.png"
        ]
    }

    backgroundColors = {
        "player1": "#004AAD",
        "player2": "#D12424"
    }

    players = {
        "player1": {
            "points": 0,
            "inv": {
                "shield": 0,
                "timeFreezer": 0,
                "doublePoints": 0
            }
        },
        "player2": {
            "points": 0,
            "inv": {
                "shield": 0,
                "timeFreezer": 0,
                "doublePoints": 0
            }
        }
    }

class CanvasManipulation:
    @staticmethod
    def canvasCleaner(canvas):
        widgets = canvas.find_all()
        for widget in widgets:
            canvas.delete(widget)

class EndingScreen:
    @staticmethod
    def endingScreenHandler(canvas, backgroundImage, nextHandler):
        CanvasManipulation.canvasCleaner(canvas)
        endingBackgroundImage = tk.PhotoImage(file=backgroundImage)
        canvas.backgroundImage = endingBackgroundImage  # Referência para evitar coleta de lixo
        canvas.create_image(0, 0, anchor="nw", image=endingBackgroundImage)
        canvas.pack()
        canvas.after(2000, nextHandler)  # Espera 2 segundos antes de chamar o próximo handler

class PlayerScreen:
    @staticmethod
    def playerScreenHandler(canvas, window, playerBackgroundImage, powerUpImage, backgroundColor, roundTime, qtyShield, qtyFrezzer, qtyDoublePoints, player):
        CanvasManipulation.canvasCleaner(canvas)
        backgroundImage = tk.PhotoImage(file=playerBackgroundImage)
        canvas.backgroundImage = backgroundImage  # Referência para evitar coleta de lixo
        canvas.create_image(0, 0, anchor="nw", image=backgroundImage)

        question = random.choice(list(GameData.questionsAnswer.keys()))
        canvas.current_question = question  # Salva a pergunta atual no canvas para uso posterior
        canvas.create_text(400, 250, anchor="nw", font=("System", 32), fill="white", text=question)
        canvas.timer_text = canvas.create_text(570, 130, anchor="nw", font=("System", 40), fill="white", text=f"00:{roundTime}")
        canvas.create_text(1080, 75, anchor="nw", font=("System", 40), fill="#004AAD", text=f"{GameData.players['player1']['points']}")
        canvas.create_text(1125, 75, anchor="nw", font=("System", 40), fill="white", text="-")
        canvas.create_text(1150, 75, anchor="nw", font=("System", 40), fill="#D12424", text=f"{GameData.players['player2']['points']}")

        powerUpImageDisplay = tk.PhotoImage(file=powerUpImage)
        canvas.powerUpImageDisplay = powerUpImageDisplay  # Referência para evitar coleta de lixo
        canvas.create_image(142, 135, anchor="nw", image=powerUpImageDisplay)

        answerEntry = tk.Entry(window, border=0, bd=0, fg="black", font=("System", 20), highlightbackground="#FFF7EC", background="#FFF7EC")
        canvas.create_window(465, 360, width=325, height=50, anchor="nw", window=answerEntry)

        submitButtonImage = tk.PhotoImage(file=GameData.paths["icons"][4])
        submitButton = tk.Button(window, image=submitButtonImage, bd=0, activebackground="#A8A39B", background="#A8A39B",
                                 command=lambda: PlayerScreen.checkAnswer(canvas, window, answerEntry, player))
        submitButton.image = submitButtonImage  # Referência para evitar coleta de lixo
        canvas.create_window(799, 368, anchor="nw", window=submitButton)

        shieldButtonImage = tk.PhotoImage(file=GameData.paths["icons"][1])
        shieldButton = tk.Button(window, image=shieldButtonImage, bd=0, activebackground="#0A3A7B", background="#0A3A7B")
        shieldButton.image = shieldButtonImage  # Referência para evitar coleta de lixo
        canvas.create_window(930, 583, anchor="nw", window=shieldButton)
        canvas.create_text(980, 630, anchor="nw", font=("System", 20), fill="white", text=f"x{qtyShield}")

        freezeTimeButtonImage = tk.PhotoImage(file=GameData.paths["icons"][3])
        freezeTimeButton = tk.Button(window, image=freezeTimeButtonImage, bd=0, activebackground="#0A3A7B", background="#0A3A7B")
        freezeTimeButton.image = freezeTimeButtonImage  # Referência para evitar coleta de lixo
        canvas.create_window(1035, 583, anchor="nw", window=freezeTimeButton)
        canvas.create_text(1085, 630, anchor="nw", font=("System", 20), fill="white", text=f"x{qtyFrezzer}")

        doublePointsButtonImage = tk.PhotoImage(file=GameData.paths["icons"][2])
        doublePointsButton = tk.Button(window, image=doublePointsButtonImage, bd=0, activebackground="#0A3A7B", background="#0A3A7B")
        doublePointsButton.image = doublePointsButtonImage  # Referência para evitar coleta de lixo
        canvas.create_window(1143, 583, anchor="nw", window=doublePointsButton)
        canvas.create_text(1190, 630, anchor="nw", font=("System", 20), fill="white", text=f"x{qtyDoublePoints}")

        PlayerScreen.start_timer(canvas, window, roundTime, player)

    @staticmethod
    def start_timer(canvas, window, time_left, player):
        canvas.after_cancel(canvas.timer) if hasattr(canvas, 'timer') else None  # Cancela o timer anterior se existir
        PlayerScreen.update_timer(canvas, window, time_left, player)

    @staticmethod
    def update_timer(canvas, window, time_left, player):
        if time_left >= 0:
            minutes = time_left // 60
            seconds = time_left % 60
            time_formatted = f"{minutes:02}:{seconds:02}"
            canvas.itemconfig(canvas.timer_text, text=time_formatted)
            canvas.timer = window.after(1000, PlayerScreen.update_timer, canvas, window, time_left - 1, player)
        else:
            PlayerScreen.next_player(canvas, window, player, "time")

    @staticmethod
    def checkAnswer(canvas, window, entry, player):
        answer = entry.get().strip().lower()
        question = canvas.current_question
        correct_answer = GameData.questionsAnswer[question].strip().lower()
        if answer == correct_answer:
            PlayerScreen.next_player(canvas, window, player, "win")
        else:
            PlayerScreen.next_player(canvas, window, player, "lose")

    @staticmethod
    def next_player(canvas, window, current_player, result):
        next_player = "player2" if current_player == "player1" else "player1"
        if result == "win":
            GameData.players[current_player]["points"] += 1

        background_index = {
            "player1": 1,
            "player2": 2,
            "time": 3,
            "lose": 4,
            "win": 5
        }

        if result in ["win", "lose", "time"]:
            EndingScreen.endingScreenHandler(canvas, GameData.paths["backgroundImage"][background_index[result]], lambda: PlayerScreen.playerScreenHandler(
                canvas, window, GameData.paths["backgroundImage"][background_index[next_player]], GameData.paths["icons"][3],
                GameData.backgroundColors[next_player], 15, 0, 0, 0, next_player))
        else:
            PlayerScreen.playerScreenHandler(canvas, window, GameData.paths["backgroundImage"][background_index[next_player]], GameData.paths["icons"][3],
                                             GameData.backgroundColors[next_player], 15, 0, 0, 0, next_player)

class Match:
    @staticmethod
    def matchHandler():
        paths = GameData.paths
        colors = GameData.backgroundColors
        player1Background = paths["backgroundImage"][1]
        player2Background = paths["backgroundImage"][2]
        clockIcon = paths["icons"][3]
        PlayerScreen.playerScreenHandler(main_canvas.canvas, game_window.window, player1Background, clockIcon, colors["player1"], 15, 0, 0, 0, "player1")

class InicialMenu:
    def __init__(self):
        window = game_window.window
        canvas = main_canvas.canvas
        paths = GameData.paths
        backgroundImage = tk.PhotoImage(file=paths["backgroundImage"][0])
        canvas.backgroundImage = backgroundImage  # Referência para evitar coleta de lixo
        canvas.create_image(0, 0, anchor="nw", image=backgroundImage)
        playButtonImage = tk.PhotoImage(file=paths["icons"][0])
        playButton = tk.Button(window, image=playButtonImage, bd=0, activebackground="#004AAD", background="#004AAD", command=Match.matchHandler)
        playButton.image = playButtonImage  # Referência para evitar coleta de lixo
        canvas.create_window(500, 350, anchor="nw", window=playButton)

if __name__ == "__main__":
    game_window = GameWindow()
    main_canvas = MainCanvas(game_window.window)
    inicial_menu = InicialMenu()
    game_window.window.mainloop()

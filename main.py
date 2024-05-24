import tkinter as tk
import random

# cria a janela
window = tk.Tk()
# formatação da janela
window.geometry("1280x720")
window.title("Passa Repassa")
window.configure(bg="white")

class Data:
    # perguntas e respostas
    questionsAnswers = {
        "Quem descobriu o Brasil?" : "pedro álvares cabral",
        "Qual o maior time do futebol brasileiro?" : "flamengo"
    }

    # dados dos jogadores
    player1 = {
        "pontos" : 0,
        "inv" : ""
    }

    player2 = {
        "pontos" : 0,
        "inv" : ""
    }

    # referência às imagens de fundo de cada jogador e às respectivas cores de botões
    playersScreens = {
        "player1" : ["Assets/Images/Player1Screen.png", "#0A3A7B"],
        "player2" : ["Assets/Images/Player2Screen.png", "#9D1C1C"]
    }

    # rodadas
    matchRound = 1

class Functions:
    roundTime = 15  # Tempo da rodada em segundos
    currentPlayer = "player1"
    question = random.choice(list(Data.questionsAnswers.keys()))  # Escolhe uma pergunta aleatória no início
    images = {}  # Dicionário para armazenar referências às imagens

    @staticmethod
    def update_timer(label):
        if Functions.roundTime > 0:
            Functions.roundTime -= 1
            label.config(text=f"00:{Functions.roundTime:02d}")
            window.after(1000, Functions.update_timer, label)
        else:
            Functions.timeOutScreen()  # Exibir tela de tempo esgotado

    @staticmethod
    def getQuestion():
        return Functions.question

    @staticmethod
    def play():
        Functions.cleanWindow()
        Functions.roundTime = 15  # Reinicia o temporizador a cada rodada

        def playerScreen():
            currentPlayerData = Data.playersScreens[Functions.currentPlayer]
            playerCanvas = tk.Canvas(window, width=1280, height=720)
            playerCanvas.pack(fill="both", expand=True)
            playerScreenImage = tk.PhotoImage(file=currentPlayerData[0])
            Functions.images['playerScreenImage'] = playerScreenImage  # Mantém a referência
            playerCanvas.create_image(0, 0, image=playerScreenImage, anchor="nw")

            timerLabel = tk.Label(window, text=f"00:{Functions.roundTime:02d}", font=("System", 40), bg="white")
            timerLabel.pack()
            Functions.update_timer(timerLabel)  # Iniciar o temporizador

            questionLabel = playerCanvas.create_text(639, 250, text=f"{Functions.getQuestion()}", font=("System", 32), fill="#FFF7EC")
            answerEntry = tk.Entry(window, border=0, bd=0, fg="black", font=("System", 20), highlightbackground="#FFF7EC", background="#FFF7EC")
            playerCanvas.create_window(465, 360, width=325, height=51, anchor="nw", window=answerEntry)

            submitButtonImage = tk.PhotoImage(file="Assets/Images/SubmitArrow.png")
            Functions.images['submitButtonImage'] = submitButtonImage  # Mantém a referência
            submitButton = tk.Button(window, border=0, bd=0, fg=currentPlayerData[1], highlightbackground=currentPlayerData[1], activebackground=currentPlayerData[1], background=currentPlayerData[1], image=submitButtonImage, command=lambda: Functions.check_answer(answerEntry.get()))
            playerCanvas.create_window(800, 368, anchor="nw", window=submitButton)

        playerScreen()

    @staticmethod
    def check_answer(answer):
        correct_answer = Data.questionsAnswers[Functions.getQuestion()]

        if answer.lower() == correct_answer:
            Functions.update_score()
            Functions.winScreen()
        else:
            Functions.loseScreen()

    @staticmethod
    def update_score():
        if Functions.currentPlayer == "player1":
            Data.player1["pontos"] += 1
        else:
            Data.player2["pontos"] += 1

    @staticmethod
    def switch_player():
        if Functions.currentPlayer == "player1":
            Functions.currentPlayer = "player2"
        else:
            Functions.currentPlayer = "player1"
        Functions.question = random.choice(list(Data.questionsAnswers.keys()))  # Escolhe uma nova pergunta para o próximo jogador
        Functions.play()

    @staticmethod
    def winScreen():
        Functions.cleanWindow()
        winCanvas = tk.Canvas(window, width=1280, height=720)
        winCanvas.pack(fill="both", expand=True)
        winScreenImage = tk.PhotoImage(file="Assets/Images/WinScreen.png")
        Functions.images['winScreenImage'] = winScreenImage  # Mantém a referência
        winCanvas.create_image(0, 0, image=winScreenImage, anchor="nw")
        window.after(2000, Functions.switch_player)

    @staticmethod
    def loseScreen():
        Functions.cleanWindow()
        loseCanvas = tk.Canvas(window, width=1280, height=720)
        loseCanvas.pack(fill="both", expand=True)
        loseScreenImage = tk.PhotoImage(file="Assets/Images/LoseScreen.png")
        Functions.images['loseScreenImage'] = loseScreenImage  # Mantém a referência
        loseCanvas.create_image(0, 0, image=loseScreenImage, anchor="nw")
        window.after(2000, Functions.switch_player)

    @staticmethod
    def timeOutScreen():
        Functions.cleanWindow()
        timeOutCanvas = tk.Canvas(window, width=1280, height=720)
        timeOutCanvas.pack(fill="both", expand=True)
        timeOutScreenImage = tk.PhotoImage(file="Assets/Images/TimeOutScreen.png")
        Functions.images['timeOutScreenImage'] = timeOutScreenImage  # Mantém a referência
        timeOutCanvas.create_image(0, 0, image=timeOutScreenImage, anchor="nw")
        window.after(2000, Functions.switch_player)

    @staticmethod
    def cleanWindow():
        for widget in window.winfo_children():
            widget.destroy()

class InicialMenu:
    # criação da tela
    inicialMenuCanvas = tk.Canvas(window, width=1280, height=720)
    inicialMenuCanvas.pack(fill="both", expand=True)

    # adiciona a imagem no fundo da tela
    inicialMenuImage = tk.PhotoImage(file="Assets/Images/InicialMenu.png")
    Functions.images['inicialMenuImage'] = inicialMenuImage  # Mantém a referência
    inicialMenuImageBackground = inicialMenuCanvas.create_image(0, 0, image=inicialMenuImage, anchor="nw")

    # adiciona o botão de jogar na tela
    playButtonImage = tk.PhotoImage(file="Assets/Images/PlayButton.png")
    Functions.images['playButtonImage'] = playButtonImage  # Mantém a referência
    playButton = tk.Button(window, image=playButtonImage, bd=0, fg="#004AAD", highlightbackground="#004AAD", activebackground="#004AAD", background="#004AAD", command=Functions.play)
    inicialMenuCanvas.create_window(500, 350, anchor="nw", window=playButton)

# roda a janela principal em looping
window.mainloop()

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
        "poderes" : {
            "escudo" : 1,
            "congelar" : 1,
            "extra" : 1
        }
    }

    player2 = {
        "pontos" : 0,
        "poderes" : {
            "escudo" : 1,
            "congelar" : 1,
            "extra" : 1
        }
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
    def update_timer(label, canvas):
        if Functions.roundTime > 0:
            Functions.roundTime -= 1
            label.config(text=f"00:{Functions.roundTime:02d}")
            window.after(1000, Functions.update_timer, label, canvas)
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
            Functions.update_timer(timerLabel, playerCanvas)  # Iniciar o temporizador

            clockImage = tk.PhotoImage(file="Assets/Images/clock.png")
            Functions.images['clockImage'] = clockImage  # Mantém a referência
            playerCanvas.create_image(100, 50, image=clockImage, anchor="nw")  # Exibe a imagem do relógio

            questionLabel = playerCanvas.create_text(639, 250, text=f"{Functions.getQuestion()}", font=("System", 32), fill="#FFF7EC")
            answerEntry = tk.Entry(window, border=0, bd=0, fg="black", font=("System", 20), highlightbackground="#FFF7EC", background="#FFF7EC")
            playerCanvas.create_window(465, 360, width=325, height=51, anchor="nw", window=answerEntry)

            submitButtonImage = tk.PhotoImage(file="Assets/Images/SubmitArrow.png")
            Functions.images['submitButtonImage'] = submitButtonImage  # Mantém a referência
            submitButton = tk.Button(window, border=0, bd=0, fg=currentPlayerData[1], highlightbackground=currentPlayerData[1], activebackground=currentPlayerData[1], background=currentPlayerData[1], image=submitButtonImage, command=lambda: Functions.check_answer(answerEntry.get()))
            playerCanvas.create_window(800, 368, anchor="nw", window=submitButton)

            # Placar
            player1ScoreLabel = playerCanvas.create_text(1100, 110, text=f"{Data.player1['pontos']}", font=("System", 40), fill="#004AAD")
            scoreLabel = playerCanvas.create_text(1130, 110, text="-", font=("System", 40), fill="#FFF7EC")
            player2ScoreLabel = playerCanvas.create_text(1160, 110, text=f"{Data.player2['pontos']}", font=("System", 40), fill="#D12424")

            # Botões de poderes
            shieldButtonImage = tk.PhotoImage(file="Assets/Images/Shield.png")
            Functions.images['shieldButtonImage'] = shieldButtonImage  # Mantém a referência
            shieldButton = tk.Button(window, border=0, bd=0, fg=currentPlayerData[1], highlightbackground=currentPlayerData[1], activebackground=currentPlayerData[1], background=currentPlayerData[1], image=shieldButtonImage, command=Functions.use_shield)
            playerCanvas.create_window(1035, 580, anchor="nw", window=shieldButton)
            shieldQuantityLabel = playerCanvas.create_text(1115, 650, text=f"{Data[Functions.currentPlayer]['poderes']['escudo']}x", font=("System", 18), fill="#FFF7EC")

            clockButtonImage = tk.PhotoImage(file="Assets/Images/Clock.png")
            Functions.images['clockButtonImage'] = clockButtonImage  # Mantém a referência
            clockButton = tk.Button(window, border=0, bd=0, fg=currentPlayerData[1], highlightbackground=currentPlayerData[1], activebackground=currentPlayerData[1], background=currentPlayerData[1], image=clockButtonImage, command=Functions.use_clock)
            playerCanvas.create_window(928, 583, anchor="nw", window=clockButton)
            clockQuantityLabel = playerCanvas.create_text(1005, 650, text=f"{Data[Functions.currentPlayer]['poderes']['congelar']}x", font=("System", 18), fill="#FFF7EC")

            rocketButtonImage = tk.PhotoImage(file="Assets/Images/Rocket.png")
            Functions.images['rocketButtonImage'] = rocketButtonImage  # Mantém a referência
            rocketButton = tk.Button(window, border=0, bd=0, fg=currentPlayerData[1], highlightbackground=currentPlayerData[1], activebackground=currentPlayerData[1], background=currentPlayerData[1], image=rocketButtonImage, command=Functions.use_rocket)
            playerCanvas.create_window(1140, 583, anchor="nw", window=rocketButton)
            rocketQuantityLabel = playerCanvas.create_text(1220, 650, text=f"{Data[Functions.currentPlayer]['poderes']['extra']}x", font=("System", 18), fill="#FFF7EC")

        playerScreen()

    @staticmethod
    def use_shield():
        if Data[Functions.currentPlayer]['poderes']['escudo'] > 0:
            Data[Functions.currentPlayer]['poderes']['escudo'] -= 1
            print(f"{Functions.currentPlayer} usou o poder de escudo!")

    @staticmethod
    def use_clock():
        if Data[Functions.currentPlayer]['poderes']['congelar'] > 0:
            Data[Functions.currentPlayer]['poderes']['congelar'] -= 1
            Functions.roundTime += 10  # Adiciona 10 segundos ao tempo restante
            print(f"{Functions.currentPlayer} usou o poder de congelar o tempo!")

    @staticmethod
    def use_rocket():
        if Data[Functions.currentPlayer]['poderes']['extra'] > 0:
            Data[Functions.currentPlayer]['poderes']['extra'] -= 1
            Data[Functions.currentPlayer]['pontos'] += 1  # Adiciona um ponto extra ao jogador
            print(f"{Functions.currentPlayer} usou o poder de ponto extra!")
            Functions.update_score_labels()

    @staticmethod
    def update_score_labels():
        # Atualiza os rótulos de pontuação na tela
        pass  # Implemente a lógica para atualizar os rótulos de pontuação

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
        Functions.update_score_labels()

    @staticmethod
    def switch_player():
        if Functions.currentPlayer == "player1":
            Functions.currentPlayer = "player2"
        else:
            Functions.currentPlayer = "player1"

        Functions.question = random.choice(list(Data.questionsAnswers.keys()))
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

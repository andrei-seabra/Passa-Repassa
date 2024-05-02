import tkinter, random, time, threading

# cria a janela
window = tkinter.Tk()
# formatação da janela
window.geometry("1280x720")
window.title("Passa Repassa")
window.configure(bg="white")

class Data:
    # perguntas e repostas
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

    # referência às imagens de fundo de cada jogador e às respetivas cores de botões // OBS: fzr um sistema que identifica de q jogador é a vez para mudar a imagem e a cor de referência dentro desse dictionary
    playersScreens = {
        "player1" : ["Assets/Images/Player1Screen.png", "#0A3A7B"],
        "player2" : ["Assets/Images/Player2Screen.png", "#9D1C1C"]
        }

    player1Screen = playersScreens["player1"]
    player1ScreenImage = player1Screen[0] # referência da imagem de fundo do jogador 1
    player1ScreenColor = player1Screen[1] # referência da cor dos botões do jogador 1

    player2Screen = playersScreens["player2"]
    player2ScreenImage = player2Screen[0] # referência da imagem de fundo do jogador 2
    player2ScreenColor = player2Screen[1] # referência da cor dos botões do jogador 2

    # rodadas
    matchRound = 1

class Functions:
    # remove todos os elementos da janela inicial
    def cleanWindow():
        for element in window.winfo_children():
            element.destroy()

    # pega uma pergunta aleatória e sua respectiva resposta
    def getQuestion():
        question = random.choice(list(Data.questionsAnswers.keys()))
        return question

    # faz o timer da rodada funcionar
    def timer():
        roundTime = 15 # tempo da rodada em segundos
        while roundTime > 0:
            roundTime -= 1
            print(roundTime)
            time.sleep(1)
        return roundTime

    # rodar o looping
    timerLoop = threading.Thread(target=timer)
    timerLoop.start()

    # funções para representar se o jogador acertou/errou a resposta, além de se o tempo se esgotou

    # tela de acerto (caso o jogador acerte a reposta da pergunta)
    def winScreen():
        # remove todos os elementos da janela inicial
        Functions.cleanWindow()
        
        # criação da janela
        winCanvas = tkinter.Canvas(window, width=1280, height=720)
        winCanvas.pack(fill="both", expand=True)

        # adiciona a imagem de fundo
        winScreenImage = tkinter.PhotoImage(file="Assets/Images/WinScreen.png")
        winScreenLabel = winCanvas.create_image(0, 0, image=winScreenImage, anchor="nw")

    # tela de erro (caso o jogador erre a reposta da pergunta)
    def loseScreen():
        # remove todos os elementos da janela inicial
        Functions.cleanWindow()
        
        # criação da janela
        loseCanvas = tkinter.Canvas(window, width=1280, height=720)
        loseCanvas.pack(fill="both", expand=True)

        # adiciona a imagem de fundo
        loseScreenImage = tkinter.PhotoImage(file="Assets/Images/WinScreen.png")
        loseScreenLabel = loseCanvas.create_image(0, 0, image=loseScreenImage, anchor="nw")

    # tela de tempo (caso o jogador não responda em tempo hábil)
    def timeOutScreen():
        # remove todos os elementos da janela inicial
        Functions.cleanWindow()
        
        # criação da janela
        timeOutCanvas = tkinter.Canvas(window, width=1280, height=720)
        timeOutCanvas.pack(fill="both", expand=True)

        # adiciona a imagem de fundo
        timeOutScreenImage = tkinter.PhotoImage(file="Assets/Images/WinScreen.png")
        timeOutScreenLabel = timeOutCanvas.create_image(0, 0, image=timeOutScreenImage, anchor="nw")

    def play():
        # remove todos os elementos da janela inicial
        Functions.cleanWindow()

        # função que que criam a tela da partida dos jogadores, indicado pela cor do fundo da imagem (azul = player1 e vermelho = player2), além de adicionar todos os elementos funcionais na tela como textos que se alteram, botões etc
        def playerScreen():
            # criação da tela
            player1Canvas = tkinter.Canvas(window, width=1280, height=720)
            player1Canvas.pack(fill="both", expand=True)    

            # adiciona a imagem de fundo
            player1ScreenImage = tkinter.PhotoImage(file=Data.player1ScreenImage) # referência da imagem de fundo de cada jogador
            player1Canvas.create_image(0,0, image=player1ScreenImage, anchor="nw")

            # temporizador
            timerLabel = player1Canvas.create_text(639, 160, text=f"00:{Functions.timer}", font=("System", 40), fill="#FFF7EC")

            # placar
            player1ScoreLabel = player1Canvas.create_text(1100, 110, text=f"{Data.player1["pontos"]}", font=("System", 40), fill="#004AAD")
            scoreLabel = player1Canvas.create_text(1130, 110, text="-", font=("System", 40), fill="#FFF7EC")
            player2ScoreLabel = player1Canvas.create_text(1160, 110, text=f"{Data.player2["pontos"]}", font=("System", 40), fill="#D12424")

            # pergunta
            questionLabel = player1Canvas.create_text(639, 250, text=f"{Functions.getQuestion()}", font=("System", 32), fill="#FFF7EC")
            # entrada de respostas
            answerEntry = tkinter.Entry(window, border=0, bd=0, fg="black", font=("System", 20), highlightbackground="#FFF7EC", background="#FFF7EC")
            answerEntryLabel = player1Canvas.create_window(465, 360, width=325, height= 51, anchor="nw", window=answerEntry)

            # botão para enviar repostas
            submitButtonImage = tkinter.PhotoImage(file="Assets/Images/SubmitArrow.png")
            submitButton = tkinter.Button(window, border=0, bd=0, fg="#A8A39B", highlightbackground="#A8A39B", activebackground="#A8A39B", background="#A8A39B", image=submitButtonImage) # trocar a referência da cor em cada botão da tela, e nos abaixo também
            submitButtonLabel = player1Canvas.create_window(800, 368, anchor="nw", window=submitButton)

            # botões dos poderes e dica

            # botão do poder de escudo (2° chance)
            shieldButtonImage = tkinter.PhotoImage(file="Assets/Images/Shield.png") 
            shieldButton = tkinter.Button(window, border=0, bd=0, fg="#0A3A7B", highlightbackground="#0A3A7B", activebackground="#0A3A7B", background="#0A3A7B", image=shieldButtonImage)
            shieldButtonLabel = player1Canvas.create_window(1035, 580, anchor="nw", window=shieldButton)
            shieldQuantityLabel = player1Canvas.create_text(1115, 650, text="0x", font=("System", 18), fill="#FFF7EC") # mostra a quantidade
            # botão do poder de congelar o tempo
            clockButtonImage = tkinter.PhotoImage(file="Assets/Images/Clock.png") 
            clockButton = tkinter.Button(window, border=0, bd=0, fg="#0A3A7B", highlightbackground="#0A3A7B", activebackground="#0A3A7B", background="#0A3A7B", image=clockButtonImage)
            clockButtonLabel = player1Canvas.create_window(928, 583, anchor="nw", window=clockButton)
            clockQuantityLabel = player1Canvas.create_text(1005, 650, text="0x", font=("System", 18), fill="#FFF7EC") # mostra a quantidade
            # botão do poder de ponto extra
            rocketButtonImage = tkinter.PhotoImage(file="Assets/Images/Rocket.png") 
            rocketButton = tkinter.Button(window, border=0, bd=0, fg="#0A3A7B", highlightbackground="#0A3A7B", activebackground="#0A3A7B", background="#0A3A7B", image=rocketButtonImage)
            rocketButtonLabel = player1Canvas.create_window(1140, 583, anchor="nw", window=rocketButton)
            rocketQuantityLabel = player1Canvas.create_text(1220, 650, text="0x", font=("System", 18), fill="#FFF7EC") # mostra a quantidade
            # dica
            tipButtonImage = tkinter.PhotoImage(file="Assets/Images/Lamp.png") 
            tipButton = tkinter.Button(window, border=0, bd=0, fg="#0A3A7B", highlightbackground="#0A3A7B", activebackground="#0A3A7B", background="#0A3A7B", image=tipButtonImage)
            tipButtonLabel = player1Canvas.create_window(89, 583, anchor="nw", window=tipButton)
            tipQuantityLabel = player1Canvas.create_text(160, 650, text="0x", font=("System", 18), fill="#FFF7EC") # mostra a quantidade
            # display do poder que foi ativado na rodada pelo jogador
            powerDisplay = player1Canvas.create_image(142, 135, image=clockButtonImage, anchor="nw") # é só trocar a referência da imagem no 'image=' (dica: usar o msm path q já usei pros botões)

        playerScreen()

class InicialMenu:
    # criação da tela
    inicialMenuCanvas = tkinter.Canvas(window, width=1280, height=720)
    inicialMenuCanvas.pack(fill="both", expand=True)

    # adiciona a imagem no fundo da tela
    inicialMenuImage = tkinter.PhotoImage(file="Assets/Images/InicialMenu.png")
    inicialMenuImageBackground = inicialMenuCanvas.create_image(0, 0, image=inicialMenuImage, anchor="nw")

    # adiciona o botão de jogar na tela
    playButtonImage = tkinter.PhotoImage(file="Assets/Images/PlayButton.png")
    playButton = tkinter.Button(window, image=playButtonImage, bd=0, fg="#004AAD", highlightbackground="#004AAD", activebackground="#004AAD", background="#004AAD", command=Functions.play)
    playButtonLabel = inicialMenuCanvas.create_window(500, 350, anchor="nw", window=playButton)

# roda a janela principal em looping
window.mainloop()
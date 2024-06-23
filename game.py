import tkinter as tk
import random

# Criação da janela principal do jogo
window = tk.Tk()
window.geometry("1280x720")
window.title("Passa Repassa")

# Ícone personalizado
icon = tk.PhotoImage(file="Assets/Images/Logo.png")
window.iconphoto(False, icon)

# Criação do canvas principal
canvas = tk.Canvas(window, width=1280, height=720)
canvas.pack(fill="both", expand=True)

# Dados do jogo
questions_answers = {
    "Qual é o maior planeta do sistema solar?": "júpiter",
    "Quem escreveu 'Dom Quixote'?": "miguel de cervantes",
    "Quantos continentes existem?": "7",
    "Quem pintou a Mona Lisa?": "leonardo da vinci",
    "Quanto é 7 vezes 8?": "56",
    "Qual é a capital do Brasil?": "brasília",
    "Quem foi o primeiro presidente do Brasil?": "deodoro da fonseca",
    "Quantos lados tem um triângulo?": "3",
    "Quem descobriu a gravidade?": "isaac newton",
    "Quantos oceanos existem na Terra?": "cinco",
    "Quem foi Leonardo da Vinci?": "pintor",
    "Qual é a cor oposta ao vermelho no círculo cromático?": "verde",
    "Qual é a capital da França?": "paris",
    "Quem inventou a lâmpada elétrica?": "thomas edison",
    "Qual é a maior cordilheira do mundo?": "cordilheira dos andes",
    "Qual é o símbolo químico do oxigênio?": "o",
    "Quem foi o inventor do telefone?": "alexander graham bell",
    "Quantos planetas têm anéis em nosso sistema solar?": "4",
    "Quem escreveu 'Romeu e Julieta'?": "william shakespeare",
    "Qual é o maior mamífero terrestre?": "elefante africano",
    "Quem foi o primeiro homem a pisar na Lua?": "neil armstrong",
    "Quem foi Albert Einstein?": "físico",
    "Qual é a cor do cavalo branco de Napoleão?": "branco",
    "Quem pintou a Capela Sistina?": "michelangelo",
    "Quantos jogadores compõem um time de futebol?": "11",
    "Quem foi Cleópatra?": "rainha do egito",
    "Qual é o número de meses em um ano bissexto?": "12",
    "Quem descobriu a penicilina?": "alexander fleming",
    "Qual é o maior deserto do mundo?": "deserto do saara",
    "Qual é a capital da Espanha?": "madrid",
    "Quem escreveu 'A Odisséia'?": "homero",
    "Quem foi o fundador da Microsoft?": "bill gates",
    "Quantos graus tem um ângulo reto?": "90",
    "Quem foi Galileu Galilei?": "astrônomo",
    "Qual é a capital do Canadá?": "ottawa",
    "Quem descobriu a América?": "cristóvão colombo",
    "Qual é o segundo planeta do sistema solar?": "vênus",
    "Quem foi Van Gogh?": "pintor",
    "Qual é a cor da esmeralda?": "verde",
    "Quem criou a Teoria da Relatividade?": "albert einstein",
    "Quantos lados tem um octógono?": "8",
    "Quem foi Martin Luther King Jr.?": "líder dos direitos civis",
    "Qual é o maior estado do Brasil em área?": "amazonas",
    "Quem escreveu 'A Divina Comédia'?": "dante alighieri",
    "Quem foi Isaac Newton?": "físico",
    "Qual é a capital da Argentina?": "buenos aires",
    "Quem inventou o avião?": "santos dumont",
    "Quantos anos tem um século?": "100",
    "Quem descobriu o Brasil?": "pedro álvares cabral"
}

# Referências de imagens
paths = {
    "backgroundImage": [
        "Assets/Images/InicialMenu.png",
        "Assets/Images/Player1Screen.png",
        "Assets/Images/Player2Screen.png",
        "Assets/Images/TimeOutScreen.png",
        "Assets/Images/LoseScreen.png",
        "Assets/Images/WinScreen.png",
        "Assets/Images/ProtectionScreen.png",
        "Assets/Images/DrawScreen.png",
        "Assets/Images/Player1WinScreen.png",
        "Assets/Images/Player2WinScreen.png"
    ],
    "icons": [
        "Assets/Images/PlayButton.png",
        "Assets/Images/Shield.png",
        "Assets/Images/Rocket.png",
        "Assets/Images/Clock.png",
        "Assets/Images/SubmitArrow.png",
        "Assets/Images/Cross.png",
        "Assets/Images/ResumeButton.png"
    ]
}

# Referências de cores
background_colors = {
    "player1": "#0A3A7B",
    "player2": "#9D1C1C"
}

# Dados dos jogadores
players = {
    "player1": {
        "points": 0,
        "inv": {
            "shield": 0,
            "timeFreezer": 0,
            "doublePoints": 0
        },
        "shield_active": False,
        "double_points_active": False,
        "time_freeze_active": False
    },
    "player2": {
        "points": 0,
        "inv": {
            "shield": 0,
            "timeFreezer": 0,
            "doublePoints": 0
        },
        "shield_active": False,
        "double_points_active": False,
        "time_freeze_active": False
    }
}

round = 0
maxRound = 20
current_player = "player1"
questions = list(questions_answers.keys())
current_question_index = random.randint(0, len(questions) - 1)
time_left = 15
timer_running = True
timer_id = None
power_up_index = 5
original_time_left = 15  # Variável para armazenar o tempo original

def canvas_cleaner():
    widgets = canvas.find_all()
    for widget in widgets:
        canvas.delete(widget)

def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"

def player_screen(player, time_left):
    global timer_running, original_time_left, power_up_quantity_id, answer_entry
    original_time_left = time_left
    timer_running = True
    canvas_cleaner()
    
    # Add the background image
    bg_index = 1 if player == "player1" else 2
    background_image = tk.PhotoImage(file=paths["backgroundImage"][bg_index])
    canvas.background_image = background_image  # Prevent garbage collection
    canvas.create_image(0, 0, anchor="nw", image=background_image)
    
    # Add question text
    canvas.create_text(400, 250, anchor="nw", font=("System", 32), fill="white", text=questions[current_question_index])
    
    # Add player scores
    canvas.create_text(1080, 75, anchor="nw", font=("System", 40), fill="#004AAD", text=str(players["player1"]["points"]))
    canvas.create_text(1125, 75, anchor="nw", font=("System", 40), fill="white", text="-")
    canvas.create_text(1150, 75, anchor="nw", font=("System", 40), fill="#D12424", text=str(players["player2"]["points"]))
    
    # Add answer entry
    answer_entry = tk.Entry(window, border=0, bd=0, fg="black", font=("System", 20), highlightbackground="#FFF7EC", background="#FFF7EC")
    answer_entry.bind("<Return>", submit_answer)
    canvas.create_window(465, 360, width=325, height=50, anchor="nw", window=answer_entry)
    
    # Add submit button
    submit_button_image = tk.PhotoImage(file=paths["icons"][4])
    submit_button = tk.Button(window, image=submit_button_image, bd=0, activebackground="#A8A39B", background="#A8A39B", command=lambda: submit_answer(None))
    submit_button.image = submit_button_image  # Prevent garbage collection
    canvas.create_window(799, 368, anchor="nw", window=submit_button)
    
    # Add power up buttons and quantities
    icons_positions = [(931, 583), (1035, 583), (1143, 583)]
    power_names = ['shield', 'doublePoints', 'timeFreezer']
    color_key = "player1" if player == "player1" else "player2"
    for i, icon in enumerate(paths["icons"][1:4]):
        power_name = power_names[i]
        power_up_image = tk.PhotoImage(file=icon)
        power_up_button = tk.Button(window, image=power_up_image, bd=0, activebackground=background_colors[color_key], background=background_colors[color_key], command=lambda p=player, pw=power_name: use_power_up(p, pw))
        power_up_button.image = power_up_image  # Prevent garbage collection
        canvas.create_window(icons_positions[i][0], icons_positions[i][1], anchor="nw", window=power_up_button)
        power_up_quantity_id = canvas.create_text(icons_positions[i][0] + 40, icons_positions[i][1] + 50, anchor="nw", font=("System", 20), fill="white", text=f"x{players[player]['inv'][power_name]}")
    
    update_timer(time_left)

def update_timer(time_left):
    global timer_running, timer_id
    if time_left >= 0 and timer_running:
        timer_text = format_time(time_left)
        canvas_cleaner_text("timer_text")
        canvas.create_text(570, 130, anchor="nw", font=("System", 40), fill="white", text=timer_text, tag="timer_text")
        timer_id = canvas.after(1000, update_timer, time_left - 1)
    elif time_left < 0:
        end_round("time_out")

def canvas_cleaner_text(item):
    canvas.delete(item)

def submit_answer(event):
    global current_player, answer_entry
    answer = answer_entry.get()
    correct_answer = questions_answers[questions[current_question_index]]
    if answer.lower() == correct_answer:
        points_to_add = 2 if players[current_player]["double_points_active"] else 1
        if players[current_player]["time_freeze_active"]:
            players[current_player]["time_freeze_active"] = False
            resume_time()  # Reinicia o temporizador se congelado
        if players[current_player]["points"] >= players["player2"]["points"]:
            players[current_player]["points"] += points_to_add
        players[current_player]["double_points_active"] = False
        give_random_power(current_player)
        end_round("win")
    else:
        if players[current_player]["shield_active"]:
            players[current_player]["shield_active"] = False
            current_player = "player2" if current_player == "player1" else "player1"
            end_round("protected")
        else:
            end_round("lose")

def give_random_power(player):
    power = random.choice(list(players[player]["inv"].keys()))
    players[player]["inv"][power] += 1

def use_power_up(player, power):
    global timer_running, timer_id, time_left, original_time_left, power_up_index, power_up_quantity_id
    if players[player]['inv'][power] > 0:
        players[player]['inv'][power] -= 1
        if power == 'shield':
            players[player]['shield_active'] = True
            power_up_index = 1
        elif power == 'timeFreezer':
            if not players[player]['time_freeze_active']:
                players[player]['time_freeze_active'] = True
                power_up_index = 3
                original_time_left = time_left  # Armazena o tempo original
                time_left = 5999  # Define tempo para 999 segundos
                canvas.after_cancel(timer_id)
                timer_running = True
                update_timer(time_left)
        elif power == 'doublePoints':
            players[player]['double_points_active'] = True
            power_up_index = 2
        update_player_inventory(player)

def update_player_inventory(player):
    global power_up_index, power_up_quantity_id
    # Atualiza apenas o inventário do jogador sem reiniciar a tela
    icons_positions = [(935, 583), (1035, 583), (1135, 583)]
    power_names = ['shield', 'doublePoints', 'timeFreezer']
    for i, power_name in enumerate(power_names):
        power_up_image = tk.PhotoImage(file=paths["icons"][power_up_index])  # Ícone do relógio (Clock.png)
        canvas.power_up_image = power_up_image  # Prevent garbage collection
        power_up_used = canvas.create_image(142, 135, anchor="nw", image=power_up_image)
        canvas.itemconfig(power_up_quantity_id, text=f"x{players[player]['inv'][power_name]}") # atualiza o número de poderes
    
def resume_time():
    global timer_running, time_left
    timer_running = True
    time_left = original_time_left  # Restaura o tempo original
    canvas_cleaner_text("freeze_message")
    update_timer(time_left)

def end_round(result):
    global current_question_index, current_player, timer_running, time_left, original_time_left, round, maxRound
    canvas_cleaner()
    round += 1
    if round <= maxRound:
        if result == "win":
            background_image = tk.PhotoImage(file=paths["backgroundImage"][5])
        elif result == "lose":
            background_image = tk.PhotoImage(file=paths["backgroundImage"][4])
        elif result == "time_out":
            background_image = tk.PhotoImage(file=paths["backgroundImage"][3])
        elif result == "protected":
            background_image = tk.PhotoImage(file=paths["backgroundImage"][6])
    
        canvas.background_image = background_image  # Prevent garbage collection
        canvas.create_image(0, 0, anchor="nw", image=background_image)
    
        timer_running = False
        current_player = "player2" if current_player == "player1" else "player1"
        current_question_index = random.randint(0, len(questions) - 1)
        time_left = 15  # Reseta o tempo para a próxima rodada
        original_time_left = 15  # Reseta o tempo original para a próxima rodada
    
        window.after(2000, lambda: player_screen(current_player, time_left))
    else:
        if players["player1"]["points"] > players["player2"]["points"]:
            background_image = tk.PhotoImage(file=paths["backgroundImage"][8])
            background_color = "#004AAD"
        elif players["player1"]["points"] < players["player2"]["points"]:
            background_image = tk.PhotoImage(file=paths["backgroundImage"][9])
            background_color = "#D12424"
        else:
            background_image = tk.PhotoImage(file=paths["backgroundImage"][7])
            background_color = "#000000"

        canvas.background_image = background_image  # Prevent garbage collection
        canvas.create_image(0, 0, anchor="nw", image=background_image)

        resume_button_image = tk.PhotoImage(file=paths["icons"][6])
        resume_button = tk.Button(window, image=resume_button_image, bd=0, activebackground=background_color, background=background_color, command=menuInicial)
        resume_button.image = resume_button_image  # Prevent garbage collection
        canvas.create_window(490, 500, anchor="nw", window=resume_button)
    
        timer_running = False
        current_player = "player1"
        current_question_index = random.randint(0, len(questions) - 1)
        time_left = 15  # Reseta o tempo para a próxima rodada
        original_time_left = 15  # Reseta o tempo original para a próxima rodada
        round = 0 # Reseta o número de rodadas
        players["player1"]["points"] = 0 # Reseta od pontos do player 1
        players["player2"]["points"] = 0 # Reseta od pontos do player 2

def start_game():
    player_screen("player1", time_left)

# Menu inicial
def menuInicial():
    canvas_cleaner()
    background_image = tk.PhotoImage(file=paths["backgroundImage"][0])
    canvas.background_image = background_image  # Prevent garbage collection
    canvas.create_image(0, 0, anchor="nw", image=background_image)

    play_button_image = tk.PhotoImage(file=paths["icons"][0])
    play_button = tk.Button(window, image=play_button_image, bd=0, activebackground="#004AAD", background="#004AAD", command=start_game)
    play_button.image = play_button_image  # Prevent garbage collection
    canvas.create_window(500, 350, anchor="nw", window=play_button)

menuInicial()

window.mainloop()

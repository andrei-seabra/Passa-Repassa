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
    "Quantos continentes existem?": "7",
    "Quanto é 7 vezes 8?": "56",
    "Qual é a capital do Brasil?": "brasília",
    "Quantos lados tem um triângulo?": "3",
    "Quantos oceanos existem na Terra?": "5",
    "Qual é a capital da França?": "paris",
    "Qual é a maior cordilheira do mundo?": "andes",
    "Qual é o maior mamífero terrestre?": "elefante",
    "Qual é a cor do cavalo branco de Napoleão?": "branco",
    "Qual é o maior deserto do mundo?": "saara",
    "Qual é a capital da Espanha?": "madrid",
    "Quantos graus tem um ângulo reto?": "90",
    "Qual é o segundo planeta do sistema solar?": "vênus",
    "Qual é a cor da esmeralda?": "verde",
    "Quantos lados tem um octógono?": "8",
    "Qual é o maior estado do Brasil em área?": "amazonas",
    "Qual é a capital da Argentina?": "buenos aires",
    "Quantos anos tem um século?": "100",
    "Qual é a capital do Japão?": "tóquio",
    "Qual é o maior animal do mundo?": "baleia",
    "Qual é a fórmula da água?": "h2o",
    "Qual é a raiz quadrada de 64?": "8",
    "Qual é o idioma oficial do Japão?": "japonês",
    "Qual é a capital da Itália?": "roma",
    "Qual é o oceano da paz?": "pacífico",
    "Calcule a média dos números 4 e 8.": "6",
    "Calcule a média dos números 10, 7 e 4.": "7",
    "Qual é o produto de 6 e 4?": "24",
    "Qual é o quociente de 20 e 5?": "4",
    "Quantos minutos há em uma hora?": "60",
    "Quantos cm tem um metro?": "100",
    "Quantos lados tem um hexágono?": "6",
    "Quantos ovos têm em uma dúzia?": "12",
    "Está gostando do jogo?": "sim",
    "Qual é o país mais populoso?": "china",
    "Qual é o nome do presidente do país?": "lula",
    "Qual a cor da banana madura?": "amarelo",
    "Qual animal é o rei da selva?": "leão",
    "Quantas pernas tem uma aranha?": "8",
    "Quantos dedos há em 1 mão?": "5",
    "Qual o oposto de quente?": "frio",
    "O que respiramos?": "ar",
    "Qual é o menor mês do ano?": "fevereiro",
    "Quantos dias há em 1 semana?": "7",
    "Quantas cores tem o arco-íris?": "7",
    "Qual é o satélite natural da Terra?": "lua",
    "Que marca te dá asas?": "redbull",
    "O que é a Via Láctea?": "galáxia",
    "Qual a cor do céu?": "azul",
    "Qual é o nome do nosso planeta?": "terra",
    "Quantos segundos há em um minuto?": "60",
    "O que é, quanto mais se tira maior fica?": "buraco",
    "Qual o esporte mais popular do país?": "futebol",
    "Qual o planeta mais proxímo do sol?": "mercúrio",
    "Quantos meses têm 28 dias?": "12",
    "Qual a maior cidade do Brasil?": "são paulo",
    "Qual é o desenho de 1 gato e 1 rato?": "tom e jerry",
    "Qual o país de origem do sushi?": "japão",
    "Quantos dias tem 1 ano?": "365",
    "Qual o coletivo de peixe?": "cardume",
    "Qual o coletivo de lobo?": "alcateia",
    "Qual é a palavra mais conhecida?": "ok",
    "Que mês comemoramos a festa junina?": "junho",
    "O que tem 4 rodas e anda?": "veículo",
    "O que o boi nos dá?": "carne",
    '"Just Do It"': "nike",
    "O que tomamos de manhã?": "café",
    "O que a galinha bota?": "ovo",
    "Quem te dá aula?": "professor",
    "Qual a cor do camaro?": "amarelo"
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
max_round = 20
power_up_index = 5
current_player = "player1"
questions = list(questions_answers.keys())
questions_clone = questions
current_question_index = random.randint(0, len(questions_clone) - 1)
max_time = 25 # variável que controla quanto tempo cada rodada tem
time_left = max_time
timer_running = True
timer_id = None
original_time_left = 30  # Variável para armazenar o tempo original

def canvas_cleaner():
    widgets = canvas.find_all()
    for widget in widgets:
        canvas.delete(widget)

def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"

def player_screen(player, time_left):
    global timer_running, original_time_left, power_up_quantity_id, answer_entry, shield_quantity_id, double_points_quantity_id, time_freezer_quantity_id, answer_entry
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
        if power_name == 'shield':
            shield_quantity_id = canvas.create_text(icons_positions[i][0] + 40, icons_positions[i][1] + 50, anchor="nw", font=("System", 20), fill="white", text=f"x{players[player]['inv'][power_name]}")
        elif power_name == 'doublePoints':
            double_points_quantity_id = canvas.create_text(icons_positions[i][0] + 40, icons_positions[i][1] + 50, anchor="nw", font=("System", 20), fill="white", text=f"x{players[player]['inv'][power_name]}")
        elif power_name == 'timeFreezer':
            time_freezer_quantity_id = canvas.create_text(icons_positions[i][0] + 40, icons_positions[i][1] + 50, anchor="nw", font=("System", 20), fill="white", text=f"x{players[player]['inv'][power_name]}")

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
        players[current_player]["shield_active"] = False # Reseta o poder de escudo caso o player acerte
        if players[current_player]["time_freeze_active"]:
            players[current_player]["time_freeze_active"] = False
            resume_time()  # Reinicia o temporizador se congelado
        if players[current_player]["points"] >= players["player2"]["points"] or players[current_player]["points"] < players["player2"]["points"]:
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
    update_player_inventory(player)  # Atualiza o inventário do jogador ao receber um novo poder

def use_power_up(player, power):
    global timer_running, timer_id, time_left, original_time_left, power_up_index
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
    global shield_quantity_id, double_points_quantity_id, time_freezer_quantity_id, power_up_index
    # adiciona o ícone do poder ativado
    power_up_image = tk.PhotoImage(file=paths["icons"][power_up_index])  # Ícone do relógio (Clock.png)
    canvas.power_up_image = power_up_image  # Prevent garbage collection
    canvas.create_image(142, 135, anchor="nw", image=power_up_image)

    # Atualiza os textos de quantidade de poderes
    canvas.itemconfig(shield_quantity_id, text=f"x{players[player]['inv']['shield']}")
    canvas.itemconfig(double_points_quantity_id, text=f"x{players[player]['inv']['doublePoints']}")
    canvas.itemconfig(time_freezer_quantity_id, text=f"x{players[player]['inv']['timeFreezer']}")

def resume_time():
    global timer_running, time_left
    timer_running = True
    time_left = original_time_left  # Restaura o tempo original
    canvas_cleaner_text("freeze_message")
    update_timer(time_left)

def end_round(result):
    global current_question_index, current_player, timer_running, time_left, original_time_left, round, max_round, answer_entry, max_time, questions_clone, questions_answers
    canvas_cleaner()
    if current_question_index in questions_clone:
        del questions_clone[current_question_index] # Remove a pergunta que foi feita na rodada
    answer_entry.unbind("<Return>")
    round += 1
    if round <= max_round:
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
        time_left = max_time  # Reseta o tempo para a próxima rodada
        original_time_left = max_time  # Reseta o tempo original para a próxima rodada
        questions_clone = questions_answers # Reseta o dictionary de perguntas e respostas
    
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

        resume_button_image = tk.PhotoImage(file=paths["icons"][5])
        resume_button = tk.Button(window, image=resume_button_image, bd=0, activebackground=background_color, background=background_color, command=menuInicial)
        resume_button.image = resume_button_image  # Prevent garbage collection
        canvas.create_window(490, 500, anchor="nw", window=resume_button)
    
        timer_running = False
        current_player = "player1"
        current_question_index = random.randint(0, len(questions) - 1)
        time_left = max_time  # Reseta o tempo para a próxima rodada
        original_time_left = max_time  # Reseta o tempo original para a próxima rodada
        round = 0 # Reseta o número de rodadas
        for i, player in players.items(): # Reseta os pontos dos players
            player['points'] = 0

        for i, player in players.items(): # Reseta os poderes dos players
            player['inv']['shield'] = 0
            player['inv']['timeFreezer'] = 0
            player['inv']['doublePoints'] = 0
                

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

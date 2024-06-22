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
    "Quem descobriu o Brasil?": "pedro álvares cabral",
    "Qual o maior time do futebol brasileiro?": "flamengo"
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
        "Assets/Images/ProtectionScreen.png"
    ],
    "icons": [
        "Assets/Images/PlayButton.png",
        "Assets/Images/Shield.png",
        "Assets/Images/Rocket.png",
        "Assets/Images/Clock.png",
        "Assets/Images/SubmitArrow.png"
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

current_player = "player1"
current_question_index = 0
questions = list(questions_answers.keys())
time_left = 15
timer_running = True
timer_id = None
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
    global timer_running, original_time_left
    original_time_left = time_left
    timer_running = True
    canvas_cleaner()
    
    # Add the background image
    bg_index = 1 if player == "player1" else 2
    color_key = "player1" if player == "player1" else "player2"
    background_image = tk.PhotoImage(file=paths["backgroundImage"][bg_index])
    canvas.background_image = background_image  # Prevent garbage collection
    canvas.create_image(0, 0, anchor="nw", image=background_image)
    
    # Add question text
    canvas.create_text(400, 250, anchor="nw", font=("System", 32), fill="white", text=questions[current_question_index])
    
    # Add player scores
    canvas.create_text(1080, 75, anchor="nw", font=("System", 40), fill="#004AAD", text=str(players["player1"]["points"]))
    canvas.create_text(1125, 75, anchor="nw", font=("System", 40), fill="white", text="-")
    canvas.create_text(1150, 75, anchor="nw", font=("System", 40), fill="#D12424", text=str(players["player2"]["points"]))
    
    # Add power up display
    power_up_image = tk.PhotoImage(file=paths["icons"][3])  # Ícone do relógio (Clock.png)
    canvas.power_up_image = power_up_image  # Prevent garbage collection
    canvas.create_image(142, 135, anchor="nw", image=power_up_image)
    
    # Add answer entry
    answer_entry = tk.Entry(window, border=0, bd=0, fg="black", font=("System", 20), highlightbackground="#FFF7EC", background="#FFF7EC")
    canvas.create_window(465, 360, width=325, height=50, anchor="nw", window=answer_entry)
    
    # Add submit button
    submit_button_image = tk.PhotoImage(file=paths["icons"][4])
    submit_button = tk.Button(window, image=submit_button_image, bd=0, activebackground="#A8A39B", background="#A8A39B", command=lambda: submit_answer(answer_entry.get()))
    submit_button.image = submit_button_image  # Prevent garbage collection
    canvas.create_window(799, 368, anchor="nw", window=submit_button)
    
    # Add power up buttons and quantities
    icons_positions = [(930, 583), (1035, 583), (1140, 583)]
    power_names = ['shield', 'doublePoints', 'timeFreezer']
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

def submit_answer(answer):
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
            end_round("protected")
        else:
            end_round("lose")

def give_random_power(player):
    power = random.choice(list(players[player]["inv"].keys()))
    players[player]["inv"][power] += 1

def use_power_up(player, power):
    global timer_running, timer_id, time_left, original_time_left
    if players[player]['inv'][power] > 0:
        players[player]['inv'][power] -= 1
        if power == 'shield':
            players[player]['shield_active'] = True
        elif power == 'timeFreezer':
            if not players[player]['time_freeze_active']:
                players[player]['time_freeze_active'] = True
                original_time_left = time_left  # Armazena o tempo original
                time_left = 5999  # Define tempo para 999 segundos
                canvas.after_cancel(timer_id)
                timer_running = True
                update_timer(time_left)
        elif power == 'doublePoints':
            players[player]['double_points_active'] = True
        update_player_inventory(player)

def update_player_inventory(player):
    # Atualiza apenas o inventário do jogador sem reiniciar a tela
    icons_positions = [(930, 583), (1035, 583), (1140, 583)]
    power_names = ['shield', 'doublePoints', 'timeFreezer']
    for i, power_name in enumerate(power_names):
        power_up_quantity_id = canvas.create_text(icons_positions[i][0] + 40, icons_positions[i][1] + 50, anchor="nw", font=("System", 20), fill="white", text=f"x{players[player]['inv'][power_name]}")
    
def resume_time():
    global timer_running, time_left
    timer_running = True
    time_left = original_time_left  # Restaura o tempo original
    canvas_cleaner_text("freeze_message")
    update_timer(time_left)

def end_round(result):
    global current_question_index, current_player, timer_running, time_left, original_time_left
    canvas_cleaner()
    
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
    current_question_index = (current_question_index + 1) % len(questions)
    time_left = 15  # Reseta o tempo para a próxima rodada
    original_time_left = 15  # Reseta o tempo original para a próxima rodada
    
    window.after(2000, lambda: player_screen(current_player, time_left))

def start_game():
    player_screen("player1", time_left)

# Menu inicial
background_image = tk.PhotoImage(file=paths["backgroundImage"][0])
canvas.background_image = background_image  # Prevent garbage collection
canvas.create_image(0, 0, anchor="nw", image=background_image)

play_button_image = tk.PhotoImage(file=paths["icons"][0])
play_button = tk.Button(window, image=play_button_image, bd=0, activebackground="#004AAD", background="#004AAD", command=start_game)
play_button.image = play_button_image  # Prevent garbage collection
canvas.create_window(500, 350, anchor="nw", window=play_button)

window.mainloop()

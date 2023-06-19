
a_1 = " "
b_1 = " "
c_1 = " "
a_2 = " "
b_2 = " "
c_2 = " "
a_3 = " "
b_3 = " "
c_3 = " "

move = ""
move_order = 1
placed_before = []
player_sym = ""


def print_board():
    
    print(" ", " ", "A", "B", "C")
    print(" ", " ", "-", "-", "-")
    print("1", "|", a_1, b_1, c_1, "|")
    print("2", "|", a_2, b_2, c_2, "|")
    print("3", "|", a_3, b_3, c_3, "|")
    print(" ", " ", "-", "-", "-")
    
def get_player_move():
    global move
    move = str(input("Enter Move: "))
    move = move.upper()
    
def get_player_pos():
    global a_1, a_2, a_3, b_1, b_2, b_3, c_1, c_2, c_3, move_order, placed_before, player_sym
    
    if move_order % 2 == 0: 
        player_sym = "O"
    else:
        player_sym = "X"
    
    
    if move == "A1" and move not in placed_before: 
        a_1 = player_sym
    elif move == "A2" and move not in placed_before:
        a_2 = player_sym
    elif move == "A3" and move not in placed_before:
        a_3 = player_sym
    elif move == "B1" and move not in placed_before: 
        b_1 = player_sym
    elif move == "B2" and move not in placed_before: 
        b_2 = player_sym
    elif move == "B3" and move not in placed_before:
        b_3 = player_sym
    elif move == "C1" and move not in placed_before:
        c_1 = player_sym
    elif move == "C2" and move not in placed_before:
        c_2 = player_sym
    elif move == "C3" and move not in placed_before:
        c_3 = player_sym
    elif move == "EXIT" or move == "STOP":
        exit()
    else:
        print("Not valid move, re enter!")
        move_order -= 1
        
    placed_before.append(move)
    

def check_for_victory():
    if (a_1 == a_2) and (a_2 == a_3) and a_3 != " ":
        print("Player", player_sym, "WON the Game!1")
        exit()
    elif (b_1 == b_2) and (b_2 == b_3) and b_3 != " ":
        print("Player", player_sym, "WON the Game!2")
        exit()
    elif (c_1 == c_2) and (c_2 == c_3) and c_3 != " ":
        print("Player", player_sym, "WON the Game!3")
        exit()
    elif (a_1 == b_1) and (b_1 == c_1) and c_1 != " ":
        print("Player", player_sym, "WON the Game!4")
        exit()
    elif (a_2 == b_2) and (b_2 == c_2) and c_2 != " ":
        print("Player", player_sym, "WON the Game!5")
        exit()
    elif (a_3 == b_3) and (b_3 == c_3) and c_3 != " ":
        print("Player", player_sym, "WON the Game!6")
        exit()
    elif (a_1 == b_2) and (b_2 == c_3) and c_3 != " ":
        print("Player", player_sym, "WON the Game!7")
        exit()
    elif (a_3 == b_2) and (b_2 == c_1) and c_1 != " ":
        print("Player", player_sym, "WON the Game!8")
        exit()

print_board()

while True:
    get_player_move()
    get_player_pos()
    print_board()
    check_for_victory()
    
    move_order += 1
    
    
    

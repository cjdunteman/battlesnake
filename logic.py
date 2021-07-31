def avoid_my_neck(my_head, my_body, possible_moves):
    my_neck = my_body[1]

    if my_neck["x"] < my_head["x"]:  # my neck is left of my head
        possible_moves.remove("left")
    elif my_neck["x"] > my_head["x"]:  # my neck is right of my head
        possible_moves.remove("right")
    elif my_neck["y"] < my_head["y"]:  # my neck is below my head
        possible_moves.remove("down")
    elif my_neck["y"] > my_head["y"]:  # my neck is above my head
        possible_moves.remove("up")

    return possible_moves

def avoid_my_body(my_head, my_body, possible_moves):
    if my_head["x" - 1] in my_body and my_head["y"] == my_body[my_head["x" - 1]]:
        possible_moves.remove("left")

    if my_head["x" + 1] in my_body and my_head["y"] == my_body[my_head["x" + 1]]:
        possible_moves.remove("right")

    if my_head["x"] in my_body and my_head["y" + 1] == my_body[my_head["x"]]:
        possible_moves.remove("up")

    if my_head["x"] in my_body and my_head["y" - 1] == my_body[my_head["x"]]:
        possible_moves.remove("down")
    
    return possible_moves

def choose_move(): 
    my_head = data["you"]["head"]
    my_body = data["you"]["body"]

    possible_moves = ["up", "down", "left", "right"]
    
    possible_moves = avoid_my_neck(my_head, my_body, possible_moves)

    possible_moves = avoid_my_body(my_head, my_body, possible_moves)

    board_height = data["board"]["height"]
    board_width = data["board"]["width"]
    board_hazards = data["board"]["hazards"]

    print(f"FINAL POSSIBLE MOVES: {possible_moves}")

    move = random.choice(possible_moves)

    return move

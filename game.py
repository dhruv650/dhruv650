def with_process():
    player_input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    def layout():
        print(f" {player_input_list[0]} | {player_input_list[1]} | {player_input_list[2]}")
        print(f"---|---|---")
        print(f" {player_input_list[3]} | {player_input_list[4]} | {player_input_list[5]}")
        print(f"---|---|---")
        print(f" {player_input_list[6]} | {player_input_list[7]} | {player_input_list[8]}")
        a = " "
        return a
    layout()
    while True:
        current_player = "Player 1"

        user_input = int(input(f"Chance of {current_player}: "))
        if user_input in player_input_list:
            index = player_input_list.index(user_input)
            player_input_list[index] = "x" if current_player == "Player 1" else "o"
            print(layout())
        if player_input_list[0] == player_input_list[3] == player_input_list[6] or player_input_list[0] == player_input_list[1] == player_input_list[2] or player_input_list[2] == player_input_list[5] == player_input_list[8] or player_input_list[6] == player_input_list[7] == player_input_list[8] or player_input_list[6] == player_input_list[4] == player_input_list[2] or player_input_list[6] == player_input_list[7] == player_input_list[8]:
                print("Player 1 wins")
                break
        current_player = "Player 2"
        user_input = int(input(f"Chance of {current_player}: "))
        if user_input in player_input_list:
            index = player_input_list.index(user_input)
            player_input_list[index] = "x" if current_player == "Player 1" else "o"
            print(layout())
        if player_input_list[0] == player_input_list[3] == player_input_list[6] or player_input_list[0] == player_input_list[1] == player_input_list[2] or player_input_list[2] == player_input_list[5] == player_input_list[8] or player_input_list[6] == player_input_list[7] == player_input_list[8] or player_input_list[6] == player_input_list[4] == player_input_list[2] or player_input_list[6] == player_input_list[7] == player_input_list[8]:
                print("Player 2 wins")
                break

with_process()
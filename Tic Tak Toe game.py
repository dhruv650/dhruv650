#  Tic Tac Toe Game 
import random
print("Tic Tac Toe Game".center(80))
inpt = int(input(" First Chance computer(1)/user(2)"))
def game():
	_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	def layout():
		print(f"{_list[0]} | {_list[1]} | {_list[2]}")
		print("--|---|--")
		print(f"{_list[3]} | {_list[4]} | {_list[5]}")
		print("--|---|--")
		print(f"{_list[6]} | {_list[7]} | {_list[8]}")
		a = ""
		return a
	layout()
	while True:
		current = "Player 1"

		user_input = int(input("Enter the number: "))
		if user_input in _list:
			index = _list.index(user_input)
			_list[index] = "X" if current == "Player 1" else "O"
			print(layout())
		if _list[0] == _list[3] == _list[6] or _list[0]  == _list[1] == _list[2] or _list[2] == _list[5] == _list[8] or _list[6] == _list[7] == _list[8] or _list[6] == _list[4] == _list[2] or _list[6] == _list[7] == _list[8]:
			print("Player 1 wins")
			break
		current = "computer"
		for i in _list:
			if str(type(i)) != "<class 'str'>":
				random_number = random.choice(_list)
		if random_number in _list:
			index = _list.index(random_number)
			_list[index] = "O" if current == "computer" else "x"
			print(layout())
		if _list[0] == _list[3] == _list[6] or _list[0] == _list[1] == _list[2] or _list[2] == _list[5] == _list[8] or _list[6] == _list[7] == _list[8] or _list[6] == _list[4] == _list[2] or _list[6] == _list[7] == _list[8]:
			print("Computer wins!")
			break
game()
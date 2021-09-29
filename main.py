
import random
import enemy


player_name  =  input("what is your name:")
HP  =   100
EXP =  0
player_Coins   =   0
enemies_killed	  =  0


def display_menu():
	print( "\nElija uno ")
	print( "1 - Explorar")
	print( "2 - Descanso")
	print("3 - Mochila")
	print("4 - Mostrar estadísticas")
	print("5 - Salir")

def explore():
  global player_Coins
  locations = ["Stranger Forest", "Dark Dugeon", " Mountain", " Hot Desert", "Path"]
  print(f"\nYou have decided to explore {random.choice(locations)}")
  chance =  random.randint(0,1)
  if chance == 1:
    print("\nGreat you found a chest")
    treasure_Coins = random.randrange(0, 50, 5)
    print(f"You find {treasure_Coins} Coins.")
    player_Coins = player_Coins + treasure_Coins
    battle()

def  show_stats ():
	print ( f"\nHP { HP } " )
	print(f"EXP {EXP}")
	print(f"Coins {player_Coins}")
	print(f"Enemy Kills {enemies_killed}")


def run_game():
	global HP
	user_choice = ""
	intro()
	while user_choice != 5 and HP > 0:
		display_menu()
		user_choice = int(input("What do you prefer to do:"))
		if user_choice == 1:
			explore()
		elif user_choice == 2:
			print()
			print("Take a rest  drink a coke")
			player_rest()
		elif user_choice == 4:
			show_stats()
		elif user_choice == 3:
			view_backpack()


def intro():
	print(
	    f"\nIt was once in a distant place (Breoris Kingdom) where a warrior lived {player_name} this was a kingdom that lived ruled by a tyrant King (Mr. B) who suffered from making people write long decrees. In this kingdom (the poorest part) a boy who dreamed of being a warrior but one of the long decrees of the tyrant king (Mr B) was that no one could leave the kingdom without his written permission and signed by his second general in command (Mr Ba)"
	)

	print(
	    f"\nWell our character escaped to fulfill his dream, causing him to climb the walls of the kingdom one night but now it is your turn to help {player_name} with his adventure"
	)


def player_rest():
	global HP
	if HP == 100:
		print("\nSorry you have your health al maximu")
		print()
	else:
		HP = HP + 25
		if HP > 100:
			HP = 100
		print(f"\nYour health has increased {HP}")


def battle():
	global HP, enemies_killed, EXP
	enemy1 = enemy.Enemy()
	print(f"\nOH OH you find a {enemy1.get_name()}")
	print(f"And it has a health of {enemy1.get_health()}")
	while enemy1.get_health() >= 0:
		print("The enemy attack you!!")
		HP -= enemy1.attack()
		print(f"\nNow, You have a HP of {HP}")
		if HP <= 0:
			print("You are dead")
			break
		print("1-Attack")
		print("2-Flee")
		combat_move = int(input("What do you want to do:"))
		if combat_move == 1:
			print("\nYou attack the enemy")
			EXP += 5
			enemy1.set_health(enemy1.get_health() - random.randint(5, 20))
			print(f"The enemy have a health of {enemy1.get_health()}")
			if enemy1.get_health() <= 0:
				print("!!You wins!!")
				enemies_killed += 1
		elif combat_move == 2:
			print("You dicided to pass")
			break


def view_backpack():
	print("\nSorry, You can use this now")


run_game()

# -*- coding:utf8 -*-
import random

humanScore = 0
robotScore = 0

def game():
	humanInput = raw_input("Please choice 1:jiandao,2:shitou,3:bu  ===> ")
	humanChoice = ""
	if humanInput == "1":
		humanChoice = "jiando"
	elif humanInput == "2":
		humanChoice = "shitou"
	elif humanInput == "3":
		humanChoice = "bu"
	else:
		print("error input")
		return

	robotChoice = random.choice(["jiando","shitou","bu"])

	if humanChoice == robotChoice:
		print("try again!!! good luck.")
		return

	humanWin = False

	if humanChoice == "jiandao" and robotChoice == "bu":
		humanWin = True

	if humanChoice == "shitou" and robotChoice == "jiandao":
		humanWin = True

	if humanChoice == "bu" and robotChoice == "shitou":
		humanWin = True

	print("human choice : "+humanChoice)
	print("robot choice : "+robotChoice)
	if humanWin:
		print("you win!")
		global humanScore
		humanScore = humanScore+1
	else:
		print("you lose!")
		global robotScore
		robotScore = robotScore+1

def show_logo():
	gameLogoFile = open("logo.txt")
	logos = gameLogoFile.readlines()
	for l in logos:
		print l
	gameLogoFile.close()

def save(record):
	gameSaveFile = open("game.dat","w")
	gameSaveFile.writelines(record)
	gameSaveFile.close()

def main():
	show_logo()

	gameRounds = raw_input("请输入游戏的回合数:")
	for i in range(int(gameRounds)):
		print("/////////////// round %d /////////////////" % int(i+1))
		game()

	gameRecord = "human vs robot is %d : %d " %(humanScore,robotScore)
	print gameRecord

	save(gameRecord)


if __name__ == '__main__':
	main()


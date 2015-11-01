from Player import *

execfile("MancalaBoard.py")
mb=MancalaBoard()
mb.hostGame(Player(1,Player.HUMAN),Player(2,Player.HUMAN))	


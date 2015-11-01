from Player import *

execfile("MancalaBoard.py")
mb=MancalaBoard()
mb.hostGame(Player(1,Player.ABPRUNE,11),MyPlayer(2,Player.ABPRUNE,11))	

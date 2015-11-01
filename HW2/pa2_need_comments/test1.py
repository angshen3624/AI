from Player import *


execfile("MancalaBoard.py")
mb=MancalaBoard()

mb.hostGame(asi031(1,Player.CUSTOM,10),asi031(2,Player.CUSTOM,10))	
#mb.hostGame(MyPlayer(1,Player.CUSTOM,10),wml431(2,Player.CUSTOM,10))

#mb.hostGame(wml431(1,Player.ABPRUNE,9),MyPlayer(2,Player.ABPRUNE,9))	
#mb.hostGame(MyPlayer(1,Player.MINIMAX,6),MyPlayer(2,Player.MINIMAX,6))

#mb.hostGame(MyPlayer(1,Player.ABPRUNE,6),MyPlayer(2,Player.ABPRUNE,6))
#mb.hostGame(MyPlayer(1,Player.CUSTOM,11),wml431(2,Player.CUSTOM,11))


# us vs minmin: ABvsAB  			9,10,11 first go win.
# us vs minmin: Custom vs Custom    9, 
# minmin vs us: ABvsAB 			 	9,10,11 second go win(us),   
#  #xzr699(Player):

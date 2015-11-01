# asi031.py
# Jixiao Ma:jmq856   Ang Shen: asi031  Huaipei Lu: hlv624
# 4/19/2015

# Define a simple artificially intelligent player agent
# Define the alpha-beta pruning search algorithm
# Define the score function in the MancalaPlayer class
# Define a subclass named as "asi031" of the Player class


#from random import *
import random
from decimal import *
from copy import *
from MancalaBoard import *

# a constant
INFINITY = 1.0e400

class Player:
    """ A basic AI (or human) player """
    HUMAN = 0
    RANDOM = 1
    MINIMAX = 2
    ABPRUNE = 3
    CUSTOM = 4
    
    def __init__(self, playerNum, playerType, ply=0):
        """Initialize a Player with a playerNum (1 or 2), playerType (one of
        the constants such as HUMAN), and a ply (default is 0)."""
        self.num = playerNum
        self.opp = 2 - playerNum + 1
        self.type = playerType
        self.ply = ply

    def __repr__(self):
        """Returns a string representation of the Player."""
        return str(self.num)
        
    def minimaxMove(self, board, ply):
        """ Choose the best minimax move.  Returns (score, move) """
        move = -1
        score = -INFINITY
        turn = self
        for m in board.legalMoves(self):
            #for each legal move
            if ply == 0:
                #if we're at ply 0, we need to call our eval function & return
                return (self.score(board), m)
            if board.gameOver():
                return (-1, -1)  # Can't make a move, the game is over
            nb = deepcopy(board)
            #make a new board
            nb.makeMove(self, m)
            #try the move
            opp = Player(self.opp, self.type, self.ply)
            s = opp.minValue(nb, ply-1, turn)
            #and see what the opponent would do next
            if s > score:
                #if the result is better than our best score so far, save that move,score
                move = m
                score = s
        #return the best score and move so far
        return score, move

    def maxValue(self, board, ply, turn):
        """ Find the minimax value for the next move for this player
        at a given board configuation. Returns score."""
        if board.gameOver():
            return turn.score(board)
        score = -INFINITY
        for m in board.legalMoves(self):
            if ply == 0:
                #print "turn.score(board) in max value is: " + str(turn.score(board))
                return turn.score(board)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            nextBoard.makeMove(self, m)
            s = opponent.minValue(nextBoard, ply-1, turn)
            #print "s in maxValue is: " + str(s)
            if s > score:
                score = s

        return score
    
    def minValue(self, board, ply, turn):
        """ Find the minimax value for the next move for this player
            at a given board configuation. Returns score."""
        if board.gameOver():
            return turn.score(board)
        score = INFINITY
        for m in board.legalMoves(self):
            if ply == 0:
                #print "turn.score(board) in min Value is: " + str(turn.score(board))
                return turn.score(board)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            nextBoard.makeMove(self, m)
            s = opponent.maxValue(nextBoard, ply-1, turn)
            #print "s in minValue is: " + str(s)
            if s < score:
                score = s
        return score


    # The default player defines a very simple score function
    # You will write the score function in the MancalaPlayer below
    # to improve on this function.
    def score(self, board):
        """ Returns the score for this player given the state of the board """
        if board.hasWon(self.num):
            return 100.0
        elif board.hasWon(self.opp):
            return -100.0
        else:
            return 50

    # You should not modify anything before this point.
    # The code you will add to this file appears below this line.
	
	# ab-pruning function.
	# Given state and ply， return move and the corresponding score
    def alphaBetaMove(self, board, ply):
        """ Choose a move with alpha beta pruning.  Returns (score, move) """
        move = -1
        score = -INFINITY
        turn = self
        alpha = -INFINITY
        beta = INFINITY
        mv_lst=board.legalMoves(self)
        for m in mv_lst:
            #for each legal move
            if ply == 0:
                #if we're at ply 0, we need to call our eval function & return
                return (self.score(board), m)
            if board.gameOver():
                return (-1, -1)  # Can't make a move, the game is over
            nb = deepcopy(board)
            #make a new board
            nb.makeMove(self, m)
            #try the move
            opp = Player(self.opp, self.type, self.ply)
            s = opp.minValue_ab(nb,  alpha , beta , ply-1,turn)
            #and see what the opponent would do next
            if s > score:
                #if the result is better than our best score so far, save that move,score
                move = m
                score = s

        #return the best score and move so far
        return score, move


    def maxValue_ab(self, board, a,b,ply, turn):
        """ Find the minimax value for the next move for this player
        at a given board configuation. Returns score."""
        if board.gameOver():
            return turn.score(board)
        score = -INFINITY
        mv_lst=board.legalMoves(self)
       # random.shuffle(mv_lst)
        for m in mv_lst:
            if ply == 0:
                #print "turn.score(board) in max value is: " + str(turn.score(board))
                return turn.score(board)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            nextBoard.makeMove(self, m)
            s = opponent.minValue_ab(nextBoard,a,b,ply-1, turn)
            #print "s in maxValue is: " + str(s)
            score=max(score,s)
            if score >= b :
                return score
            a=max(a,score)
        return score
    
    def minValue_ab(self, board, a,b,ply, turn):
        """ Find the minimax value for the next move for this player
            at a given board configuation. Returns score."""
        if board.gameOver():
            return turn.score(board)
        score = INFINITY
        mv_lst=board.legalMoves(self)
        for m in mv_lst:
            if ply == 0:
                return turn.score(board)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            nextBoard.makeMove(self, m)
            s = opponent.maxValue_ab(nextBoard, a,b,ply-1, turn)
            score=min(score,s)
            if score<= a:
                return score
            b=min(b,score)
        return score

     def chooseMove(self, board):
        """ Returns the next move that this player wants to make """
        if self.type == self.HUMAN:
            move = input("Please enter your move:")
            while not board.legalMove(self, move):
                print move, "is not valid"
                move = input( "Please enter your move" )
            return move
        elif self.type == self.RANDOM:
            move = choice(board.legalMoves(self))
            print "chose move", move
            return move
        elif self.type == self.MINIMAX:
            val, move = self.minimaxMove(board, self.ply)
            print self.num,"chose move", move, " with value", val
            return move
        elif self.type == self.ABPRUNE:
            val, move = self.alphaBetaMove(board,self.ply)
            print self.num,"chose move", move, " with value", val
            return move
        elif self.type == self.CUSTOM:
            # TODO: Implement a custom player
            # You should fill this in with a call to your best move choosing
            # function.  You may use whatever search algorithm and scoring
            # algorithm you like.  Remember that your player must make
            # each move in about 10 seconds or less.
            val,move = self.customMove(board)
            print self.num,"chose move", move, " with value", val
            return move
        else:
            print "Unknown player type"
            return -1

# custom player with better score function and improved ab-pruning approach
class asi031(Player):
    """ Defines a player that knows how to evaluate a Mancala gameboard
        intelligently """
    def __init__(self, playerNum, playerType, ply=0):
        """Initialize a Player with a playerNum (1 or 2), playerType (one of
        the constants such as HUMAN), and a ply (default is 0)."""
        self.num = playerNum
        self.opp = 2 - playerNum + 1
        self.type = playerType
        self.ply = ply
        self.count=0
    def score(self, board):
        """ Evaluate the Mancala board for this player """
		# check whether any of players wins the game 
        if board.hasWon(self.num):
            return 100.0
        elif board.hasWon(self.opp):
            return -100.0
		# if neither player wins the game, we consider two parameter
		#Param 1 is the distance to reach the winning status, 
		# in other word, it is the number of stones to reach 25
		#Param 2 is the difference in total number of stones in all cups and in mancala on both side
        # we weighted these two parameters the same, thus we simply added them together
		else:
            if self.num==1:
                a= 25 - board.scoreCups[self.opp - 1] +(board.scoreCups[0]-board.scoreCups[1]) + (sum(board.P1Cups) - sum(board.P2Cups))
                return a 
            else:
                a= 25 - board.scoreCups[self.opp - 1]+ (board.scoreCups[1]-board.scoreCups[0]) + (sum(board.P2Cups) - sum(board.P1Cups))       
                return a
	# An improved ab-pruning approach, which considers the extra move 
    def customMove(self, board, ply=10):
        """ Choose a move with alpha beta pruning.  Returns (score, move) """
        move = -1
        score = -INFINITY
        turn = self
        alpha = -INFINITY
        beta = INFINITY
        mv_lst=board.legalMoves(self)
        self.count+=1
        print "The ",self.count,"round:"
        # Hard coded move action
        if self.num==1 :   
            if self.count==1:    # if we move first
                return 0,3       # then we move the position 3
            elif self.count==2:  # we have an extra move
                return 0,6       # move position 6.

        elif self.num==2 :       # if oppo moves first
            if self.count==1:    # then our first move 
               if board.P1Cups[5]==0:   # if oppo's positon 6 is empty
                   return 0,2           # make move at postion 2
            elif self.count==2:         # extra move
               if board.P2Cups[1]!=0:   # if oppo could capture our marbles at postion 1 
                   return 0,1           # avoid being capture. make move at positon 1
        random.shuffle(mv_lst)
        for m in mv_lst:
            # for each legal move
            if ply == 0:
                # if we're at ply 0, we need to call our eval function & return
                return (self.score_custom(board,self.count), m)
            if board.gameOver():
                return (-1, -1)  # Can't make a move, the game is over
            nb = deepcopy(board)
            # make a new board
            flag=nb.makeMove(self, m)
            # try the move
            opp = asi031(self.opp, self.type, self.ply)
            if flag:
                num = asi031(self.num, self.type, self.ply)
                s = num.maxValue_custom(nb, alpha, beta, ply-1, turn)
            else:
                s = opp.minValue_custom(nb, alpha, beta, ply-1,turn)
            # See what the opponent would do next

            if s > score:
                #if the result is better than our best score so far, save that move,score
                move = m
                score = s
        #return the best score and move so far
        return score, move

    def maxValue_custom(self, board, a,b,ply, turn):
        """ Find the minimax value for the next move for this player
        at a given board configuation. Returns score."""
        if board.gameOver():
            return turn.score(board)
        score = -INFINITY
        mv_lst=board.legalMoves(self)
        for m in mv_lst:
            if ply == 0:
                return turn.score(board)
            # make a new player to play the other side
            opponent = asi031(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            # To see whether the next move will cause a extra move
            flag=nextBoard.makeMove(self, m)
            # if we could get an extra move, continue max's turn
            # else switch to min's turn 
            if flag:
                num=asi031(self.num, self.type, self.ply)
                s=num.maxValue_custom(nextBoard,a,b,ply-1,turn)
            else:
                s = opponent.minValue_custom(nextBoard,a,b,ply-1, turn)
            score=max(score,s)
            if score >= b :
                return score
            a=max(a,score)
        return score
    
    def minValue_custom(self, board, a,b,ply, turn):
        """ Find the minimax value for the next move for this player
            at a given board configuration. Returns score."""
        if board.gameOver():
            return turn.score(board)
        score = INFINITY
        mv_lst = board.legalMoves(self)
        for m in mv_lst:
            if ply == 0:
                return turn.score(board)
            # make a new player to play the other side
            opponent = asi031(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            # To see whether the next move will cause a extra move
            flag=nextBoard.makeMove(self, m) 
            # if we could get an extra move, continue min's turn
            # else switch to max's turn 
            if flag:   
                num = asi031(self.num, self.type, self.ply)
                s = num.minValue_custom(nextBoard,a,b,ply-1,turn)
            else:
                s = opponent.maxValue_custom(nextBoard,a,b,ply-1, turn)
            score = min(score,s)
            if score<= a:
                return score
            b = min(b,score)
        return score

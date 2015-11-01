# File: Player.py
# Author(s) names AND netid's:
# Date: 
# Defines a simple artificially intelligent player agent
# You will define the alpha-beta pruning search algorithm
# You will also define the score function in the MancalaPlayer class,
# a subclass of the Player class.


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
            if self.num==1:
               # if board.scoreCups[0] > 24:
                #    return 100.0
                a= 1 * (board.scoreCups[0]-board.scoreCups[1]) + (sum(board.P1Cups) - sum(board.P2Cups))#+(board.scoreCups[0]-24)
                return a 
            else:
            #    if board.scoreCups[1] > 24:
              #      return 100.0
                a= 1 * (board.scoreCups[1]-board.scoreCups[0]) + (sum(board.P2Cups) - sum(board.P1Cups))#+(board.scoreCups[1]-24)       
                return a

    # You should not modify anything before this point.
    # The code you will add to this file appears below this line.

    # You will write this function (and any helpers you need)
    # You should write the function here in its simplest form:
    #   1. Use ply to determine when to stop (when ply == 0)
    #   2. Search the moves in the order they are returned from the board's
    #       legalMoves function.
    # However, for your custom player, you may copy this function
    # and modify it so that it uses a different termination condition
    # and/or a different move search order.
    def alphaBetaMove(self, board, ply):
        """ Choose a move with alpha beta pruning.  Returns (score, move) """
        #print "Alpha Beta Move not yet implemented"
        """ Choose the best minimax move.  Returns (score, move) """
        move = -1
        score = -INFINITY
        turn = self
        alpha = -INFINITY
        beta = INFINITY
        mv_lst=board.legalMoves(self)
     #  random.shuffle(mv_lst)
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
        #random.shuffle(mv_lst)
        for m in mv_lst:
            if ply == 0:
                #print "turn.score(board) in min Value is: " + str(turn.score(board))
                return turn.score(board)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            nextBoard.makeMove(self, m)
            s = opponent.maxValue_ab(nextBoard, a,b,ply-1, turn)
            #print "s in minValue is: " + str(s)
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
            print "chose move", move, " with value", val
            return move
        elif self.type == self.ABPRUNE:
            val, move = self.alphaBetaMove(board,self.ply)
            print "chose move", move, " with value", val
            return move
        elif self.type == self.CUSTOM:
            # TODO: Implement a custom player
            # You should fill this in with a call to your best move choosing
            # function.  You may use whatever search algorithm and scoring
            # algorithm you like.  Remember that your player must make
            # each move in about 10 seconds or less.
            print "Custom player not yet implemented"
            return -1
        else:
            print "Unknown player type"
            return -1


# Note, you should change the name of this player to be your netid
class MyPlayer(Player):
    """ Defines a player that knows how to evaluate a Mancala gameboard
        intelligently """

    def score(self, board):
        """ Evaluate the Mancala board for this player """
        # Currently this function just calls Player's score
        # function.  You should replace the line below with your own code
        # for evaluating the board
        if board.hasWon(self.num):
            return 100.0
        elif board.hasWon(self.opp):
            return -100.0
        else:
            if self.num==1:
                if board.scoreCups[0] > 24:
                    return 100.0
                a= 1*self.capture(board) + (board.scoreCups[0]-board.scoreCups[1]) + (sum(board.P1Cups) - sum(board.P2Cups))#+(board.scoreCups[0]-24)
                return a 
            else:
                if board.scoreCups[1] > 24:
                    return 100.0
                a= 1*self.capture(board) + (board.scoreCups[1]-board.scoreCups[0]) + (sum(board.P2Cups) - sum(board.P1Cups))#+(board.scoreCups[1]-24)       
                return a
    def capture(self, board):
        if self.num == 1:
            for pos in range(5):
                if board.P1Cups[pos] != 0:
                    last_pos = pos + board.P1Cups[pos]
                    if last_pos < 6 and board.P1Cups[last_pos] == 0:
                        return board.P2Cups[5-last_pos]

            return 0
        else:
            for pos in range(5):
                if board.P2Cups[pos] != 0:
                    last_pos = pos + board.P2Cups[pos]
                    if last_pos < 6 and board.P2Cups[last_pos] == 0:
                        return board.P1Cups[5-last_pos]

            return 0


# input file(.csv) is given as a command line argument
#-*-coding:utf-8-*-
class Player:
    def __init__(self,name): #player class
        self.name = name
        self.__point = 0
        self.__game = 0
        self.__set = 0
    def add_point(self,opponent):
        if self.__point == 30 :
            self.__point += 10
        elif self.__point == 40 and opponent.__point != 40 and opponent.__point != 'A' :
            self.add_game(opponent)
        elif self.__point == 'A':
            self.add_game(opponent)
        elif self.__point == 40 and opponent.__point == 40:
            self.__point = 'A'
        elif self.__point == 40 and opponent.__point == 'A':
            opponent.__point = 40
        else:
            self.__point += 15
    def add_game(self,opponent): #increementing
        global x1
        global y1
        global flag
        flag = 1 # in order to prevent the change of player 1 and 2 when it enters into add_game method
        self.__point = 0
        opponent.__point = 0
        self.__game += 1
        tmp = x1
        x1 = y1
        y1 = tmp
        if self.__game == 6 and opponent.__game <= 4:
            self.add_set()
        elif self.__game >=5 and opponent.__game >= 5:
            if self.__game - opponent.__game == 2:
                self.add_set(opponent)
    def add_set(self,opponent):
        self.__game = 0
        opponent.__game = 0
        self.__set += 1
class Score:
    global Iteration #score class
    Iteration = 0
    def __init__(self,state,a,b):
        global Iteration
        Iteration += 1
        print "Iteration:  {0}".format(Iteration)
        print "{1}  :  {0}".format(state,a.name)
        if x._Player__point == 40 and y._Player__point == 40:
            print "P1 Score: Deuce"
            print "P2 Score: Deuce"
        else:
            print "P1 Score: {0}".format(x._Player__point)
            print "P2 Score: {0}".format(y._Player__point)
        print "P1 Game Win Count: {0}".format(x._Player__game)
        print "P2 Game Win Count: {0}".format(y._Player__game)
        print "P1 Set Win Count: {0}".format(x._Player__set)
        print "P2 Set Win Count: {0}".format(y._Player__set)
p1 = Player("Player1")
p2 = Player("Player2")
def pointer(player):
    tmp = player
    return tmp
x = pointer(p1) #p1 starts the serve and x keeps track of the player receiving the ball
y = pointer(p2) #the one who doesnt have ball at time of T
import csv
import sys
f = open(sys.argv[-1],'r')
f_csv = csv.reader(f,delimiter=' ')
x1 = x
y1 = y
flag = 0
for row in f_csv:
    state = row[1]
    flag = 0
    if state == "Serve":
        tmp1 = x1
        tmp2 = y1
        # print "{0} starts the serve".format(x1.name)
        Score(state,x1,y1)
    elif state == "Ace":
        x1.add_point(y1)
        if flag == 1:
            Score(state,y1,x1)
        else:
            Score(state,x1,y1)
    elif state == "Fault":
        y1.add_point(x1)
        if flag == 1:
            Score(state,y1,x1)
        else:
            Score(state,x1,y1)
    elif state == "Forehand" or state == "Backhand":
        tmp = x1
        x1 = y1
        y1 = tmp
        if state == "Forehand":
            Score(state,x1,y1)
        else:
            Score(state,x1,y1)
    elif state == "PointLost‐CouldNotReach":
        x1.add_point(y1)
        if flag == 1:
            Score(state,y1,x1)
        else:
            Score(state,x1,y1)
    elif state == "PointLost-SameSide" or state == "PointLost-Out" or state == "Nets":
        y1.add_point(x1)
        if state == "PointLost‐SameSide":
            if flag == 1:
                Score(state,y1,x1)
            else:
                Score(state,x1,y1)
        elif state == "PointLost‐Out":
            if flag == 1:
                Score(state,y1,x1)
            else:
                Score(state,x1,y1)
        else:
            if flag == 1:
                Score(state,y1,x1)
            else:
                Score(state,x1,y1)
        x1 = tmp1
        y1 = tmp2

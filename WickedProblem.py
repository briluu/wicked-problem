#Siying Li, 1238928
#Chiho Kim, 0963203
#Brian Luu
#HW4, Wicked Problem

#<METADATA>
QUIET_VERSION = "0.2"
PROBLEM_NAME = "Wicked Problem"
PROBLEM_VERSION = "0.1"
PROBLEM_AUTHORS = ['Siying Li', 'Chiho Kim', 'Brian Luu']
PROBLEM_CREATION_DATE = "27-APR-2017"
PROBLEM_DESC=\
'''This formulation of the wicked problem of solving North Korea standoff 
uses generic Python 3 constructs and has been tested with Python 3.4.
It is designed to work according to the QUIET tools interface, Version 0.2.
'''
#</METADATA>
'''
#pass in list of countries, list of corresponding properties, <, >, =
def can_move(s, From, flag):
    if(flag == "miliaty trianion"):

    try:
        board = s.board
        return ((abs(From - To) == 1 or abs(From - To) == 3) and \
                (board[From] != 0 and board[To] == 0))
    except (Exception) as e:
        print(e)
'''

# specify the property to be changed as the parameter,
# i.e specific country, specific property, numbers to go down/up
def move(s, From, To):
    news = s.__copy__()
    board2 = news.board
    board2[To] = board2[From]
    board2[From] = 0
    return news

#not required
# def goal_test(s):
#     goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#     return s.board == goal_state

def goal_message(s):
    return "Done."

class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self,s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)

# our heuristics evaluation function
# calculate each country's number, and have a formula to take each country's number
# need to be the inverse of how good this state is in
def h1(state):
    "Counts the number of disks NOT at the destination peg."
    p3 = state.d['peg3']
    return 4 - len(p3)

#<STATE>
class State():
    def __init__(self, board):
        self.board = board

    def __str__(self):
        board = self.board
        return str(board)

    def __eq__(self, s2):
        if not(type(self) == type(s2)) : return False
        return self.board == s2.board

    def __hash__(self):
        return (str(self)).__hash__()

    def __copy__(self):
        news = State([])
        news.board = self.board[:]
        return news
#</STATE>


#<INITIAL_STATE>
def CREATE_INITIAL_STATE():
    countries = {}
    USA = {}
    USA = CREATE_COUNTRY(USA, 90, 94, 94, False, 91, 'right')
    countries['USA'] = USA
    Russia = {}
    Russia = CREATE_COUNTRY(Russia, 60, 96, 80, False, 55, 'right')
    countries['Russia'] = Russia
    China = {}
    China = CREATE_COUNTRY(China, 24, 10, 79, False, 83, 'left')
    countries['China'] = China
    NK = {}
    NK = CREATE_COUNTRY(NK, 0, 8, 30, False, 9, 'right')
    NK['dictator'] = 90
    countries['NK'] = NK
    SK = {}
    SK = CREATE_COUNTRY(SK, 90, 0, 52, False, 60, 'right' )
    countries['SK'] = SK
    Japan = {}
    Japan = CREATE_COUNTRY(Japan, 50, 0, 73, False, 60, 'right' )
    countries['Japan'] = Japan
    q = []
    vote = ['USA', 'China', 'South Korea', 'Japan']
    q.append(vote)
    hostility = []
    hostility = HOSTILITY(countries, hostility)
    return State(countries, q)

#</INITIAL_STATE>

def CREATE_COUNTRY(country, h, n, m, s, e, p):
    country['hostility'] = h
    country['nuclear'] = n
    country['military'] = m
    country['sanction'] = s
    country['economy'] = e
    country['party'] = p
    return country

def HOSTILITY(countries, hostility):
    del hostility[:]
    hostility.append(countries['USA']['hostility'])
    hostility.append(countries['Russia']['hostility'])
    hostility.append(countries['China']['hostility'])
    hostility.append(countries['SK']['hostility'])
    hostility.append(countries['Japan']['hostility'])
    hostility.sort();
    return hostility

#<GOAL_TEST>
# GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<OPERATORS>
# create each operator as a own instance,
move_combination = [(x,y) for x in range(0,9) for y in range(0,9)]
OPERATORS =[Operator("Move from index " + str(x) + " to index " + str(y), \
                     lambda s, x1=x, y1=y: can_move(s, x1,y1),\
                     lambda s, x1=x, y1=y: move(s, x1, y1))\
            for(x,y) in move_combination]

#<GOAL_MESSAGE_FUNCTION>
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

#<HEURISTICS> (optional)
HEURISTICS = [h1]
#</HEURISTICS>

print(CREATE_INITIAL_STATE())


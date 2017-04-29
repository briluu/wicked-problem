#Siying Li, 1238928
#Chiho Kim
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

import random

#pass in list of countries, list of corresponding properties, <, >, =
def can_move(s, flag):
    if(flag == "joint military training"):
        return s.countries['USA']['economy'] > 70 and s.countries['SK']['economy'] > 70
    elif(flag == "change ruling party"):
        curr = s.q[0];
        party = ['left', 'right']
        num = random.randint(0,1)
        return s.countries[curr]['party'] != party[num]
    elif(flag == "nk missle"):
        return s.countries['NK']['military'] > 70 and s.countries['NK']['dictator'] > 50
    elif(flag == "submarines"):
        return s.countries['USA']['military'] > 50 and s.countries['USA']['hostility'] > 50 \
               and s.countries['NK']['dictator'] > 70
    elif(flag == "funding"):




    try:
        board = s.board
        return ((abs(From - To) == 1 or abs(From - To) == 3) and \
                (board[From] != 0 and board[To] == 0))
    except (Exception) as e:
        print(e)


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
    def __init__(self, countries, q):
        self.countries = countries
        self.q = q

    # need to change later
    def __str__(self):
        countries = self.countries
        q = self.q
        return str(countries) + str(q)

    def __eq__(self, s2):
        if not (type(self) == type(s2)): return False
        countries1 = self.countries;
        countries2 = s2.countries;
        return countries1 == countries2


    def __hash__(self):
        return (str(self)).__hash__()

    def __copy__(self):
        news = State({})
        news.countries = self.countries.copy();
        news.q = self.q[:]
        return news
#</STATE>

#<INITIAL_STATE>
# INITIAL_STATE = State([1, 4, 2, 3, 7, 0, 6, 8, 5])
# CREATE_INITIAL_STATE = lambda: INITIAL_STATE
# Need to fill in
def CREATE_INITIAL_STATE():
    pass
#</INITIAL_STATE>

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

